from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Discount
from .forms import SearchForm, UserLoginForm
from django.views.decorators.csrf import csrf_exempt



def home_page(request):
    return render(request, "base.html")


def search_discount(request): 
    context = {
            "form": SearchForm(),
            "data": None
        }
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            context["data"] = Discount.objects.filter(title__icontains=request.POST["searched_titles"])
            return render(request, "discounts.html", context)
    else:
        context["data"] = Discount.objects.all()
        return render(request, "discounts.html", context)    



def register_user(request):   
    context = {"form": UserCreationForm(),
                "message": ""}
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User(username=request.POST["username"], password=request.POST["password1"])
            user.save()
            return render(request, "login.html", {"message": "User created succesfully!",})
        else:
            context["message"] = f"\n{form.errors.as_text()}\n"
            return render(request, "register.html", context)
            
    else:
        return render(request, "register.html", context)
    
    
    
def login_user(request):
    context = {"form": UserLoginForm(),
               "message": ""}
    
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            context["message"] = f"Welcome, {request.POST['username']}"
            return render(request, "base.html", context)
        else:
            context["message"] = "Invalid username or password"
            return render(request, "login.html", context)

    else:
        return render(request, "login.html", context)









'''
def db_test(request):
    #test func
    template = loader.get_template("discounts.html")
    return HttpResponse(template.render({"data": Discount.objects.all()}))
''' 
