from django.urls import path

from myadmin import views

app_name='myadmin'
urlpatterns = [
    path('',views.admin_login,name="admin_login"),
    path('admin_login_check/',views.admin_login_check,name="admin_login_check"),
    path('login_success/',views.admin_login_success,name="login_success"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    #Admin Course Operations
    path('add_course/',views.add_course,name = "add_course"),
    path('save_course_type/',views.add_course,name = "save_course_type"),
]