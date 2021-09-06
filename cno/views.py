import json

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.viewsets import ViewSet

from djqscsv import render_to_csv_response

from .models import Education
from .dict_generators import DictGeneratorFactory

dict_generator_factory = DictGeneratorFactory()

class HomeViewSet(ViewSet):

    QUERYSET_CARRIER = None

    def render_login(self, request):

        return render(request, "login.html")
    
    def lvl_id_based_filters(self, request):

        data = request.POST
        lvl_id = data.get("lvl_id", None)

        access_levels = {}

        for lvl in range(1, 10):
            access_level = Education.objects.filter(**{"lvl{}_id".format(lvl): lvl_id}).first()
            if access_level:
                break

        queryset = Education.objects.filter(**{"lvl{}_id".format(lvl): lvl_id})

        self.__class__.QUERYSET_CARRIER = queryset

        grad_dict = dict_generator_factory.grad_dict_generator(queryset)
        profession_dict = dict_generator_factory.profession_dict_generator(queryset)
        edu_dict = dict_generator_factory.edu_dict_generator(queryset)
        access_levels = dict_generator_factory.access_levels_generator(queryset)

        return render(
            request,
            "home.html",
            {
                "access_levels": access_levels,
                "educationLevel": edu_dict,
                "gradDict": grad_dict,
                "professionDict": profession_dict,
                "highestLvl": lvl
            }
        )

    def filter_access_levels(self, request):

        data = request.POST

        if data.get("get_csv", False):
            s = render_to_csv_response(self.__class__.QUERYSET_CARRIER)
            return s

        lvl_array = json.loads(data.get("lvl_array", None))

        queryset = Education.objects.all()

        for level_obj in lvl_array[1:]:

            if level_obj["curr_level_id"] == "all":
                break

            queryset = queryset.filter(
                **{
                    "lvl{}_id".format(level_obj["curr_level"]): level_obj["curr_level_id"]
                }
            )
        
        self.__class__.QUERYSET_CARRIER = queryset

        grad_dict = dict_generator_factory.grad_dict_generator(queryset)
        profession_dict = dict_generator_factory.profession_dict_generator(queryset)
        edu_dict = dict_generator_factory.edu_dict_generator(queryset)
        access_levels =  dict_generator_factory.access_levels_generator(queryset)

        return JsonResponse({
            "access_levels": access_levels,
            "educationLevel": edu_dict,
            "gradDict": grad_dict,
            "professionDict": profession_dict
        })
