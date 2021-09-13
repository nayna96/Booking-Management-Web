from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from . import db, utils
import json
from bson import json_util

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
        doc  = utils.getUserData(request)
        db.InsertData("Settings", "UserMaster", doc) 
        return HttpResponseRedirect(request.path_info)
    return render(request, 'settings/user_master.html', {"userDetails":userDetails})

def project_master(request, project_name=None):
    projectDetails = db.getProjects()
    if request.is_ajax():
        selectedProjectDetails = db.getProjectByName(project_name)
        files = db.GetFilesByMetaData("Master", selectedProjectDetails["_id"])
        response =  {
            "selectedProjectDetails": selectedProjectDetails,
            "files": json.loads(json_util.dumps(files))
        }
        return JsonResponse(response)
    elif request.method == "POST":
        _id = request.POST.get("_id")
        [doc, files] = utils.getprojectData(request, _id)
        if 'Save' in request.POST:
            db.InsertData("Master", "Project", doc, files)
        elif 'Update' in request.POST:
            db.UpdateData("Master", "Project", doc, files) 
        return HttpResponseRedirect(request.path_info)
    return render(request, 'master/project.html', 
    {
        "projectDetails":projectDetails
    })
    
def block_master(request, block_name=None):
    return render(request, 'master/block.html')

def flat_master(request, flat_name=None):
    return render(request, 'master/flat.html')

def customer_master(request, customer_name=None):
    customerDetails = db.getCustomers()
    occupations_list = db.getOccupations()
    castes_list = db.getCastes()
    if request.is_ajax():
        selectedCustomerDetails = db.getCustomerByName(customer_name)
        files = db.GetFilesByMetaData("Master", selectedCustomerDetails["_id"])
        response =  {
            "selectedCustomerDetails": selectedCustomerDetails,
            "files": json.loads(json_util.dumps(files))
        }
        return JsonResponse(response)
    elif request.method == "POST":
        _id = request.POST.get("_id")
        [doc, files] = utils.getCustomerData(request, _id)
        if 'Save' in request.POST:
            db.InsertData("Master", "Customer", doc, files)
        elif 'Update' in request.POST:
            db.UpdateData("Master", "Customer", doc, files) 
        return HttpResponseRedirect(request.path_info)
    return render(request, 'master/customer.html', 
    {
        "customerDetails":customerDetails,
        "occupations_list": occupations_list,
        "castes_list": castes_list
    })

def bank_master(request, bank_name=None):
    return render(request, 'master/bank.html')

def booking_entry(request, reference_id=None):
    return render(request, 'transaction/booking_entry.html')

def customer_request(request, reference_id=None):    
    return render(request, 'transaction/customer_request.html')

def flat_booking_status(request):
    return render(request, 'report/flat_booking_status.html')

def view_file(request, dbName, fileName):
    db.ViewFile(dbName, fileName)
    return JsonResponse({})