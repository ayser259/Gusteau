# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import HttpResponse
from .data_gen import *

from django.shortcuts import render

def data_gen(request):
    # This view is used to run a script to call the api and save the data
    deta_generator()
    return HttpResponse("Data Genetation Method Ran")

# Create your views here.
@api_view(['GET'])
def get_buildings(request):
    try:
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
    except Building.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_locations(request):
    try:
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_location_hours(request):
    try:
        location_hours = LocationHours.objects.all()
        serializer = LocationHoursSerializer(location_hours, many=True)
    except LocationHours.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_login(request):
    try:
        login = Login.objects.all()
        serializer = LoginSerializer(login, many=True)
    except Login.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_user(request):
    try:
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_adminuser(request):
    try:
        adminuser = AdminUser.objects.all()
        serializer = AdminUserSerializer(adminuser, many=True)
    except AdminUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_student(request):
    try:
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_diet_type(request):
    try:
        diet_type = DietType.objects.all()
        serializer = DietTypeSerializer(diet_type, many=True)
    except DietType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_food(request):
    try:
        food = Food.objects.all()
        serializer = FoodSerializer(food, many=True)
    except Food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_food_item_to_location(request):
    try:
        food_item_to_location = FoodItemToLocation.objects.all()
        serializer = FoodItemToLocationSerializer(food_item_to_location, many=True)
    except FoodItemToLocation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_menu_calendar(request):
    try:
        menu_calendar = MenuCalendar.objects.all()
        serializer = MenuCalendarSerializer(menu_calendar, many=True)
    except MenuCalendar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_review(request):
    try:
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_feedback(request):
    try:
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_favorite_location(request):
    try:
        favorite_location = FavoriteLocation.objects.all()
        serializer = FavoriteLocationSerializer(favorite_location, many=True)
    except FavoriteLocation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_favorite_location_for_student(request,student_id):
    try:
        favorite_location = FavoriteLocation.objects.all()
        favorite_location = favorite_location.filter(student=Student.objects.get(student_id=int(student_id)))
        serializer = FavoriteLocationSerializer(favorite_location, many=True)
    except FavoriteLocation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_menu_calendar_for_food(request,food_id):
    try:
        food_item_to_location_set = FoodItemToLocation.objects.filter(food=Food.objects.get(food_id=food_id))
        menu_calendar = MenuCalendar.objects.filter(food_item_to_location__in=food_item_to_location_set)
        serializer = MenuCalendarSerializer(menu_calendar, many=True)
    except MenuCalendar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_menu_calendar_for_location(request,location_id):
    try:
        food_item_to_location_set = FoodItemToLocation.objects.filter(location=Location.objects.get(location_id=location_id))
        menu_calendar = MenuCalendar.objects.filter(food_item_to_location__in=food_item_to_location_set)
        serializer = MenuCalendarSerializer(menu_calendar, many=True)
    except MenuCalendar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_review_for_user(request,user_id):
    try:
        review_set = Review.objects.filter(user=User.objects.get(user_id=user_id))
        serializer = ReviewSerializer(review_set, many=True)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET'])
def get_location_hours_for_location(request,location_id):
    try:
        location_hours_set = LocationHours.objects.filter(location=Location.objects.get(location_id=location_id))
        serializer = LocationHoursSerializer(location_hours_set, many=True)
    except LocationHours.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single location
    if request.method == 'GET':
        return Response(serializer.data)
    # delete a single location
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single location
    elif request.method == 'PUT':
        return Response({})


@api_view(['POST'])
def submit_review(request):
    if request.method == 'POST':
        post_dict = request.post_dict
        print(post_dict)
        try:
            review = Review()
            review.star_rating = post_dict['stat_rating']
            review.text = post_dict['review_text']
            review.user = User.objects.get(user_id=int(post_dict['review_user_id']))
            review.item = Food.objects.get(food_id = int(post_dict['review_food_id']))
            review.save()
        except:
            print("ERROR WITH REVIEW SUBMISSION")
