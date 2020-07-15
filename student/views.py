from django.shortcuts import render,redirect
from django.views.generic.base import View
from .forms import *
from  .models import *
from myadmin.models import ScheduleBatch
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

# New Batch Enrolement


def view_new_batches(request):
    try:
        context = {
            "ScheduleBatch":ScheduleBatch.objects.all(),
            "student_data":Student.objects.get(email= request.session['status'])
         }
        return render(request,"student/view_new_batches.html",context=context)
    except KeyError:
        return redirect('student:login_success')


def enroll_student(request,batch_id,mobile):
    BatchEnrollement(batch_id=batch_id,mobile=mobile).save()
    messages.success(request,"Entrolled Successfully")
    return redirect('student:view_new_batches')


def enrolled_batches(request):
    context = {
        "BatchEnrollement": [
            [batch.batch_id,s.course_name,s.faculty_name,s.start_date,s.time,s.duration,s.batch_type,s.fee]
            for batch in BatchEnrollement.objects.all() for s in ScheduleBatch.objects.all() if batch.batch_id == s.idno
        ],
        "BE":BatchEnrollement.objects.all()
    }
    print(context["BatchEnrollement"])

    return render(request,"student/enrolled_batches.html",context=context)


def cancel_registration(request,batch_id):
    BatchEnrollement.objects.get(id=batch_id).delete()
    messages.success(request,"Registration Cancelled Successfully")
    return redirect('student:enrolled_batches')