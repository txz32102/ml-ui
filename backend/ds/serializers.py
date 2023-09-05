from rest_framework import serializers
from .models import json_api_test

class testapi(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    def get_tags(self, instance):
        print("hello")

    class Meta:
        model = json_api_test
        fields = ('keyword', 'tags')