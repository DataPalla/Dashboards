from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse

from rest_framework.viewsets import ViewSet

from djqscsv import render_to_csv_response

from .models import Education

global_qs = None

class HomeViewSet(ViewSet):

    def render_login(self, request):

        return render(request, "login.html")
    
    def lvl_id_based_filters(self, request):

        data = request.POST
        lvl_id = data.get("lvl_id", None)

        labels = [i['education_level'] for i in Education.objects.values('education_level').distinct()]

        edu_dict = {course: 0 for course in labels}

        access_levels = {}

        for lvl in range(1, 11):

            access_level = Education.objects.filter(**{"lvl{}_id".format(lvl): lvl_id}).first()
            if access_level:
                break

        queryset = Education.objects.filter(**{"lvl{}_id".format(lvl): lvl_id})

        global global_qs
        global_qs = queryset

        grad_dict = self.grad_dict_generator(queryset)

        profession_dict = self.profession_dict_generator(queryset)

        user_count_per_education_level = queryset.values('education_level').annotate(distinct=Count("user_id"))

        for _ in user_count_per_education_level:

            edu_dict[_['education_level']] += _["distinct"]

        for i in range(1, 10):

            level_options = queryset.values('level{}'.format(i), 'lvl{}_id'.format(i)).distinct()

            level_options = [{
                "id": k['lvl{}_id'.format(i)],
                "string": k['level{}'.format(i)],
            } for k in level_options]

            access_levels[i] = level_options

        return render(request, "home.html", {"access_levels": access_levels, "educationLevel": edu_dict, "gradDict": grad_dict, "professionDict": profession_dict})

    def profession_dict_generator(self, queryset):
        profession_dict = {
            "None": 0,
            "Associate": 0,
            "Bachelors": 0,
            "Certificate": 0,
            "Diploma": 0,
            "Doctorate": 0,
            "High School": 0,
            "Masters": 0,
            "No Degree Awarded": 0,
        }

        distinct_profession_count = queryset.values("degree_name").distinct().annotate(users=Count("user_id"))

        for record in distinct_profession_count:
            if record["degree_name"] in ("PhD", "MD", ):
                profession_dict["Doctorate"] += record["users"]

            elif record["degree_name"] == None:
                profession_dict["None"] += record["users"]
            
            else:
                profession_dict[record["degree_name"]] += record["users"]

        return profession_dict

    def grad_dict_generator(self, queryset):
        grad_qs_data = queryset.values("anticipated_graduation_year").distinct().annotate(users=Count("user_id"))

        grad_dict = {year: 0 for year in ["Incomplete", "<2020", "2020", "2021", "2022", ">2022"]}

        for record in grad_qs_data:
            # record year will be in string, conversion to int needed for categorization
            if record["anticipated_graduation_year"]:
                record["anticipated_graduation_year"] = float(record["anticipated_graduation_year"])

                if record["anticipated_graduation_year"] > 2022.0:
                    record["anticipated_graduation_year"] = ">2022"

                elif record["anticipated_graduation_year"] < 2020.0:
                    record["anticipated_graduation_year"] = "<2020"

                else:
                    record["anticipated_graduation_year"] = int(record["anticipated_graduation_year"])
            
            else:
                record["anticipated_graduation_year"] = "Incomplete"
            
            grad_dict[str(record["anticipated_graduation_year"])] += record["users"]
        return grad_dict

    def filter_access_levels(self, request):

        global global_qs
        data = request.POST

        if data.get("get_csv", False):
            s = render_to_csv_response(global_qs)
            return s

        curr_level = int(data.get("level", 1))
        value = data.get("value", None)

        labels = [i['education_level'] for i in Education.objects.values('education_level').distinct()]

        if value == "all":

            filtered_qs = Education.objects.all()
        
        else:

            filtered_qs = Education.objects.filter(**{"lvl{}_id".format(curr_level): value})
        
        global_qs = filtered_qs

        grad_dict = self.grad_dict_generator(filtered_qs)
        profession_dict = self.profession_dict_generator(filtered_qs)

        if value != None:

            access_levels = {}

            edu_dict = {course: 0 for course in labels}

            for i in range(1, 10):

                level_options = filtered_qs.values("level{}".format(i), "lvl{}_id".format(i)).distinct()

                user_count = filtered_qs.values("education_level").annotate(distinct=Count("user_id"))

                for _ in user_count:

                    edu_dict[_['education_level']] += _["distinct"]

                level_options = [{
                    "id": k['lvl{}_id'.format(i)],
                    "string": k['level{}'.format(i)],
                } for k in level_options if k['level{}'.format(i)] != None]

                access_levels[i] = level_options

            return JsonResponse({"access_levels": access_levels, "currLevel": curr_level, "educationLevel": edu_dict, "gradDict": grad_dict, "professionDict": profession_dict})
