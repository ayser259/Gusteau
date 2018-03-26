from rest_framework import serializers
from .models import *


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('name', 'street_number','street_name','postal_code')

class LocationSerializer(serializers.ModelSerializer):
    building = serializers.CharField(source='building.name', read_only=True)
    class Meta:
        model = Location
        fields = ('name', 'building','location_id')

class LocationHoursSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source='location.name', read_only=True)
    location_id = serializers.CharField(source='location.location_id',read_only=True)
    building = serializers.CharField(source='location.building.name',read_only=True)
    class Meta:
        model = LocationHours
        fields = ('location','day_of_week', 'opening_hour', 'closing_hour','location_id','building')

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        fields = ('username','password','email')

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='login.username',read_only=True)
    class Meta:
        model = User
        fields = ('username','first_name','surname')

class AdminUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.login.username',read_only=True)
    first_name = serializers.CharField(source='user.first_name',read_only=True)
    surname = serializers.CharField(source='user.surname',read_only=True)
    location = serializers.CharField(source='location.name',read_only=True)
    class Meta:
        model = AdminUser
        fields = ('username','first_name','surname','location')

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.login.username',read_only=True)
    first_name = serializers.CharField(source='user.first_name',read_only=True)
    surname = serializers.CharField(source='user.surname',read_only=True)
    class Meta:
        model = Student
        fields = ('username','first_name','surname','student_id')

class DietTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietType
        fields = ('diet_type_id','diet_type')

class FoodItemToLocationSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source='food.name', read_only=True)
    location = serializers.CharField(source='location.name',read_only=True)
    location_id = serializers.CharField(source='location.location_id',read_only=True)
    building = serializers.CharField(source='location.building.name',read_only=True)
    class Meta:
        model = FoodItemToLocation
        fields = ('food_name','location','building','location_id')

class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ('name', 'cal', 'weight', 'diet_type', 'average_rating', 'fat', 'fat_percent', 'sat_fat','sat_fat_percent', 'carbs', 'carbs_percent', 'sodium', 'sodium_percent', 'protein', 'protein_percent')

class MenuCalendarSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source='food_item_to_location.food.name', read_only=True)
    location = serializers.CharField(source='food_item_to_location.location.name',read_only=True)
    class Meta:
        model = MenuCalendar
        fields = ('food_name','location','date_available')

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.login.username',read_only=True)
    first_name = serializers.CharField(source='user.first_name',read_only=True)
    surname = serializers.CharField(source='user.surname',read_only=True)
    food_name = serializers.CharField(source='menu_calendar.food_item_to_location.food.name', read_only=True)
    class Meta:
        model = Review
        fields = ('star_rating', 'text', 'first_name', 'food_name','surname','username')

class FeedbackSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.login.username',read_only=True)
    first_name = serializers.CharField(source='user.first_name',read_only=True)
    surname = serializers.CharField(source='user.surname',read_only=True)
    location = serializers.CharField(source='location.name',read_only=True)
    class Meta:
        model = Feedback
        fields =('username','first_name','surname','location','text')

class FavoriteLocationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='student.user.login.username',read_only=True)
    first_name = serializers.CharField(source='student.user.first_name',read_only=True)
    surname = serializers.CharField(source='student.user.surname',read_only=True)
    location = serializers.CharField(source='location.name',read_only=True)
    class Meta:
        model = FavoriteLocation
        fields =('username','first_name','surname','location')
