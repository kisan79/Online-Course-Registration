from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AdminLoginForm
from .models import AdminLoginModel
from django.contrib import messages


def admin_login(request):
    '''The FBV returns a HttpResponse with AdminLoginForm'''
    return render(request,template_name="myadmin/admin_login.html",context={'AdminLoginForm':AdminLoginForm()})


def admin_login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        obj = AdminLoginModel.objects.get(username=username,password=password)
        request.session['status'] = obj.mobile
        return redirect('myadmin:login_success')
    except AdminLoginModel.DoesNotExist:
        messages.error(request,"Invalid Credentials")
        return redirect('myadmin:admin_login')


def admin_login_success(request):
    return render(request,"myadmin/login_success.html")