from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import testapi
from .models import json_api_test


class testView(viewsets.ModelViewSet):
    serializer_class = testapi
    queryset = json_api_test.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = "hellop world"
        return Response(data)
    
    def create(self, request, *args, **kwargs):
        data = "hellop world"
        return Response(data, status=status.HTTP_201_CREATED)