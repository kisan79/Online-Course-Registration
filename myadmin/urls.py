from django.urls import path
from myadmin import views

app_name = 'myadmin'
urlpatterns = [
    path('',views.admin_login,name="admin_login"),
    path('admin_login_check/',views.admin_login_check,name="admin_login_check"),
    path('login_success/',views.admin_login_success,name="login_success"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    # Admin Course Operations
    path('add_course/',views.add_course,name = "add_course"),
    path('save_course_type/',views.add_course,name = "save_course_type"),
    path('save_course/',views.save_course,name = "save_course"),

    # Admin Schedule Operations
    path('schedule_new_batches/',views.ScheduleNewBatch.as_view(),name = "schedule_new_batches"),
    path('view_scheduled_batches/',views.ViewScheduledBatches.as_view(),name = "view_scheduled_batches"),
    path('update_batch/<int:pk>',views.UpdateSchedule.as_view(),name = "update_batch"),
    path('delete_batch/<int:pk>',views.delete_batch,name ="delete_batch"),

    # Admin Faculty operation
    path('faculty/',views.FacultyOperation.as_view(),name ="faculty"),
]