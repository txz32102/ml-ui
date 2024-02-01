from django.db import models

class MyData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='debug01/test_file/', null=True, blank=True)




