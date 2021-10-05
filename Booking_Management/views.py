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

def ifExists(request, db_name, collection_name, dt):
    response =  {
        "result": False
    }

    dt = json.loads(dt)
    if db.ifExistsDoc(db_name, collection_name, dt):
        response =  {
           "result": True
        } 

    return JsonResponse(response)

def view_file(request, db_name, file_name):
    db.ViewFile(db_name, file_name)
    return JsonResponse({})

def load_blocks(request, project_name=None):
    project_name = request.GET.get('project_name')
    blocks = db.getBlocksListByProject(project_name)
    return render(request, 'master/dropdown/load_blocks.html', {'blocks': blocks})

def load_floors(request, project_name=None, block_name=None):
    project_name = request.GET.get('project_name')
    block_name = request.GET.get('block_name')
    floors = db.getFloorsListByBlock(project_name, block_name)
    return render(request, 'master/dropdown/load_floors.html', {'floors': floors})

#master
def project_master(request, project_name=None):
    projectDetails = db.getDetails("Master", "Project")
    banks_list =  db.getBanksList()

    if request.is_ajax():
        if project_name != None:
            selectedProjectDetails = db.getProjectByName(project_name)
            files = db.GetFilesByMetaData("Master", selectedProjectDetails["_id"])
            response =  {
                "selectedProjectDetails": selectedProjectDetails,
                "files": json.loads(json_util.dumps(files))
            }
            return JsonResponse(response)

    if request.method == 'POST':        
        _id = request.POST.get("_id")
        [doc, files] = utils.getProjectData(_id, 
        request=request)

        if 'Save' in request.POST:
            db.InsertData("Master", "Project", doc, files)
        elif 'Update' in request.POST:
            db.UpdateData("Master", "Project", doc, files) 
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'master/project.html', 
    {        
        "projectDetails":projectDetails,
        "banks_list": banks_list
    })
    
def block_master(request, project_name=None):
    blockDetails = db.getDetails("Master", "Block")
    projects_list =  db.getProjectsList()

    if request.is_ajax():
        selectedBlockDetails = db.getBlockDetailsByProject(project_name)
        files = db.GetFilesByMetaData("Master", selectedBlockDetails["_id"])
        response =  {
            "selectedBlockDetails": selectedBlockDetails,
            "files": json.loads(json_util.dumps(files))
        }
        return JsonResponse(response)

    if request.method == 'POST':        
        _id = request.POST.get("_id")
        [doc, files] = utils.getBlockData(_id, 
        request=request)

        if 'Save' in request.POST:
            db.InsertData("Master", "Block", doc, files)
        elif 'Update' in request.POST:
            db.UpdateData("Master", "Block", doc, files) 
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'master/block.html', 
    {        
        "blockDetails":blockDetails,
        "projects_list": projects_list
    })

def flat_master(request, project_name=None, block_name=None, floor_no=None):
    flatDetails = db.getDetails("Master", "Flat")
    projects_list =  db.getProjectsList("Master", "Block")

    if request.is_ajax():
        selectedFlatDetails = db.getFlatDetailsByFloor(project_name, block_name, floor_no)
        files = db.GetFilesByMetaData("Master", selectedFlatDetails["_id"])
        response =  {
            "selectedFlatDetails": selectedFlatDetails,
            "files": json.loads(json_util.dumps(files))
        }
        return JsonResponse(response)

    if request.method == 'POST':        
        _id = request.POST.get("_id")
        [doc, files] = utils.getFlatData(_id, 
        request=request)

        if 'Save' in request.POST:
            db.InsertData("Master", "Flat", doc, files)
        elif 'Update' in request.POST:
            db.UpdateData("Master", "Flat", doc, files) 
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'master/flat.html', 
    {        
        "flatDetails": flatDetails,
        "projects_list": projects_list
    })

def customer_master(request, customer_name=None):
    customerDetails = db.getDetails("Master", "Customer")
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
    
    if request.method == "POST":
        _id = request.POST.get("_id")
        [doc, files] = utils.getCustomerData(_id, 
        request=request)
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
    bankDetails = db.getDetails("Master", "Bank")
    
    if request.is_ajax():
        selectedBankDetails = db.getCustomerByName(bank_name)
        files = db.GetFilesByMetaData("Master", selectedBankDetails["_id"])
        response =  {
            "selectedBankDetails": selectedBankDetails,
            "files": json.loads(json_util.dumps(files))
        }
        return JsonResponse(response)
    
    if request.method == "POST":
        _id = request.POST.get("_id")
        [doc, files] = utils.getBankData(_id, 
        request=request)
        if 'Save' in request.POST:
            db.InsertData("Master", "Bank", doc, files)
        elif 'Update' in request.POST:
            db.UpdateData("Master", "Bank", doc, files) 
        return HttpResponseRedirect(request.path_info)
        
    return render(request, 'master/bank.html', 
    {
        "bankDetails":bankDetails
    })

#transaction
def booking_entry(request, reference_id=None):
    entries = db.getDetails("Transaction", "BookingEntry")
    
    if request.is_ajax():
        selectedBookingEntry = db.getBookingEntryByReferenceId(reference_id)
        files = db.GetFilesByMetaData("Transaction", selectedBookingEntry["_id"])
        response =  {
            "selectedBookingEntry": selectedBookingEntry,
            "files": json.loads(json_util.dumps(files))
        }
        return JsonResponse(response)
    
    if request.method == "POST":
        _id = request.POST.get("_id")
        [doc, files] = utils.getBookingEntries(_id, 
        request=request)
        if 'Save' in request.POST:
            db.InsertData("Transaction", "Booking Entry", doc, files)
        elif 'Update' in request.POST:
            db.UpdateData("Transaction", "Booking Entry", doc, files) 
        return HttpResponseRedirect(request.path_info)
        
    return render(request, 'transaction/booking_entry.html', 
    {
        "entries":entries
    })

def customer_request(request, reference_id=None):    
    return render(request, 'transaction/customer_request.html')

#report
def flat_booking_status(request):
    return render(request, 'report/flat_booking_status.html')

#settings
def settings(request):
    return render(request, "settings/index.html")

def organisation_master(request, org_name=None):
    organisationDetails = db.getDetails("Master", "Organisation")

    if request.is_ajax():
        selectedOrganisationDetails = db.getOrganisationByName(org_name)
        files = db.GetFilesByMetaData("Settings", selectedOrganisationDetails["_id"])
        response =  {
            "selectedOrganisationDetails": selectedOrganisationDetails,
            "files": json.loads(json_util.dumps(files))
        }
        return JsonResponse(response)

    if request.method == 'POST':        
        _id = request.POST.get("_id")
        [doc, files] = utils.getOrganisationData(_id, 
        request=request)

        if 'Save' in request.POST:
            db.InsertData("Settings", "Organisation Master", doc, files)
        elif 'Update' in request.POST:
            db.UpdateData("Settings", "Organisation Master", doc, files) 
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'settings/organisation_master.html', 
    {        
        "organisationDetails":organisationDetails
    })

def user_master(request):
    userDetails = db.getDetails("Master", "User")
    if request.method == "POST":
        doc  = utils.getUserData(request)
        db.InsertData("Settings", "UserMaster", doc) 
        return HttpResponseRedirect(request.path_info)
    return render(request, 'settings/user_master.html', {"userDetails":userDetails})