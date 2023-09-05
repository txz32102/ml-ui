from django.db import models

class json_api_test(models.Model):
    keyword = models.CharField(max_length=100)
    tags = models.TextField(blank=True)