# Faculty Form


from django import forms
from .models import Faculty



class FacultyForm(forms.ModelForm):


    class Meta:
        model = Faculty
        fields = "__all__"
        widgets = {
            "password":forms.PasswordInput(
                attrs={
                    "placeholder":"Enter Password",
                    "class":"form-control-lg",
                }
            ),
            "first_name":forms.TextInput(
                attrs={
                    "placeholder":"First Name",
                    "class":"form-control-lg",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Last Name",
                    "class": "form-control-lg",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Enter Username",
                    "class": "form-control-lg",
                }
            ),
            "mobile": forms.NumberInput(
                attrs={
                    "placeholder": "10 Digit mobile",
                    "class": "form-control-lg",
                    "type":"tel",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email ID",
                    "class": "form-control-lg",
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "placeholder": "Address",
                    "class": "form-control",
                }
            ),
        }