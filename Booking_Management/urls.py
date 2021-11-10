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
    path('block_master/<str:project_name>', views.block_master, name='block_master'),
    
    re_path('flat_master/$', views.flat_master, name='flat_master'),
    path('flat_master/<str:project_name>/<str:block_name>/<str:floor_no>', views.flat_master, name='flat_master'),

    re_path('customer_master/$', views.customer_master, name='customer_master'),
    path('customer_master/<str:customer_name>', views.customer_master, name='customer_master'),

    re_path('bank_master/$', views.bank_master, name='bank_master'),
    path('bank_master/<str:bank_name>', views.bank_master, name='bank_master'),

    re_path('broker_master/$', views.broker_master, name='broker_master'),
    path('broker_master/<str:broker_name>', views.broker_master, name='broker_master'),
    
    #transaction
    re_path('booking_entry/$', views.booking_entry, name='booking_entry'),
    path('booking_entry/<str:reference_id>', views.booking_entry, name='booking_entry'),
    
    re_path('customer_request/$', views.customer_request, name='customer_request'),
    path('customer_request/<str:reference_id>', views.customer_request, name='customer_request'),
    
    #reports
    path('flat_booking_status', views.flat_booking_status, name='flat_booking_status'),
    
    #settings
    path('settings', views.settings, name='settings'),
    re_path('organisation_master/$', views.organisation_master, name='organisation_master'),
    path('organisation_master/<str:organisation_name>', views.organisation_master, name='organisation_master'),
    re_path('user_master/$', views.user_master, name='user_master'),
    path('user_master/<str:username>', views.user_master, name='user_master'),

    #load data
    re_path('load-blocks/$', views.load_blocks, name='load_blocks'),
    path('load-blocks/<str:project_name>', views.load_blocks, name='load_blocks'),

    re_path('load-floors/$', views.load_floors, name='load_floors'),
    path('load-floors/<str:project_name>/<str:block_name>', views.load_floors, name='load_floors'),

    re_path('load-flats/$', views.load_flats, name='load_flats'),
    path('load-flats/<str:project_name>/<str:block_name>/<str:floor_no>/<str:share_type>/<str:save_update>', views.load_flats, name='load_flats'),
    path('show_flats/<str:project_name>/<str:block_name>', views.show_flats, name='show_flats'),

    re_path('flat_details/$', views.flat_details, name='flat_details'),
    path('flat_details/<str:project_name>/<str:block_name>/<str:floor_no>/<str:flat_no>', views.flat_details, name='flat_details'),

    re_path('customer_details/$', views.customer_details, name='customer_details'),
    path('customer_details/<str:customer_name>', views.customer_details, name='customer_details'),
    
    re_path('get_no_flats/$', views.get_no_flats, name='get_no_flats'),
    path('get_no_flats/<str:project_name>/<str:block_name>/<str:floor_no>', views.get_no_flats, name='get_no_flats'),

    #ajax
    path('ifexists/<str:db_name>/<str:collection_name>/<str:dt>', views.ifExists, name='ifexists'),
    path('get_project_status/<str:project_name>', views.get_project_status, name='get_project_status'),
    path('get_customer_details/<str:project_name>/<str:block_name>/<str:floor_no>/<str:flat_no>/<str:collection_name>', views.get_customer_details, name='get_customer_details'),
    path('if_phno_exist/<str:ph_no>', views.if_phno_exist, name='if_phno_exist'),

    #file ops
    path('view_file/<str:db_name>/<str:docname>/<str:file_name>', views.view_file, name='view_file'),
    path('remove_file/<str:file_name>/<str:docname>', views.remove_file, name='remove_file')
]
