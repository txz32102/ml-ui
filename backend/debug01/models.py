from django.db import models

class MyData(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/', null=True, blank=True)   # Add this line
