"""Booking_Management URL Configuration

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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('login', views.organisation_login, name='org_login'),
    path('home', views.home, name='home'),

    #master
    re_path('project_master/$', views.project_master, name='project_master'),
    path('project_master/<str:project_name>', views.project_master, name='project_master'),

    re_path('block_master/$', views.block_master, name='block_master'), 
    path('block_master/<str:block_name>', views.block_master, name='block_master'),
    
    re_path('flat_master/$', views.flat_master, name='flat_master'),
    path('flat_master/<str:flat_name>', views.flat_master, name='flat_master'),

    re_path('customer_master/$', views.customer_master, name='customer_master'),
    path('customer_master/<str:customer_name>', views.customer_master, name='customer_master'),

    re_path('bank_master/$', views.bank_master, name='bank_master'),
    path('bank_master/<str:bank_name>', views.bank_master, name='bank_master'),
    
    #transaction
    re_path('booking_entry/$', views.booking_entry, name='booking_entry'),
    path('booking_entry/<str:reference_id>', views.booking_entry, name='booking_entry'),
    
    re_path('customer_request/$', views.customer_request, name='customer_request'),
    path('customer_request/<str:reference_id>', views.customer_request, name='customer_request'),
    
    #reports
    path('flat_booking_status', views.flat_booking_status, name='flat_booking_status'),
    
    #settings
    path('settings', views.settings, name='settings'),
    path('organisation_master', views.organisation_master, name='organisation_master'),
    path('user_master', views.user_master, name='user_master'),
    
    #download file
    path('view/<str:dbName>/<str:fileName>', views.view_file, name='view_file')
]
