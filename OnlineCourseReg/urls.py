"""OnlineCourseReg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myadmin import urls as admin_url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from student import urls as student_url

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('myadmin/',include(admin_url)) ,
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('student/',include(student_url)),
]

# static function will return a URL pattern for serving files in debug mode


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)