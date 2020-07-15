from django.urls import path
from student import views

app_name = 'student'
urlpatterns = [
    # Student Register
    path('register/',views.Register.as_view(),name = "register"),
    path('login/',views.Login.as_view(),name = "login"),
    path('login_success/',views.login_success,name = "login_success"),
    path('logout/',views.student_logout,name = "logout"),

    # New Batch Enrolement

    path('view_new_batches/',views.view_new_batches,name = "view_new_batches")
]