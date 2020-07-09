from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def admin_login(request):
    return HttpResponse('Admin Login page')