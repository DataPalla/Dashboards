from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse

from rest_framework.viewsets import ViewSet

from .models import Education

class HomeViewSet(ViewSet):

    def render_login(self, request):

        return render(request, "login.html")
    
    def lvl_id_based_filters(self, request):

        data = request.POST
        lvl_id = data.get("lvl_id", None)

        labels = [i['education_level'] for i in Education.objects.values('education_level').distinct()]

        edu_dict = {course: 0 for course in labels}

        access_levels = {}

        access_level = None
        for lvl in range(1, 11):

            access_level = Education.objects.filter(**{"lvl{}_id".format(lvl): lvl_id}).first()
            if access_level:
                break

        queryset = Education.objects.filter(**{"lvl{}_id".format(lvl): lvl_id})

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

        return render(request, "home.html", {"access_levels": access_levels, "educationLevel": edu_dict})

    def filter_access_levels(self, request):

        data = request.POST
        curr_level = int(data.get("level", 1))
        value = data.get("value", None)

        labels = [i['education_level'] for i in Education.objects.values('education_level').distinct()]

        if value == "all":

            filtered_qs = Education.objects.all()
        
        else:

            filtered_qs = Education.objects.filter(**{"lvl{}_id".format(curr_level): value})

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

            return JsonResponse({"access_levels": access_levels, "currLevel": curr_level, "educationLevel": edu_dict})
