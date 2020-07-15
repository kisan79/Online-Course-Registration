from django.shortcuts import render,redirect
from django.views.generic.base import View
from .forms import *
from  .models import *
from django.contrib import messages

# Create your views here.


class Register(View):
    """ Performs Student Adding And Saving Operation"""
    def get(self,request):
        """Showing Student Registration Form"""
        context = {
            "StudentRegister":StudentRegister()
        }
        return render(request,"student/register.html",context=context)

    def post(self,request):
        """Saving Student Details"""
        sr = StudentRegister(request.POST,request.FILES)
        if sr.is_valid():
            sr.save()
            messages.success(request,"Registered Successfully")
            return redirect('student:register')
        else:
            return render(request,"student/register.html",context={"StudentRegister":sr})


class Login(View):
    """ Performs Student Login and Session Creation """

    def get(self, request):
        """Showing Student Login Form"""
        context = {
            "StudentLoginForm": StudentLoginForm()
        }
        return render(request, "student/login.html", context=context)

    def post(self, request):
        """Performs Session Creation on Successful Login"""
        username = request.POST['username']
        password = request.POST['password']
        try:
            obj = Student.objects.get(username=username, password=password)
            request.session['status'] = obj.email
            return redirect('student:login_success')
        except Student.DoesNotExist:
            messages.error(request, "Invalid Credentials")
            return redirect('student:login')


def login_success(request):
    try:
        obj = Student.objects.get(email= request.session['status'])
        return render(request,"student/login_success.html",context={"student_data":obj})
    except KeyError:
        return redirect('student:login')


def student_logout(request):
    del request.session['status']
    return redirect('student:login')