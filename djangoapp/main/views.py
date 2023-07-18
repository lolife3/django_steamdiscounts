from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Discount
from .forms import SearchForm, UserForm
from django.views.decorators.csrf import csrf_exempt



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
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User(username=request.POST["username"], password=request.POST["password1"])
            user.save()
            return render(request, "login.html", {"form": form,
                                                  "message": "User created succesfully!",})
        else:
            print(f"\n{form.errors.as_text()}\n")

    else:
        return render(request, "login.html", {"form": UserCreationForm()})









'''
def db_test(request):
    #test func
    template = loader.get_template("discounts.html")
    return HttpResponse(template.render({"data": Discount.objects.all()}))
''' 
