from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Discount, ToDo
from .forms import SearchForm, UserLoginForm, ToDoForm
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
    context = {"form": UserCreationForm(),}
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User created succesfully!")
            return  redirect("login")
        else:
            messages.warning(request, f"{form.errors}")
            return render(request, "register.html", context)
            
    else:
        return render(request, "register.html", context)
    
    
    
def login_user(request):
    context = {"form": UserLoginForm(),}
    
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            messages.success(request, f"Logged in succesfully! Welcome, {request.POST['username']}")
            return render(request, "login.html", context)
        else:
            messages.warning(request, "Invalid username or password")
            return render(request, "login.html", context)

    else:
        return render(request, "login.html", context)
    
    
    
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out succesfully!")
    return redirect("login")



def todo(request):
    context = {"form": ToDoForm(),
               "data": ToDo.objects.all()}
    
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():    
            todo_object = ToDo(text=request.POST["todo_task"])
            todo_object.save()
            return render(request, "todo.html", context)
    
    
    return render(request, "todo.html", context)
    









'''
def db_test(request):
    #test func
    template = loader.get_template("discounts.html")
    return HttpResponse(template.render({"data": Discount.objects.all()}))
''' 
