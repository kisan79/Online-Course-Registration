from django.shortcuts import render,redirect
from django.views.generic.base import View
from .forms import StudentRegister
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