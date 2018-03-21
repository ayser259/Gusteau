# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Building)
admin.site.register(Location)
admin.site.register(LocationHours)
admin.site.register(Login)
admin.site.register(User)
admin.site.register(AdminUser)
admin.site.register(Student)
admin.site.register(DietType)
admin.site.register(Food)
admin.site.register(FoodItemToLocation)
admin.site.register(MenuCalendar)
admin.site.register(Review)
admin.site.register(Feedback)
