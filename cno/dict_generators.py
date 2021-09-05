from django.db.models import Count

class DictGeneratorFactory:

    def access_levels_generator(self, queryset):
        access_levels = {}
        for i in range(1, 10):
            level_options = queryset.values("level{}".format(i), "lvl{}_id".format(i)).distinct()

            level_options = [{
                "id": k['lvl{}_id'.format(i)],
                "string": k['level{}'.format(i)],
            } for k in level_options if k['level{}'.format(i)] != None]

            access_levels[i] = level_options
        return access_levels

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

    def edu_dict_generator(self, queryset):
        edu_dict_values = queryset.values("education_level").distinct().annotate(users=Count("user_id"))
        edu_dict = {record["education_level"]: record["users"] for record in edu_dict_values}
        return edu_dict