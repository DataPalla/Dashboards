from typing import List
from django.db import connection
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.shortcuts import render
from django.db.models import Q, Count
from .models import *
from json import dumps
from django.http import JsonResponse, response

def get_distinct_education_level(request):
    data = Education.objects.values('education_level').annotate(distinct=Count('user_id', distinct=True))
    l1 = data[0]['education_level']
    l2 = data[1]['education_level']
    l3 = data[2]['education_level']
    l4 = data[3]['education_level']
    d1 = data[0]['distinct']
    d2 = data[1]['distinct']
    d3 = data[2]['distinct']
    d4 = data[3]['distinct']
    return render(request, 'main.html', {'a': l1, 'b': l2, 'c': l3, 'd': l4, 'e': d1, 'f': d2, 'g': d3, 'h': d4})


def get_level_info(request):

    labels = [i['education_level'] for i in Education.objects.values('education_level').distinct()]

    edu_dict = {course: 0 for course in labels}

    info = {}

    qs = Education.objects.all()

    hi = qs.values('education_level').annotate(distinct=Count("user_id"))

    for _ in hi:

        edu_dict[_['education_level']] += _["distinct"]

    for i in range(1, 10):

        level_options = qs.values('level{}'.format(i), 'lvl{}_id'.format(i)).distinct()

        level_options = [{
            "id": k['lvl{}_id'.format(i)],
            "string": k['level{}'.format(i)],
        } for k in level_options]

        info[i] = level_options

    return render(request, "main.html", {"info": info, "educationLevel": edu_dict})

def filter(request):

    data = request.POST
    curr_level = int(data.get("level", 1))
    value = data.get("value", None)

    labels = [i['education_level'] for i in Education.objects.values('education_level').distinct()]

    if value == "all":

        filtered_qs = Education.objects.all()
    
    else:

        filtered_qs = Education.objects.filter(**{"lvl{}_id".format(curr_level): value})

    if value != None:

        info = {}

        edu_dict = {course: 0 for course in labels}

        for i in range(1, 10):

            level_options = filtered_qs.values("level{}".format(i), "lvl{}_id".format(i)).distinct()

            hi = filtered_qs.values("education_level").annotate(distinct=Count("user_id"))

            for _ in hi:

                edu_dict[_['education_level']] += _["distinct"]

            level_options = [{
                "id": k['lvl{}_id'.format(i)],
                "string": k['level{}'.format(i)],
            } for k in level_options if k['level{}'.format(i)] != None]

            info[i] = level_options

        return JsonResponse({"info": info, "currLevel": curr_level, "educationLevel": edu_dict})


def get_org_name(request):
    org_names = Education.objects.values_list('org_name').distinct()
    return render(request, 'raw.html', {'org_names': org_names})
