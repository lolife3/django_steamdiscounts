"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import show_from_db
from myapi.views import UserViewSet, DiscountsViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'discounts', DiscountsViewSet, basename="discounts")





urlpatterns = [
    path("admin", admin.site.urls),
    path("discounts", show_from_db, name='discounts'),
    path("discounts/search", show_from_db, name="search"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
