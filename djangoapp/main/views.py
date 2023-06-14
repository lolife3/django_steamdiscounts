from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Discounts 
from .forms import SearchForm



def base(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())


def show_from_db(request):
    data = Discounts.objects.all()
    return render(request, "discounts.html", {"data": data})

def get_titles(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            ...
    

'''
def db_test(request):
    #test func
    template = loader.get_template("discounts.html")
    return HttpResponse(template.render({"data": Discounts.objects.all()}))
''' 
