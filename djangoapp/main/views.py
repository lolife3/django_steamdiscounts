from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Discounts 

def base(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())


def show_from_db(request):
    data = Discounts.objects.all()
    return render(request, "new_table.html", {"data": data})

def db_test(request):
    template = loader.get_template("new_table.html")
    return HttpResponse(template.render({"data": Discounts.objects.all()}))
    
