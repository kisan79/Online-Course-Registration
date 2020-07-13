from django.db import models
from myadmin.models import CommonModel


# Faculty Model


class Faculty(CommonModel):
    '''Faculty Model'''
    joined_date = models.DateField(auto_now=True)
    pic = models.ImageField(blank=True, upload_to="faculty_pics/")