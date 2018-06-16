from django.http import JsonResponse

from foodtaskerapp.models import Restaurant
from foodtaskerapp.serializers import RestaurantSerializer

def customer_get_restaurant(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by("-id"),
        many = True
    ).data

    return JsonResponse({"restaurants": restaurants})
