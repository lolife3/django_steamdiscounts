from django.contrib.auth.models import User
from .serializers import  UserSerializer, DiscountSerializer
from main.models import Discount
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]
    


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_class = [permissions.IsAuthenticated]



class _DiscountViewSet(APIView):
    def get(self, request, format=None):
        queryset = Discount.objects.all()
        serializer = DiscountSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
