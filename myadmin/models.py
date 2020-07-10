from django.db import models

# Create your models here.


class AdminLoginModel(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    pic = models.ImageField(blank=True,upload_to="admin_pics/")
