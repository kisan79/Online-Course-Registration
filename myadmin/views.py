from django.shortcuts import render
from django.http import HttpResponse
from .forms import AdminLoginForm


def admin_login(request):
    '''The FBV returns a HttpResponse with AdminLoginForm'''
    return render(request,template_name="myadmin/admin_login.html",context={'AdminLoginForm':AdminLoginForm()})