#Admin form


from django import forms
from .models import AdminLoginModel


class AdminLoginForm(forms.ModelForm):
    '''Admin Login Form'''

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