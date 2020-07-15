from django.db import models
from myadmin.models import CommonModel

#Student Registration Model


class Student(CommonModel):
    pic = models.ImageField(blank=True, upload_to="student_pics/")
    def __str__(self):
        return self.first_name

class BatchEnrollement(models.Model):

    mobile = models.BigIntegerField()
    batch_id = models.IntegerField()
