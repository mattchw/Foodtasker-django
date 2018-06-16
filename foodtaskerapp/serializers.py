from rest_framework import serializers

from foodtaskerapp.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id","name","phone","address","logo")
