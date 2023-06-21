from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import Discounts

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")
        

class DiscountsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discounts 
        fields = ("__all__")