from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from foodtaskerapp.forms import UserForm, RestaurantForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return redirect(restaurant_home)

@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/home.html', {})

def restaurant_sign_up(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        restaurant_form = RestaurantForm(request.POST, request.FILES)
        #print(user_form.is_valid())
        #print(restaurant_form.is_valid())

        if user_form.is_valid() and restaurant_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_restaurant = restaurant_form.save(commit=False)
            new_restaurant.user = new_user
            new_restaurant.save()

            login(request,authenticate(
                username=user_form.cleaned_data["username"],
                password=user_form.cleaned_data["password"]
            ))

            return redirect(restaurant_home)

    return render(request, 'restaurant/sign_up.html', {
        "user_form": user_form,
        "restaurant_form": restaurant_form
    })
