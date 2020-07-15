from django import forms
from .models import Student

# Student Register Form


class StudentRegister(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


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