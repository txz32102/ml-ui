from rest_framework import serializers
from .models import MyData

class MyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyData
        fields = ['id', 'created_at', 'title', 'description', 'file']  # Include 'file' here
