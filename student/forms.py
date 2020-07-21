from django import forms
from .models import Student

# Student Register Form


class StudentRegister(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets ={
            "first_name":forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "username":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "onblur":"ajaxCall('id_username','http://127.0.0.1:8000/student/check-username/','msgUsername')",
                }
            ),
            "mobile":forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "type":"tel",
                    "onblur": "ajaxCall('id_mobile','http://127.0.0.1:8000/student/check-mobile/','msgMobile')",
                }
            ),
            "email":forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "onblur": "ajaxCall('id_email','http://127.0.0.1:8000/student/check-email/','msgEmail')",
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ),
            "pic": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


# Student login form


class StudentLoginForm(forms.ModelForm):
    """Admin Login Form"""
    class Meta:
        model = Student
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