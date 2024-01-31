from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    # Add other fields as needed (e.g., upload date, user, etc.)
