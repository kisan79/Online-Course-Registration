from django.db import models
# from myadmin.models import CommonModel


# Faculty Model


class Faculty(models.Model):
    '''Faculty Model'''
    idno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=15)
    mobile = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    joined_date = models.DateField(auto_now=True)
    pic = models.ImageField(blank=True, upload_to="faculty_pics/")
    def __str__(self):
        return self.first_name