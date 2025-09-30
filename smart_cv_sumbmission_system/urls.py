"""smart_cv_sumbmission_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from system.views import job_applicaion
from system.views import view_job
from system.views import add_job
from system.views import view_result
from system.views import pdf_view
from system.views import log_out
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (
handler404
)

handler404 = 'system.views.bad_request'

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/logout/', log_out),
    path('admin/', admin.site.urls),
    path('apply/', job_applicaion, name='job_applicaion'),
    path('jobs/', view_job, name='view_job'),
    path('', view_job, name='view_job'),
    path('addjob/', add_job, name='add_job'),
    path('result/', view_result, name='view_result'),
    path('showres/<path:p>/', pdf_view, name='pdf_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
