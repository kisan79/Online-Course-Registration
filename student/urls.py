from django.urls import path
from student import views

app_name = 'student'
urlpatterns = [
    # Student Register
    path('register/',views.Register.as_view(),name = "register"),
]