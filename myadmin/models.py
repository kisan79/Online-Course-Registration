from django.db import models
from django.utils import timezone

from faculty.models import Faculty

# Common Register Model


class CommonModel(models.Model):
    '''Common Register Model'''
    idno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=15)
    mobile = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()


    class Meta:
        abstract = True


# Admin Login Model


class AdminLoginModel(CommonModel):
    '''Admin Model'''
    pic = models.ImageField(blank=True, upload_to="admin_pics/")

# Course Type Model


class CourseType(models.Model):
    '''Different Trending Types Of Courses'''
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

# Course Model


class Course(models.Model):
    '''Course Model'''
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40,unique=True)
    pic = models.ImageField(blank=True, upload_to="course_pics/")
    type = models.ManyToManyField(CourseType)
    def __str__(self):
        return self.name

# Schedule Batch Model


class ScheduleBatch(models.Model):
    idno = models.AutoField(primary_key=True)
    course_name = models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty_name = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    batch_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    fee = models.FloatField()
    start_date = models.DateField(default=timezone.now)
    time = models.TimeField()

    def __str__(self):
        return self.course_name.name
