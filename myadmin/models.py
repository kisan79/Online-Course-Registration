from django.db import models

# Create your models here.


class AdminLoginModel(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=15)
    mobile = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    pic = models.ImageField(blank=True,upload_to="admin_pics/")
