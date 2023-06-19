from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    query = User.objects.all().order_by("-date_joined")
    serializer = UserSerializer
    permission = [permissions.IsAuthenticated]



class GroupViewSet(viewsets.ModelViewSet):
    query = Group.objects.all()
    serializer = GroupSerializer
    permission = [permissions.IsAuthenticated]

