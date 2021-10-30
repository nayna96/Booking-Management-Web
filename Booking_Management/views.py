from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from . import db, utils
import json
from bson import json_util

toRemoveFiles = []

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

#AJAX CALLS
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

def get_project_status(request, project_name):
    project_status = db.getProjectStatus(project_name)
    response =  {
        "project_status": project_status
    } 

    return JsonResponse(response)

def load_blocks(request, project_name=None):
    project_name = request.GET.get('project_name')
    blocks = db.getBlocksListByProject(project_name)
    response = {'blocks': blocks}
    return JsonResponse(response)

def load_floors(request, project_name=None, block_name=None):
    project_name = request.GET.get('project_name')
    block_name = request.GET.get('block_name')
    floors = db.getFloorsListByBlock(project_name, block_name)
    response = {'floors': floors}
    return JsonResponse(response)

def load_flats(request, project_name=None, block_name=None, floor_no=None, share_type=None, save_update=None):
    project_name = request.GET.get('project_name')
    block_name = request.GET.get('block_name')
    floor_no = request.GET.get('floor_no')
    share_type = request.GET.get('share_type')
    save_update = request.GET.get('save_update')

    if len(project_name) > 0 and len(block_name) > 0 and len(floor_no) > 0:
        flats = db.getFlatsListByFloorNo(project_name, block_name, floor_no, share_type, save_update)
    else:
        flats = []

    response = {'flats': flats}
    return JsonResponse(response)

def flat_details(request, project_name=None, block_name=None, floor_no=None, flat_no=None):
    project_name = request.GET.get('project_name')
    block_name = request.GET.get('block_name')
    floor_no = request.GET.get('floor_no')
    flat_no = request.GET.get('flat_no')

    response =  {}
    if len(project_name) > 0 and len(block_name) > 0 and len(floor_no) > 0 and len(flat_no) > 0:
        flatDetails = db.getFlatDetailsByFlatNo(project_name, block_name, floor_no, flat_no)
        response =  {
            "flatDetails": flatDetails
        } 

    return JsonResponse(response)

def customer_details(request, customer_name=None):
    customer_name = request.GET.get('customer_name')

    customerDetails = db.getCustomerDetailsByName(customer_name)
    response =  {
        "customerDetails": customerDetails
    } 

    return JsonResponse(response)

def get_no_flats(request, project_name=None, block_name=None, floor_no=None):
    no_flats = db.getNoFlatsByFloor(project_name, block_name, floor_no)
    response = {
        "no_flats": no_flats
    }
    return JsonResponse(response)

#master
def project_master(request, project_name=None):
    projectDetails = db.getDetails("Master", "Project")
    banks_list =  db.getBanksList()

    if request.is_ajax():
        if project_name != None:
            selectedProjectDetails = db.getProjectByName(project_name)
            
            metadata_filters = [
                {"metadata._id" : selectedProjectDetails["_id"]}
            ]
            files = db.GetFiles("Master", metadata_filters)
            
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
            global toRemoveFiles
            for toRemoveFile in toRemoveFiles:                
                dt = [
                    { "filename": toRemoveFile["file_name"] },
                    { "metadata._id" : doc["_id"] },
                    { "metadata.doc_name": toRemoveFile["docname"] }
                ]
                db.RemoveFile("Master", dt)
                toRemoveFiles = []

        project_name = doc["project_name"]
        approved_banks = doc["approved_banks"]
        approved_banks_lst = [bank['bank_name'] for bank in approved_banks]
        db.updateBankDetails(approved_banks_lst, project_name)

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
        response = {}
        if project_name != None:
            selectedBlockDetails = db.getBlockDetailsByProject(project_name)
            response =  {
                "selectedBlockDetails": selectedBlockDetails
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
        response = {}
        if project_name!= None and block_name != None and floor_no != None:
            selectedFlatDetails = db.getFlatDetailsByFloor(project_name, block_name, floor_no)
            response =  {
                "selectedFlatDetails": selectedFlatDetails
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
        selectedCustomerDetails = db.getCustomerDetailsByName(customer_name)

        metadata_filters = [
                {"metadata._id" : selectedCustomerDetails["_id"]}
            ]
        files = db.GetFiles("Master", metadata_filters)

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
            
            global toRemoveFiles
            for toRemoveFile in toRemoveFiles:                
                dt = [
                    { "filename": toRemoveFile["file_name"] },
                    { "metadata._id" : doc["_id"] },
                    { "metadata.doc_name": toRemoveFile["docname"] }
                ]
                db.RemoveFile("Master", dt)
                toRemoveFiles = [] 

        return HttpResponseRedirect(request.path_info)
        
    return render(request, 'master/customer.html', 
    {
        "customerDetails":customerDetails,
        "occupations_list": occupations_list,
        "castes_list": castes_list
    })

def if_phno_exist(request, ph_no=None):
    ph_exists = db.ifPhNoExists(ph_no)
    response =  {
            "ph_exists": ph_exists
        }
    return JsonResponse(response)

def bank_master(request, bank_name=None):
    bankDetails = db.getDetails("Master", "Bank")
    
    if request.is_ajax():
        selectedBankDetails = db.getBankDetailsByName(bank_name)

        metadata_filters = [
                {"metadata._id" : selectedBankDetails["_id"]}
            ]
        files = db.GetFiles("Master", metadata_filters)

        response =  {
            "selectedBankDetails": selectedBankDetails,
            "files": json.loads(json_util.dumps(files))
        }
        return JsonResponse(response)
    
    if request.method == "POST":
        _id = request.POST.get("_id")
        approved_projects = request.POST.get("approved_projects")
        [doc, files] = utils.getBankData(_id, approved_projects,
        request=request)
        if 'Save' in request.POST:
            db.InsertData("Master", "Bank", doc, files)
        elif 'Update' in request.POST:
            db.UpdateData("Master", "Bank", doc, files)

            global toRemoveFiles
            for toRemoveFile in toRemoveFiles:                
                dt = [
                    { "filename": toRemoveFile["file_name"] },
                    { "metadata._id" : doc["_id"] },
                    { "metadata.doc_name": toRemoveFile["docname"] }
                ]
                db.RemoveFile("Master", dt)
                toRemoveFiles = []

        return HttpResponseRedirect(request.path_info)
        
    return render(request, 'master/bank.html', 
    {
        "bankDetails":bankDetails
    })

def broker_master(request, broker_name=None):
    brokerDetails = db.getDetails("Master", "Broker")
    
    if request.is_ajax():
        selectedBrokerDetails = db.getBrokerDetailsByName(broker_name)

        metadata_filters = [
                {"metadata._id" : selectedBrokerDetails["_id"]}
            ]
        files = db.GetFiles("Master", metadata_filters)

        response =  {
            "selectedBankDetails": selectedBrokerDetails,
            "files": json.loads(json_util.dumps(files))
        }
        return JsonResponse(response)
    
    if request.method == "POST":
        _id = request.POST.get("_id")
        [doc, files] = utils.getBrokerData(_id, request=request)
        if 'Save' in request.POST:
            db.InsertData("Master", "Broker", doc, files)
        elif 'Update' in request.POST:
            db.UpdateData("Master", "Broker", doc, files)

            global toRemoveFiles
            for toRemoveFile in toRemoveFiles:                
                dt = [
                    { "filename": toRemoveFile["file_name"] },
                    { "metadata._id" : doc["_id"] },
                    { "metadata.doc_name": toRemoveFile["docname"] }
                ]
                db.RemoveFile("Master", dt)
                toRemoveFiles = []

        return HttpResponseRedirect(request.path_info)
        
    return render(request, 'master/broker.html', 
    {
        "brokerDetails":brokerDetails
    })

#transaction
def booking_entry(request, reference_id=None):
    if reference_id == None:
        reference_id = db.getNextId("Transaction", "BookingEntry")

    entries = db.getDetails("Transaction", "BookingEntry")
    projects_list =  db.getProjectsList("Master", "Flat")
    customers_list = db.getCustomersList()
    banks_list = db.getBanks()
    brokers_list = db.getBrokersList()
    
    if request.is_ajax():
        if reference_id != None:
            selectedBookingEntry = db.getBookingEntryByReferenceId(reference_id)
            response =  {
                "selectedBookingEntry": selectedBookingEntry
            }
            return JsonResponse(response)
    
    if request.method == "POST":
        _id = request.POST.get("_id")
        [doc, files] = utils.getBookingEntry(_id, 
        request=request)
        if 'Save' in request.POST:
            db.InsertData("Transaction", "BookingEntry", doc, files)
        elif 'Update' in request.POST:
            db.UpdateData("Transaction", "BookingEntry", doc, files)

        db.updateFlatStatus(doc["project_name"], doc["block_name"], doc["floor_no"], doc["flat_no"], "BOOKED")

        return HttpResponseRedirect(request.path_info)

    return render(request, 'transaction/booking_entry.html', 
    {
        "reference_id": reference_id,
        "entries":entries,
        "projects_list": projects_list,
        "customers_list": customers_list,
        "banks_list": banks_list,
        "brokers_list": brokers_list
    })

def customer_request(request, reference_id=None):    
    return render(request, 'transaction/customer_request.html')

#report
def flat_booking_status(request):
    projects_list =  db.getProjectsList()
    return render(request, 'report/flat_booking_status.html', 
    {
        "projects_list": projects_list
    })

def show_flats(request, project_name=None, block_name=None):
    flats_list = {}
    
    floors_list = db.getFloorsListByBlock(project_name, block_name)    
    for floor in floors_list:
        details = db.getFlatDetailsByFloor(project_name, block_name, floor)
        if len(details) != 0:
            flats = details["flats"]
            flats_list[floor] = flats

    response =  {
            "flats_list": flats_list
        }
    return JsonResponse(response)

def get_customer_details(request, project_name=None, block_name=None, floor_no=None, 
    flat_no=None, collection_name=None):
    customer_details = db.getCustomerDetailsByFlatNo(project_name, block_name, floor_no, 
        flat_no, collection_name)
    response =  {
            "customer_details": customer_details
        }
    return JsonResponse(response)

#settings
def settings(request):
    return render(request, "settings/index.html")

def organisation_master(request, org_name=None):
    organisationDetails = db.getDetails("Master", "Organisation")

    if request.is_ajax():
        selectedOrganisationDetails = db.getOrganisationByName(org_name)

        metadata_filters = [
                {"metadata._id" : selectedOrganisationDetails["_id"]}
            ]
        files = db.GetFiles("Settings", metadata_filters)

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
            
            global toRemoveFiles
            for toRemoveFile in toRemoveFiles:                
                dt = [
                    { "filename": toRemoveFile["file_name"] },
                    { "metadata._id" : doc["_id"] },
                    { "metadata.doc_name": toRemoveFile["docname"] }
                ]
                db.RemoveFile("Settings", dt)
                toRemoveFiles = [] 

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

#FILE OPS
def view_file(request, db_name, docname, file_name):
    dt = [
        { "filename": file_name },
        { "metadata.doc_name": docname }
    ]
    db.ViewFile(db_name, dt)
    return JsonResponse({})

def remove_file(request, file_name, docname):    
    toRemoveFiles.append({ 
        "file_name": file_name,
        "docname": docname 
        })    
    return JsonResponse({})