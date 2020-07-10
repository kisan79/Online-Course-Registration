from django.urls import path

from myadmin import views

# app_name='admin'
urlpatterns = [
    path('',views.admin_login,name="admin_login"),
]