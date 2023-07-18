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
from main import views
from myapi.views import UserViewSet, DiscountViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'discounts', DiscountViewSet, basename="discount")





urlpatterns = [
    path("", views.home_page, name="home"),
    path("login", views.login_user, name="login"),
    path("register", views.register_user, name="register"),
    path("admin", admin.site.urls),
    path("discounts", views.search_discount, name='discounts'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
