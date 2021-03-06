# coding=utf-8
from __future__ import unicode_literals
import requests, datetime, json,requests,sys, random,os,django
from random import randint
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gusteau.settings")
from kitchen.models import *
'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
'''
def deta_generator():
    try:
        user_set = User.objects.all()
        building_set = Building.objects.all()
        user_set.delete()
        building_set.delete()
        login_set = Login.objects.all()
        login_set.delete()
        diets= DietType.objects.all()
        diets.delete()
        food_set = Food.objects.all()
        food_set.delete()
    except:
        q =1
    os.environ['UW_API_KEY'] = '2cdafc74c7a20fcec6c0d766947f4919'
    from uwaterloodriver import UW_Driver
    uw_driver = UW_Driver()
    uw_driver.foodservices_diets()
    # plan tier 1: building, locsation, locationHours
    a = uw_driver.foodservices_locations()

    for item in a:
        try:
            current_bulding = Building.objects.get(name = item['building'])
        except:
            if item['building'] == None:
                try:
                    current_bulding = Building.objects.get(name = 'SCH')
                except:
                    new_building = Building()
                    new_building.name = 'SCH'
                    new_building.street_number = 200
                    new_building.street_name = 'University Avenue West'
                    new_building.postal_code = 'N2L 3G1'
                    new_building.save()
            else:
                new_building = Building()
                new_building.name = item['building']
                new_building.street_number = 200
                new_building.street_name = 'University Avenue West'
                new_building.postal_code = 'N2L 3G1'
                new_building.save()

    for item in a:
        new_location = Location()
        new_location.name = item['outlet_name']
        if item['building'] == 'None' or item['building'] == None:
            new_location.building = None
        else:
            new_location.building = Building.objects.get(name =item['building'])
        new_location.save()

        times = item['opening_hours']
        time_keys = list(times.keys())
        for day in time_keys:
            hour_dict = times[day]
            location_hours = LocationHours()
            location_hours.location = new_location
            location_hours.day_of_week = day
            try:
                location_hours.opening_hour = datetime.datetime.strptime(hour_dict['opening_hour'], '%H:%M')
            except:
                location_hours.opening_hour = None
            if str(hour_dict['closing_hour']) == "None":
                x = 2
            else:
                location_hours.closing_hour = datetime.datetime.strptime((hour_dict['closing_hour']), '%H:%M')
            location_hours.save()

    # Tier 2 Create Valid User Data:
    # This Includes Login, User, AdminUser, Student
    first_names =  ['Fatima','Juan','Sara','Santiago','Ayser','Sofía', 'Aaron', 'Ahmad', 'Elie','Jing','Tamar','Avigail','Sakura','Marc','Zahra','Olivia','Elise','Dominique','Yasmine', 'Sofia','Pooja', 'Victoria']
    last_names = ['Arvo','Li','Yim','Wang','Nguyen','Choudhury', 'Patel', 'Hernandez', 'Smith','Smirnov','Müller','Concettina']

    x = randint(0, len(first_names)-1)
    y = randint(0,len(last_names)-1)

    for i in range(0,100):
        x = randint(0, len(first_names)-1)
        y = randint(0,len(last_names)-1)

        first_name = first_names[x]
        surname =last_names[y]

        login = Login()
        login.username = first_name[0:3]+surname[0:3]+str(x)+str(y)
        login.email = first_name + surname +"@uwaterloo.ca"
        login.password = "AyserVictoriaAaronPooja"
        login.save()

        user = User()
        user.login = login
        user.first_name = first_name
        user.surname = surname
        user.save()

        student = Student()
        student.user = user
        student.save()
        student.student_id = int("20600"+str(student.student_id))
        student.save()

    location_set = Location.objects.all()
    student_set = Student.objects.all()

    for location in location_set:
        z = randint(0,(len(student_set)-1))
        student = student_set[z]
        user = student.user
        admin_user = AdminUser()
        admin_user.user = user
        admin_user.location = location
        admin_user.save()
        student.delete()
        student_set = Student.objects.all()

    diet_type = DietType()
    diet_type.diet_type = "Non Vegetarian"
    diet_type.save()

    diet_type = DietType()
    diet_type.diet_type = "Vegan"
    diet_type.save()

    diet_type = DietType()
    diet_type.diet_type = "Halal"
    diet_type.save()

    diet_type = DietType()
    diet_type.diet_type = "Vegetarian"
    diet_type.save()

    # Tier 3 Create Food, FoodItemToLocation,MenuCalendar, Review, Feedback
    for i in range(0,1000):
        try:
            menu = uw_driver.foodservices_products(i)
            print(menu)
            if len(menu)>0:
                food = Food()
                food.product_id = (menu['product_id'])
                food.cal = menu['calories']
                food.name = menu['product_name']
                food.weight = menu['serving_size']
                food.fat = (menu['total_fat_g'])
                food.fat_percent = menu['total_fat_percent']
                food.sat_fat =(menu['fat_saturated_g'])
                food.sat_fat_percent =(menu['fat_saturated_percent'])
                food.sodium =(menu['sodium_mg'])
                food.sodium_percent =(menu['sodium_percent'])
                food.carbs =(menu['carbo_g'])
                food.carbs_percent =(menu['carbo_percent'])
                food.protein =(menu['protein_g'])
                y = randint(15,85)
                food.protein_percent = y
                food.diet_type=DietType.objects.get(diet_type=menu['diet_type'])
                food.average_rating = randint(0,5)
                food.save()
        except:
            x = 1
            print("Tossed Error 1")
    print("Alpha")
    location_set = Location.objects.all()
    food_set = Food.objects.all()
    print('food_set')
    print(len(location_set))

    for item in location_set:
        x = randint(2,10)
        food_list = []
        for i in range(0,x):
            relation = FoodItemToLocation()
            relation.location = item
            y = randint(0,len(food_set)-1)
            while y in food_list:
                y = y+1
                if y >= len(food_set):
                    y = y/2
            food_list.append(y)
            try:
                relation.food = food_set[y]
                relation.save()
            except:
                print("Tossed an Error 2")

    future_dates_available = ['2018-04-02','2018-04-03','2018-04-04','2018-04-05','2018-04-06','2018-04-07','2018-04-08','2018-04-09','2018-04-10','2018-04-11','2018-04-12','2018-04-13','2018-04-14']
    past_dates_available = ['2018-03-09','2018-03-10','2018-03-11','2018-03-12','2018-03-13','2018-03-14','2018-03-15','2018-03-16','2018-03-17','2018-03-18','2018-03-19','2018-03-20','2018-03-21','2018-03-22','2018-03-23','2018-03-24','2018-03-25','2018-03-26','2018-03-27','2018-03-28','2018-03-29','2018-03-30','2018-04-01']
    geo_food_set = FoodItemToLocation.objects.all()
    user_set = User.objects.all()
    for item in geo_food_set:
        for i in range(1,5):
            food_list = []
            calendar = MenuCalendar()
            calendar.food_item_to_location = item
            y = randint(0,len(future_dates_available)-1)
            while y in food_list:
                y = y+1
                if y >= len(future_dates_available):
                    y = y-int(y/2)
            food_list.append(y)
            try:
                print("Al")
                calendar.data_available = future_dates_available[y]
                print("Gore")
                print(calendar)
                print(str(calendar))
                calendar.save()

                print("ASDF")
            except:
                print("Tossed an error 3")

    lorem = "Lorem ipsum dolor sit amet, probo sanctus ius ad, ei inani latine gubergren eum. Sumo fugit conceptam ad est, partem interpretaris at cum. Eos corpora vituperata ea, qui cu utroque eloquentiam. Cibo porro efficiendi eu nam, te fabellas philosophia qui."

    food_set = Food.objects.all()
    user_set = User.objects.all()
    for i in range(0,100):
        review = Review()
        y = randint(0,len(past_dates_available)-1)
        review.data_available = past_dates_available[y]
        review.star_rating = randint(0,5)
        y = randint(0,len(user_set)-1)
        review.user = user_set[y]
        y = randint(0,len(food_set)-1)
        review.item = food_set[y]
        review.text = lorem
        review.save()

    for i in range(0,100):
        feedback = Feedback()
        feedback.text = lorem
        y = randint(0,len(user_set)-1)
        feedback.user = user_set[y]
        y = randint(0,len(location_set)-1)
        feedback.location = location_set[y]
        feedback.save()

    student_set = Student.objects.all()
    location_set = Location.objects.all()

    for student in student_set:
        loc_list = []
        for i in range(0,3):
            fav_location = FavoriteLocation()
            fav_location.student =  student
            y = randint(0,len(location_set)-1)
            while y in loc_list:
                y=y+1
                if y>=len(location_set):
                    y = int(y/2)
            fav_location.location = location_set[y]
            loc_list.append(y)
            fav_location.save()
