from django.shortcuts import render
from rest_framework import viewsets

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


# Create your views here.

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer