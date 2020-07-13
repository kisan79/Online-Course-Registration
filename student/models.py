from django.db import models
from myadmin.models import CommonModel

#Student Registration Model


class Student(CommonModel):
    pic = models.ImageField(blank=True, upload_to="student_pics/")
