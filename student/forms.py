from django import forms
from .models import Student

# Student Register Form


class StudentRegister(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

