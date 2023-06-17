from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Discounts 
from .forms import SearchForm


def show_from_db(request):
    context = {
        "form": SearchForm(),
        "data": None
    }
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            context["data"] = Discounts.objects.filter(title__icontains=request.POST["searched_titles"])
            return render(request, "discounts.html", context)
    else:
        context["data"] = Discounts.objects.all()
        return render(request, "discounts.html", context)

'''
def db_test(request):
    #test func
    template = loader.get_template("discounts.html")
    return HttpResponse(template.render({"data": Discounts.objects.all()}))
''' 
