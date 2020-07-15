from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import UpdateView

from .forms import *
from .models import AdminLoginModel,CourseType,Course
from django.contrib import messages
from django.views.generic.base import View
from faculty.forms import *
from django.urls import reverse_lazy


def admin_login(request):
    '''The FBV returns a HttpResponse with AdminLoginForm'''
    return render(request,template_name="myadmin/admin_login.html",context={'AdminLoginForm':AdminLoginForm()})

# Admin Login Check


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

# Admin Login Success


def admin_login_success(request):

    try:
        obj = AdminLoginModel.objects.get(mobile= request.session['status'])
        return render(request,"myadmin/login_success.html",context={"admin_data":obj})
    except KeyError:
        return render(request,"myadmin/login_success.html")

# Admin Logout


def admin_logout(request):
    del request.session['status']
    return redirect('myadmin:admin_login')


def add_course(request):
    if request.method == "POST":
        ctype = CourseTypeForm(request.POST,request.FILES)
        if ctype.is_valid():
            ctype.save()
            messages.success(request,"Course Type Successfully Saved")
            return redirect('myadmin:add_course')
        else:
            return render(request,"myadmin/add_course.html",context={"CourseTypeForm":ctype})
    else:
        try:
            obj = AdminLoginModel.objects.get(mobile=request.session['status'])
            # If There is Session
            context = {
                "admin_data": obj,
                "CourseTypeForm": CourseTypeForm(),
                "CourseForm": CourseForm(),
            }
            return render(request, "myadmin/add_course.html", context=context)

        # If No Session
        except KeyError:

            return render(request, "myadmin/add_course.html")


def save_course(request):
    if request.method == "POST":
        cf = CourseForm(request.POST,request.FILES)
        if cf.is_valid():
            cf.save()
            messages.success(request, "Course Successfully Saved")
            return redirect('myadmin:add_course')
        else:
            return render(request,"myadmin/add_course.html",context={'CourseForm':cf})


# Schedule New Batch


class ScheduleNewBatch(View):
    def get(self,request):
        context = {
            "ScheduleBatchForm": ScheduleBatchForm()
        }
        return render(request, "myadmin/schedule_new_batches.html", context=context)
    def post(self,request):
        sbf = ScheduleBatchForm(request.POST)
        if sbf.is_valid():
            sbf.save()
            messages.success(request,"New Batch Scheduled")
            return redirect('myadmin:schedule_new_batches')
        else:
            return render(request,"myadmin/schedule_new_batches.html",context={"ScheduleBatchForm":sbf})

class ViewScheduledBatches(View):
    def get(self,request):
        context = {
            "view":ScheduleBatch.objects.all()
        }
        return render(request,"myadmin/view_scheduled_batches.html",context=context)

class UpdateSchedule(UpdateView):
    template_name = "myadmin/update_batch.html"
    model = ScheduleBatch
    form_class = ScheduleBatchForm
    success_url = reverse_lazy("myadmin:view_scheduled_batches")

def delete_batch(request,pk):
    ScheduleBatch.objects.get(idno=pk).delete()
    messages.success(request,"Batch Deleted Successfully")
    return redirect('myadmin:view_scheduled_batches')


# Faculty Operation


class FacultyOperation(View):


    def get(self,request):
        context = {
            "FacultyForm":FacultyForm()
        }
        return render(request,"myadmin/faculty.html",context=context)


    def post(self,request):
        """Save Faculty Operation"""
        ff = FacultyForm(request.POST,request.FILES)
        if ff.is_valid():
            ff.save()
            messages.success(request,"Faculty Saved Successfully")
            return redirect("myadmin:faculty")
        else:
            context = {
                "FacultyForm": ff,
            }
            return render(request,"myadmin/faculty.html",context=context)
