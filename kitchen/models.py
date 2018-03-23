# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Building(models.Model):
    # Campus Building Model

    building_id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)

    def __repr__(self):
        return str(self.building_id) + ": " + self.name + ' is added.'

    def __str__(self):
        return str(self.building_id) + ": " + self.name

class Location(models.Model):
    # Food Service Location

    location_id = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.location_id) + ": " + self.name

class LocationHours(models.Model):
    # Operatng hours of a given Location

    location_hours_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    opening_hour = models.TimeField(null=True)
    closing_hour = models.TimeField(null=True)

    def __str__(self):
        return str(self.location_hours_id) +" :" + self.day_of_week +" , opening_hour: "+str(self.opening_hour)+" , closing_hour: "+str(self.closing_hour)

class Login(models.Model):
    # User Login LoginInformation

    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length =40)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

    def __str__(self):
        return str(self.login_id)+": "+ self.username

class User(models.Model):
    # User Profile information

    user_id = models.AutoField(primary_key=True)
    login = models.ForeignKey(Login,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user_id)+": "+ self.first_name+" "+self.surname

class AdminUser(models.Model):
    # Additional Information for Admin USER

    admin_user_id = models.AutoField(primary_key=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.admin_user_id)+": "+ self.user.first_name +" location: "+self.location.name

class Student(models.Model):
    # Additional Information for Student USER

    student_id = models.AutoField(primary_key=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student_id)+" "+str(self.user.first_name)+" "+str(self.user.surname)

class DietType(models.Model):
    # Veggie, Halal or Vegan

    diet_type_id = models.AutoField(primary_key = True)
    diet_type = models.CharField(max_length=20)

    def __str__(self):
        return str(self.diet_type_id)+" "+str(self.diet_type)

class Food(models.Model):

    food_id = models.AutoField(primary_key= True)
    product_id = models.IntegerField(null=True)
    name = models.CharField(max_length=40)
    cal = models.IntegerField(null=True)
    weight = models.CharField(max_length=40)
    diet_type = models.ForeignKey(DietType,on_delete=models.CASCADE)
    average_rating = models.FloatField(null=True)

    fat = models.IntegerField(null=True)
    fat_content = models.IntegerField(null=True)
    fat_percent = models.IntegerField(null=True)

    sat_fat = models.IntegerField(null=True)
    sat_fat_content = models.IntegerField(null=True)
    sat_fat_percent = models.IntegerField(null=True)

    carbs = models.IntegerField(null=True)
    carbs_content = models.IntegerField(null=True)
    carbs_percent = models.IntegerField(null=True)

    sodium = models.IntegerField(null=True)
    sodium_content = models.IntegerField(null=True)
    sodium_percent = models.IntegerField(null=True)

    protein = models.IntegerField(null=True)
    protein_content = models.IntegerField(null=True)
    protein_percent = models.IntegerField(null=True)


    def __str__(self):
        return str(self.food_id)+" "+str(self.name)+" " + str(self.cal)

class FoodItemToLocation(models.Model):

    food_item_to_location_id = models.AutoField(primary_key=True)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.food_item_to_location_id)+" "+str(self.food.name)+" "+str(self.location.name)


class MenuCalendar(models.Model):

    menu_calendar_id = models.AutoField(primary_key=True)
    food_item_to_location = models.ForeignKey(FoodItemToLocation,on_delete=models.CASCADE)
    data_available = models.DateField()

    def __str__(self):
        return str(self.menu_calendar_id)+" "+str(self.food_item_to_location.location.name)+" "+str(self.data_available)


class Review(models.Model):

    review_id = models.AutoField(primary_key=True)
    star_rating = models.FloatField()
    text = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(MenuCalendar,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.review_id)+ " "+ str(self.user.user_id)+" "+str(self.star_rating)


class Feedback(models.Model):

    feedback_id = models.AutoField(primary_key=True)
    text = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.feedback_id)+ " "+ str(self.user.user_id)+" "+str(self.location.name)
