from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyDataViewSet

router = DefaultRouter()
router.register(r'mydata', MyDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
