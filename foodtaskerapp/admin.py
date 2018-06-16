from django.contrib import admin

# Register your models here.
from foodtaskerapp.models import Restaurant, Customer, Driver, Meal

admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal)
