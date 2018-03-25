# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import BuildingSerializer
from django.http import HttpResponse
from .data_gen import *


from django.shortcuts import render

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

def data_gen(request):
    deta_generator()
    return HttpResponse("Data Genetation Method Ran")
