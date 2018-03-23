from django.conf.urls import url
from . import views

urlpatterns = [
    url('data_gen', views.data_gen, name='data_gen'),
    url(
        r'^api/v1/kitchen/buildings',
        views.get_buildings,
        name='get_buildings'
    )

]
