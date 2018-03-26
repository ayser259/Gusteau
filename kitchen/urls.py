from django.conf.urls import url
from . import views

urlpatterns = [
    url('data_gen', views.data_gen, name='data_gen'),
    url(
    r'^api/v1/kitchen/menu_calendar_for_food/(?P<food_id>[0-9]+)/$',
        views.get_menu_calendar_for_food,
        name='get_menu_calendar_for_food'
    ),
    url(
    r'^api/v1/kitchen/menu_calendar_for_location/(?P<location_id>[0-9]+)/$',
        views.get_menu_calendar_for_location,
        name='get_menu_calendar_for_location'
    ),
    url(
    r'^api/v1/kitchen/review_for_user/(?P<user_id>[0-9]+)/$',
        views.get_review_for_user,
        name='get_review_for_user'
    ),
    url(
    r'^api/v1/kitchen/favorite_location_for_student/(?P<student_id>[0-9]+)/$',
        views.get_favorite_location_for_student,
        name='get_favorite_location_for_student'
    ),

    url(
        r'^api/v1/kitchen/submit_review',
        views.submit_review,
        name='submit_review'
    ),
    url(
        r'^api/v1/kitchen/buildings',
        views.get_buildings,
        name='get_buildings'
    ),
    url(
        r'^api/v1/kitchen/locations',
        views.get_locations,
        name='get_locations'
    ),
    url(
        r'^api/v1/kitchen/location_hours',
        views.get_location_hours,
        name='get_location_hours'
    ),
    url(
        r'^api/v1/kitchen/login',
        views.get_login,
        name='get_login'
    ),
    url(
        r'^api/v1/kitchen/user',
        views.get_user,
        name='get_user'
    ),

    url(
        r'^api/v1/kitchen/adminuser',
        views.get_adminuser,
        name='get_adminuser'
    ),

    url(
        r'^api/v1/kitchen/student',
        views.get_student,
        name='get_student'
    ),

    url(
        r'^api/v1/kitchen/diet_type',
        views.get_diet_type,
        name='get_diet_type'
    ),
    url(
        r'^api/v1/kitchen/foodloc',
        views.get_food_item_to_location,
        name='get_food_item_to_location'
    ),
    url(
        r'^api/v1/kitchen/food',
        views.get_food,
        name='get_food'
    ),

    url(
        r'^api/v1/kitchen/menu_calendar',
        views.get_menu_calendar,
        name='get_menu_calendar'
    ),

    url(
        r'^api/v1/kitchen/review',
        views.get_review,
        name='get_review'
    ),

    url(
        r'^api/v1/kitchen/feedback',
        views.get_feedback,
        name='get_feedback'
    ),

    url(
        r'^api/v1/kitchen/favorite_location',
        views.get_favorite_location,
        name='get_favorite_location'
    )

]
