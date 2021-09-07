import re
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from . import db

def home(request):    
    return render(request, 'index.html')

def login(request):
    error_msg = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if db.verifyUser(username, password):        
            return render(request, 'organisation_login.html')
        else:
            error_msg = "Invalid username and password"
    return render(request, 'login.html', {"error_msg": error_msg})

def organisation_login(request):
    if request.method == "POST":
        organisation = request.POST.get('orhanisation')
        branch = request.POST.get('branch')
        fin_year = request.POST.get('fin_year')
        return render(request, 'index.html', {"organisation": organisation})
    return render(request, 'organisation_login.html')

#settings
def settings(request):
    return render(request, "settings/index.html")

def user_master(request):
    userDetails = db.getUsers()
    if request.method == "POST":
        doc = {}
        doc["username"] = request.POST.get("username")
        doc["password"] = request.POST.get("password")
        doc["user_type"] = request.POST.get("user_type")
        doc["full_name"] = request.POST.get("ful_name")
        doc["designation"] = request.POST.get("designation")
        db.InsertData("Settings", "UserMaster", doc) 
        return HttpResponseRedirect(request.path_info)
    return render(request, 'settings/user_master.html', {"userDetails":userDetails})

def project_master(request):
    return render(request, 'master/project.html')

def block_master(request):
    return render(request, 'master/block.html')

def flat_master(request):
    return render(request, 'master/flat.html')

def customer_master(request):
    customerDetails = db.getCustomers()
    return render(request, 'master/customer.html', {"customerDetails":customerDetails})

def modify_customer(request, customer_name):
    customer_name = "KOUSHAL KISHORE AGRAWALLA"
    customerDetails = db.getCustomers()
    selectedCustomerDetails = db.getCustomerByName(customer_name)
    return render(request, 'master/customer.html', 
    {
        "customerDetails":customerDetails,
        "selectedCustomerDetails": selectedCustomerDetails
    })

def bank_master(request):
    return render(request, 'master/bank.html')

def booking_entry(request):
    return render(request, 'transaction/booking_entry.html')

def customer_request(request):    
    return render(request, 'transaction/customer_request.html')

def flat_booking_status(request):
    return render(request, 'report/flat_booking_status.html')