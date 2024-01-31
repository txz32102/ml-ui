from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from debug01.views import MyDataViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('debug01.urls')),
]