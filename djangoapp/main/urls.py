from django.urls import path
from . import views


urlpatterns = [
    path("", views.base, name="base"),
    path("db_table", views.show_from_db)
]