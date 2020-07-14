from django import forms
from .models import *

# Admin form


class AdminLoginForm(forms.ModelForm):
    """Admin Login Form"""
    class Meta:
        model = AdminLoginModel
        fields = ('username','password')
        widgets = {
            "username":forms.TextInput(
                attrs={
                    "class":"form-control-lg",
                    "placeholder":"Enter Your Username"
                }
            ),
            "password":forms.PasswordInput(
                attrs={
                    "class":"form-control-lg",
                    "placeholder":"Enter Your Password"
                }
            )
        }


# CourseType Form

class CourseTypeForm(forms.ModelForm):
    """CourseType Form"""
    class Meta:
        model = CourseType
        fields = "__all__"
        exclude = ("idno",)
    name = forms.CharField(
        label="Course Type",
        widget=forms.TextInput(
            attrs={
                "class":"form-control-lg",
                "placeholder":"Course Type Name"
            }
        )
    )
    pic = forms.ImageField(
        label="Logo",
        required=False,
        widget=forms.FileInput(
            attrs={
                "class":"form-control-md",
            }
        )
    )

# Course Form


class CourseForm(forms.ModelForm):
    """Course Form"""
    class Meta:
        model = Course
        fields = "__all__"
        exclude = ("idno",)

    name = forms.CharField(
        label= 'Course Name',
        widget=forms.TextInput(
            attrs={
                "class":"form-control-lg",
                "placeholder":"Course Name"
            }
        )
    )

    pic = forms.ImageField(
        label="Image",
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "form-control-md",
            }
        )
    )

class ScheduleBatchForm(forms.ModelForm):
    BATCH_CHOICES = (
        ("Class Room Training","Class Room Training"),
        ("Online Training","Online Training"),
        ("Weekend Training","Weekend Training"),
        ("Special Batch","Special Batch"),
        ("Job Placement","Job Placement")
    )
    class Meta:
        model = ScheduleBatch
        fields = "__all__"
        exclude = ("idno",)
        widgets ={
            "time":forms.TimeInput(
                attrs={
                    "type":"time",
                    "class":"form-control-lg"
                },
                                   ),
            "start_date":forms.DateInput(
                attrs={
                    "class":"form-control-lg",
                    "type":"date"
                },
            )
        }
    batch_type = forms.ChoiceField(
        choices=BATCH_CHOICES,
        label="Type",
        widget=forms.Select(
            attrs={
                "class":"form-control"
            }
        )
    )


    fee = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control-lg",
                "step": 0.01,
                "min": 0
            }
        )
    )

