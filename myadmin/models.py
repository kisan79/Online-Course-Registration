from django.db import models

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
    pic = models.ImageField(blank=True, upload_to="coursetype_logo/")

# Course Model


class Course(models.Model):
    '''Course Model'''
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40,unique=True)
    pic = models.ImageField(blank=True, upload_to="course_pics/")
    type = models.ManyToManyField(CourseType)
    fee = models.FloatField()