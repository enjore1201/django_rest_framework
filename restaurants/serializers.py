from django.contrib.auth.models import User
from rest_framework import serializers

from restaurants.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"  # 모든 필드를 읽기 및 쓰기가 가능하도록 설정




