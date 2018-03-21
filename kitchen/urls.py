from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/kitchen/buildings',
        views.get_buildings,
        name='get_buildings'
    )
]
