from django.urls import path
from . import views

urlpatterns = [

    path('', views.get_distinct_education_level),
    path('raw', views.get_org_name),
    path('home/', views.get_level_info),
    path('filter/', views.filter)
    # path('', views.bar),
]
