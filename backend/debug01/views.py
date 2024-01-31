from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import MyData
from .serializers import MyDataSerializer

class MyDataViewSet(viewsets.ModelViewSet):
    queryset = MyData.objects.all()
    serializer_class = MyDataSerializer
