# Generated by Django 5.0.1 on 2024-01-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debug01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydata',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
