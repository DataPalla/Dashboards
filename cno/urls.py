from django.urls import path
from . import views

urlpatterns = [

    path('', views.get_distinct_education_level),
    path('raw', views.get_org_name),
    # path('', views.bar),
]
