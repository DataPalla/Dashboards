from django.urls import path
from .views import HomeViewSet

render_login = HomeViewSet.as_view({
    "get": "render_login"
})

lvl_id_based_filters = HomeViewSet.as_view({
    "post": "lvl_id_based_filters"
})

filter_access_levels = HomeViewSet.as_view({
    "post": "filter_access_levels"
})

urlpatterns = [
    path("", render_login),
    path("home/", lvl_id_based_filters, name="lvl_id_based_filters"),
    path("filter-access-levels/", filter_access_levels),
]
