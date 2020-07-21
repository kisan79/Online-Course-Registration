from django import forms
from .models import Student

# Student Register Form


class StudentRegister(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets ={
            "username":forms.TextInput(
                attrs={
                    "onblur":"ajaxCall('id_username','http://127.0.0.1:8000/student/check-username/','msgUsername')",
                }
            ),
            "mobile":forms.NumberInput(
                attrs={
                    "type":"tel",
                    "onblur": "ajaxCall('id_mobile','http://127.0.0.1:8000/student/check-mobile/','msgMobile')",
                }
            ),
            "email":forms.EmailInput(
                attrs={
                    "onblur": "ajaxCall('id_email','http://127.0.0.1:8000/student/check-email/','msgEmail')",
                }
            )
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