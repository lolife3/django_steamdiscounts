from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .models import Discount
from .forms import SearchForm, UserForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def search_discount(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            return render(request, "discounts.html", {"data": Discount.objects.filter(title__icontains=request.POST["searched_titles"]),
                                                      "form": form})
 
    else:
        return render(request, "discounts.html", {"data": Discount.objects.all(),
                                              "form": SearchForm()})
    


def register_user(request):   
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "login.html", {"form": form})
        else:
            return(form.errors)
    else:  
        return render(request, "login.html", {"form": UserCreationForm()})









'''
def db_test(request):
    #test func
    template = loader.get_template("discounts.html")
    return HttpResponse(template.render({"data": Discount.objects.all()}))
''' 
