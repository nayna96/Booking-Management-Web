from . import db

#Master
def getProjectData(_id=None, **kwargs):
    id = db.getNextId("Master", "Project")
    doc = {}
    doc["_id"] = "P" + str(id) if len(_id) == 0 else _id
    doc["project_name"] = kwargs["request"].POST.get("project_name")                
    doc["addLine1"] = kwargs["request"].POST.get("addLine1")
    doc["addLine2"] = kwargs["request"].POST.get("addLine2")
    doc["district"] = kwargs["request"].POST.get("district")
    doc["city"] = kwargs["request"].POST.get("city")
    doc["state"] = kwargs["request"].POST.get("state")
    doc["pin"] = kwargs["request"].POST.get("pin")

    n = int(kwargs["request"].POST.get("fs1-fields"))
    approved_banks = []
    for i in range(n):
        bank_name = kwargs["request"].POST.get("fs1-" + str(i) + "-bank_name")
        if len(bank_name) > 0:
            b_id = db.getBankDetailsByName(short_bank_name=bank_name)["_id"]
            reference_dt = {
                "$ref": "Bank",
                "$id": b_id,
                "$db": "Master"
            }
            dt={
                "bank_name": reference_dt
            }
            approved_banks.append(dt)
    doc["approved_banks"] = approved_banks

    doc["project_status"] =  kwargs["request"].POST.get("project_status") 
    doc["sharing_pct"] =  kwargs["request"].POST.get("sharing_pct") 
    
    n = int(kwargs["request"].POST.get("fs2-fields"))
    landarea = []
    for i in range(n):
        dt = {
            "mouza": kwargs["request"].POST.get("fs2-" + str(i) + "-mouza"),
            "khata_no": kwargs["request"].POST.get("fs2-" + str(i) + "-khata_no"),
            "plot_no": kwargs["request"].POST.get("fs2-" + str(i) + "-plot_no"),
            "kisam": kwargs["request"].POST.get("fs2-" + str(i) + "-kisam"),
            "area": kwargs["request"].POST.get("fs2-" + str(i) + "-area"),
            "rent_receipt_fyr": kwargs["request"].POST.get("fs2-" + str(i) + "-rent_receipt_fyr")
        }
        landarea.append(dt)
    doc["landarea"] = landarea
    
    doc["devAuth_approval_no"] = kwargs["request"].POST.get("devAuth_approval_no")
    doc["devAuth_approval_fromdate"] = kwargs["request"].POST.get("devAuth_approval_fromdate")
    doc["devAuth_approval_todate"] = kwargs["request"].POST.get("devAuth_approval_todate")
    doc["renewal_devAuth_approval_no"] = kwargs["request"].POST.get("renewal_devAuth_approval_no")
    doc["renewal_devAuth_approval_fromdate"] = kwargs["request"].POST.get("renewal_devAuth_approval_fromdate")
    doc["renewal_devAuth_approval_todate"] = kwargs["request"].POST.get("renewal_devAuth_approval_todate")
    doc["rera_certificate_no"] = kwargs["request"].POST.get("rera_certificate_no")
    doc["rera_certificate_fromdate"] = kwargs["request"].POST.get("rera_certificate_fromdate")
    doc["rera_certificate_todate"] = kwargs["request"].POST.get("rera_certificate_todate")
    doc["renewal_rera_certificate_no"] = kwargs["request"].POST.get("renewal_rera_certificate_no")
    doc["renewal_rera_certificate_fromdate"] = kwargs["request"].POST.get("renewal_rera_certificate_fromdate")
    doc["renewal_rera_certificate_todate"] = kwargs["request"].POST.get("renewal_rera_certificate_todate")

    land_docs = kwargs["request"].FILES.getlist("land_docs")
    agreements_doc = kwargs["request"].FILES.getlist("agreements_doc")
    pow = kwargs["request"].FILES.getlist("pow")
    dev_auth_approval = kwargs["request"].FILES.getlist("dev_auth_approval")
    rera_certificate = kwargs["request"].FILES.getlist("rera_certificate")
    rent_receipt_doc = kwargs["request"].FILES.getlist("rent_receipt_doc")

    files = {
        "land_docs": land_docs,
        "agreements_doc": agreements_doc,
        "pow": pow,
        "dev_auth_approval": dev_auth_approval,
        "rera_certificate": rera_certificate,
        "rent_receipt_doc": rent_receipt_doc
    }

    return [doc, files]    

def getBlockData(_id=None, **kwargs):
    project_name = kwargs["request"].POST.get("project_name")
    p_id = db.getProjectDetailsByName(project_name)["_id"]

    doc = {}
    doc["_id"] = p_id + "B" if len(_id) == 0 else _id

    reference_dt = {
        "$ref": "Project",
        "$id": p_id,
        "$db": "Master"
    }
    doc["project_name"] = reference_dt
    doc["no_blocks"] = kwargs["request"].POST.get("no_blocks")

    n = int(kwargs["request"].POST.get("fs1-fields"))
    blocks = []
    for i in range(n):
        dt = {
            "block_name": kwargs["request"].POST.get("fs1-" + str(i) + "-block_name"),
            "no_floors": kwargs["request"].POST.get("fs1-" + str(i) + "-no_floors"),
            "floor_no": kwargs["request"].POST.get("fs1-" + str(i) + "-floor_no"),
            "no_flats": kwargs["request"].POST.get("fs1-" + str(i) + "-no_flats")
        }
        blocks.append(dt)
    doc["blocks"] = blocks

    files = {}

    return [doc, files]

def getFlatData(_id=None, **kwargs):
    project_name = kwargs["request"].POST.get("project_name")
    p_id = db.getProjectDetailsByName(project_name)["_id"]

    block_name = kwargs["request"].POST.get("block_name")
    floor_no = kwargs["request"].POST.get("floor_no")

    doc = {}
    doc["_id"] =  p_id + "B_" + block_name + "_" + floor_no + "F" if len(_id) == 0 else _id
    
    reference_dt = {
        "$ref": "Project",
        "$id": p_id,
        "$db": "Master"
    }
    doc["project_name"] = reference_dt

    doc["block_name"] = kwargs["request"].POST.get("block_name") 
    doc["floor_no"] = kwargs["request"].POST.get("floor_no") 

    '''reference_dt = {
        "$ref": "",
        "$id": p_id,
        "$db": "Master"
    }
    doc["block_name"] = reference_dt

    reference_dt = {
        "$ref": "",
        "$id": p_id,
        "$db": "Master"
    }
    doc["floor_no"] = reference_dt'''

    n = int(kwargs["request"].POST.get("fs1-fields"))
    flats = []
    for i in range(n):
        dt = {
            "flat_no": kwargs["request"].POST.get("fs1-" + str(i) + "-flat_no"),
            "flat_type": kwargs["request"].POST.get("fs1-" + str(i) + "-flat_type"),
            "ownership_status": kwargs["request"].POST.get("fs1-" + str(i) + "-ownership_status"),
            "flat_status": kwargs["request"].POST.get("fs1-" + str(i) + "-flat_status"),
            "carpet_area": kwargs["request"].POST.get("fs1-" + str(i) + "-carpet_area"),
            "builtup_area": kwargs["request"].POST.get("fs1-" + str(i) + "-builtup_area"),
            "superbuiltup_area": kwargs["request"].POST.get("fs1-" + str(i) + "-superbuiltup_area"),
            "parking_no": kwargs["request"].POST.get("fs1-" + str(i) + "-parking_no"),
            "parking_area": kwargs["request"].POST.get("fs1-" + str(i) + "-parking_area")
        }                            
        flats.append(dt)
    doc["flats"] = flats

    files = {}

    return [doc, files]

def getCustomerData(_id=None, **kwargs):
    id = db.getNextId("Master", "Customer")
    doc = {}
    doc["_id"] = "C" + str(id) if len(_id) == 0 else _id

    doc["customer_salutation"] = kwargs["request"].POST.get("customer_salutation")
    doc["customer_fname"] = kwargs["request"].POST.get("customer_fname").replace(" ", "")
    doc["customer_mname"] = kwargs["request"].POST.get("customer_mname").replace(" ", "")
    doc["customer_lname"] = kwargs["request"].POST.get("customer_lname").replace(" ", "")
    doc["customer_dob"] = kwargs["request"].POST.get("customer_dob")
    doc["customer_gender"] = kwargs["request"].POST.get("customer_gender")
    doc["customer_occupation"] = kwargs["request"].POST.get("customer_occupation")
    doc["customer_employer_company_name"] = kwargs["request"].POST.get("customer_employer_company_name")
    doc["customer_company_address"] = kwargs["request"].POST.get("customer_company_address")
    doc["customer_posted_at"] = kwargs["request"].POST.get("customer_posted_at")
    doc["customer_caste"] = kwargs["request"].POST.get("customer_caste")

    doc["co-owner_salutation"] = kwargs["request"].POST.get("co-owner_salutation")
    doc["co-owner_fname"] = kwargs["request"].POST.get("co-owner_fname").replace(" ", "")
    doc["co-owner_mname"] = kwargs["request"].POST.get("co-owner_mname").replace(" ", "")
    doc["co-owner_lname"] = kwargs["request"].POST.get("co-owner_lname").replace(" ", "")
    doc["co-owner_dob"] = kwargs["request"].POST.get("co-owner_dob")
    doc["co-owner_gender"] = kwargs["request"].POST.get("co-owner_gender")
    doc["co-owner_occupation"] = kwargs["request"].POST.get("co-owner_occupation")
    doc["co-owner_employer_company_name"] = kwargs["request"].POST.get("co-owner_employer_company_name")
    doc["co-owner_company_address"] = kwargs["request"].POST.get("co-owner_company_address")
    doc["co-owner_posted_at"] = kwargs["request"].POST.get("co-owner_posted_at")
    doc["co-owner_caste"] = kwargs["request"].POST.get("co-owner_caste")
    doc["co-owner_relation"] = kwargs["request"].POST.get("co-owner_relation")

    doc["email"] = kwargs["request"].POST.get("email")
    doc["mobile_no"] = kwargs["request"].POST.get("mobile_no")
    doc["whatsapp_no"] = kwargs["request"].POST.get("whatsapp_no")
    
    doc["father_husband's_salutation"] = kwargs["request"].POST.get("father_husband's_salutation")
    doc["father_husband's_name"] = kwargs["request"].POST.get("father_husband's_name")
    doc["relation"] = kwargs["request"].POST.get("relation")

    doc["copy_from"] = kwargs["request"].POST.get("copy_from")
    doc["contact_p_salutation"] = kwargs["request"].POST.get("contact_p_salutation")
    doc["contact_p_name"] = kwargs["request"].POST.get("contact_p_name")
    doc["contact_p_phone_no"] = kwargs["request"].POST.get("contact_p_phone_no")

    if "copy_present" in kwargs["request"].POST:
        doc["copy_present"] = "copy_present"
    else:
        doc["copy_present"] = " "

    doc["pr_addLine1"] = kwargs["request"].POST.get("pr_addLine1")
    doc["pr_addLine2"] = kwargs["request"].POST.get("pr_addLine2")
    doc["pr_district"] = kwargs["request"].POST.get("pr_district")
    doc["pr_city"] = kwargs["request"].POST.get("pr_city")
    doc["pr_state"] = kwargs["request"].POST.get("pr_state")
    doc["pr_pincode"] = kwargs["request"].POST.get("pr_pincode")

    doc["pe_addLine1"] = kwargs["request"].POST.get("pe_addLine1")
    doc["pe_addLine2"] = kwargs["request"].POST.get("pe_addLine2")
    doc["pe_district"] = kwargs["request"].POST.get("pe_district")
    doc["pe_city"] = kwargs["request"].POST.get("pe_city")
    doc["pe_state"] = kwargs["request"].POST.get("pe_state")
    doc["pe_pincode"] = kwargs["request"].POST.get("pe_pincode")
    
    doc["username"] = kwargs["request"].POST.get("username")
    doc["password"] = kwargs["request"].POST.get("password")
    passport_photo = kwargs["request"].FILES.getlist("passport_photo")

    doc["bank_name"] = kwargs["request"].POST.get("bank_name")
    doc["branch_name"] = kwargs["request"].POST.get("branch_name")
    doc["branch_address"] = kwargs["request"].POST.get("branch_address")
    doc["branch_city"] = kwargs["request"].POST.get("branch_city")
    doc["ifsc_code"] = kwargs["request"].POST.get("ifsc_code")
    doc["account_type"] = kwargs["request"].POST.get("account_type")
    doc["account_no"] = kwargs["request"].POST.get("account_no")

    doc["aadhar_no"] = kwargs["request"].POST.get("aadhar_no")
    aadhar_card = kwargs["request"].FILES.getlist("aadhar_card")
    doc["pan_no"] = kwargs["request"].POST.get("pan_no")
    pan_card = kwargs["request"].FILES.getlist("pan_card")
    doc["voter_id"] = kwargs["request"].POST.get("voter_id")
    voter_id_card = kwargs["request"].FILES.getlist("voter_id_card")
    doc["gst_no"] = kwargs["request"].POST.get("gst_no")
    gst_doc = kwargs["request"].FILES.getlist("gst_doc")
    other_docs = kwargs["request"].FILES.getlist("other_docs")
    brokers_pan_card = kwargs["request"].FILES.getlist("broker's_pan_card")
    cancelled_cheque_passbook = kwargs["request"].FILES.getlist("cancelled_cheque_passbook")

    files = {
        "passport_photo": passport_photo, 
        "aadhar_card": aadhar_card, 
        "pan_card": pan_card, 
        "voter_id_card": voter_id_card,
        "gst_doc": gst_doc, 
        "other_docs": other_docs,
        "broker's_pan_card": brokers_pan_card,
        "cancelled_cheque_passbook": cancelled_cheque_passbook
    }

    return [doc, files]

def getBankData(_id=None, approved_projects=None, **kwargs):
    id = db.getNextId("Master", "Bank")
    doc = {}
    doc["_id"] = "B" + str(id) if len(_id) == 0 else _id
    doc["bank_name"] =kwargs["request"].POST.get("bank_name")
    doc["short_bank_name"] = kwargs["request"].POST.get("short_bank_name")
    doc["branch"] = kwargs["request"].POST.get("branch")
    doc["address"] = kwargs["request"].POST.get("address")
    doc["pin_code"] = kwargs["request"].POST.get("pin_code")
    doc["branch_manager"] = kwargs["request"].POST.get("branch_manager")
    doc["branch_manager_phno"] = kwargs["request"].POST.get("branch_manager_phno")
    doc["contact_person"] = kwargs["request"].POST.get("contact_person")
    doc["contact_person_phno"] = kwargs["request"].POST.get("contact_person_phno")
    doc["ifsc_code"] = kwargs["request"].POST.get("ifsc_code")
    doc["rate_of_interest"] = kwargs["request"].POST.get("rate_of_interest")

    if approved_projects != '':
        projects = approved_projects.split(",")
        approved_projects = []
        for project in projects:
            if len(project) > 0:
                p_id = db.getProjectDetailsByName(project)["_id"]
                reference_dt = {
                    "$ref": "Project",
                    "$id": p_id,
                    "$db": "Master"
                }    
                dt={
                    "project_name": reference_dt
                }
                approved_projects.append(dt)
        doc["approved_projects"] = approved_projects
    else:
        doc["approved_projects"] = []

    list_docs = kwargs["request"].FILES.getlist("list_docs")
    agreements_doc = kwargs["request"].FILES.getlist("agreements_doc")

    files = {
        "list_docs": list_docs, 
        "agreements_doc": agreements_doc
    }

    return [doc, files]   

def getBrokerData(_id=None, **kwargs):
    id = db.getNextId("Master", "Broker")
    doc = {}
    doc["_id"] = "BR" + str(id) if len(_id) == 0 else _id
    doc["broker_salutation"] = kwargs["request"].POST.get("broker_salutation")
    doc["broker_name"] = kwargs["request"].POST.get("broker_name")
    doc["broker_address"] = kwargs["request"].POST.get("broker_address")
    doc["broker_phno"] = kwargs["request"].POST.get("broker_phno")
    doc["brokerage_commission"] = kwargs["request"].POST.get("brokerage_commission")

    doc["aadhar_no"] = kwargs["request"].POST.get("aadhar_no")
    broker_aadhar_card = kwargs["request"].FILES.getlist("broker_aadhar_card")
    doc["pan_no"] = kwargs["request"].POST.get("pan_no")
    broker_pan_card = kwargs["request"].FILES.getlist("broker_pan_card")
    doc["gst_no"] = kwargs["request"].POST.get("gst_no")
    broker_gst_doc = kwargs["request"].FILES.getlist("broker_gst_doc")

    files = {
        "broker_aadhar_card": broker_aadhar_card, 
        "broker_pan_card": broker_pan_card,
        "broker_gst_doc": broker_gst_doc
    }

    return [doc, files]   

#Transaction
def getBookingEntry(_id=None, **kwargs):
    doc = {}
    reference_id = kwargs["request"].POST.get("reference_id")
    doc["_id"] = reference_id if len(_id) == 0 else _id
    doc["reference_id"] = doc["_id"]
    doc["booking_date"] = kwargs["request"].POST.get("booking_date") 
    
    customer_name = kwargs["request"].POST.get("customer_name")
    c_id = db.getCustomerDetailsByName(customer_name)["_id"]
    reference_dt = {
        "$ref": "Customer",
        "$id": c_id,
        "$db": "Master"
    }
    doc["customer_name"] = reference_dt

    doc["landowner_company_share"] = kwargs["request"].POST.get("landowner_company_share")

    project_name = kwargs["request"].POST.get("project_name")
    p_id = db.getProjectDetailsByName(project_name)["_id"]  
    reference_dt = {
        "$ref": "Project",
        "$id": p_id,
        "$db": "Master"
    }
    doc["project_name"] = reference_dt

    doc["block_name"] = kwargs["request"].POST.get("block_name") 
    doc["floor_no"] = kwargs["request"].POST.get("floor_no") 
    doc["flat_no"] = kwargs["request"].POST.get("flat_no") 

    '''block_name = kwargs["request"].POST.get("block_name") 
    reference_dt = {
        "$ref": "",
        "$id": p_id,
        "$db": "Master"
    }
    doc["block_name"] = reference_dt

    floor_no = kwargs["request"].POST.get("floor_no")
    reference_dt = {
        "$ref": "",
        "$id": p_id,
        "$db": "Master"
    }
    doc["floor_no"] = reference_dt

    flat_no = kwargs["request"].POST.get("flat_no")
    reference_dt = {
        "$ref": "",
        "$id": p_id,
        "$db": "Master"
    }
    doc["flat_no"] = reference_dt'''

    doc["flat_condn"] = kwargs["request"].POST.get("flat_condn")
    
    broker_name = kwargs["request"].POST.get("broker_name")
    if broker_name != "DIRECT":
        br_id = db.getBrokerDetailsByName(broker_name)["_id"]
        reference_dt = {
            "$ref": "Broker",
            "$id": br_id,
            "$db": "Master"
        }
        doc["broker_name"] = reference_dt
    else:
        doc["broker_name"] = broker_name

    n = int(kwargs["request"].POST.get("fs1-fields"))
    payment_details = []
    for i in range(n):
        dt = {
            "payment_date": kwargs["request"].POST.get("fs1-" + str(i) + "-payment_date"),
            "payment_mode": kwargs["request"].POST.get("fs1-" + str(i) + "-payment_mode"),
            "payment_details": kwargs["request"].POST.get("fs1-" + str(i) + "-payment_details"),
            "bank_name": kwargs["request"].POST.get("fs1-" + str(i) + "-bank_name"),
            "amount": kwargs["request"].POST.get("fs1-" + str(i) + "-amount")
        }
        payment_details.append(dt)    
    doc["payment_details"] = payment_details

    doc["sellable_area"] = kwargs["request"].POST.get("sellable_area")
    doc["sellable_area_rate"] = kwargs["request"].POST.get("sellable_area_rate")
    doc["sellable_area_amount"] = kwargs["request"].POST.get("sellable_area_amount")
    doc["car_parking_chgs"] = kwargs["request"].POST.get("car_parking_chgs")
    doc["dg_chgs"] = kwargs["request"].POST.get("dg_chgs")
    doc["trans_substation_chgs"] = kwargs["request"].POST.get("trans_substation_chgs")
    doc["discount"] = kwargs["request"].POST.get("discount")
    doc["cash_discount"] = kwargs["request"].POST.get("cash_discount")
    doc["add_gst_pct"] = kwargs["request"].POST.get("add_gst_pct")    
    doc["less_booking_amount"] = kwargs["request"].POST.get("less_booking_amount")

    files = {}

    return [doc, files]

def getCustomerRequest(_id=None, **kwargs):
    id = db.getNextId("Master", "Project")
    doc = {}
    doc["_id"] = "P" + str(id) if len(_id) == 0 else _id
    doc["request_date"] = kwargs["request"].POST.get("request_date")
    doc["customer_salutation"] = kwargs["request"].POST.get("customer_salutation")
    doc["customer_fname"] = kwargs["request"].POST.get("customer_fname")
    doc["customer_mname"] = kwargs["request"].POST.get("customer_mname")
    doc["customer_lname"] = kwargs["request"].POST.get("customer_lname")
    doc["customer_dob"] = kwargs["request"].POST.get("customer_dob")
    doc["customer_gender"] = kwargs["request"].POST.get("customer_gender")
    doc["mobile_no"] = kwargs["request"].POST.get("mobile_no")
    doc["whatsapp_no"] = kwargs["request"].POST.get("whatsapp_no")
    doc["email"] = kwargs["request"].POST.get("email")
    doc["occupation"] = kwargs["request"].POST.get("occupation")
    doc["contact_p_salutation"] = kwargs["request"].POST.get("contact_p_salutation")
    doc["contact_p_name"] = kwargs["request"].POST.get("contact_p_name")
    doc["contact_p_phone_no"] = kwargs["request"].POST.get("contact_p_phone_no")
    doc["pr_addLine1"] = kwargs["request"].POST.get("pr_addLine1")
    doc["pr_addLine2"] = kwargs["request"].POST.get("pr_addLine2")
    doc["pr_city"] = kwargs["request"].POST.get("pr_city")
    doc["pr_state"] = kwargs["request"].POST.get("pr_state")
    doc["pr_pincode"] = kwargs["request"].POST.get("pr_pincode")
    doc["project_name"] = kwargs["request"].POST.get("project_name")
    doc["block_name"] = kwargs["request"].POST.get("block_name")
    doc["floor_no"] = kwargs["request"].POST.get("floor_no")
    doc["flat_no"] = kwargs["request"].POST.get("flat_no")
    doc["to_be_hold_days"] = kwargs["request"].POST.get("to_be_hold_days")
    doc["status"] = kwargs["request"].POST.get("status")
    doc["reason_of_unhold"] = kwargs["request"].POST.get("reason_of_unhold")

    files = {}

    return [doc, files]

#Settings
def getOrganisationData(_id=None, **kwargs):
    id = db.getNextId("Settings", "UserMaster")
    doc = {}
    doc["_id"] = "O" + str(id) if len(_id) == 0 else _id
    
    doc["organisation_name"] = kwargs["request"].POST.get("organisation_name")
    doc["estd_on"] = kwargs["request"].POST.get("estd_on")
    doc["branch"] = kwargs["request"].POST.get("branch")
    doc["constitution"] = kwargs["request"].POST.get("constitution")    
    doc["nature_of_business"] = kwargs["request"].POST.get("nature_of_business")
    doc["start_fin_yr"] = kwargs["request"].POST.get("start_fin_yr")
    doc["enable_tds_deduction"] = kwargs["request"].POST.get("enable_tds_deduction")
    doc["tds_deduction_type"] = kwargs["request"].POST.get("tds_deduction_type")    
    doc["addLine1"] = kwargs["request"].POST.get("addLine1")
    doc["addLine2"] = kwargs["request"].POST.get("addLine2")
    doc["city"] = kwargs["request"].POST.get("city")    
    doc["district"] = kwargs["request"].POST.get("district")
    doc["state"] = kwargs["request"].POST.get("state")
    doc["pin"] = kwargs["request"].POST.get("pin")    
    doc["mobile_no"] = kwargs["request"].POST.get("mobile_no")
    doc["whatsapp_no"] = kwargs["request"].POST.get("whatsapp_no")
    doc["email"] = kwargs["request"].POST.get("email")

    doc["pan_no"] = kwargs["request"].POST.get("pan_no")
    pan_card = kwargs["request"].FILES.getlist("pan_card")
    doc["tan_no"] = kwargs["request"].POST.get("tan_no")
    tan_doc = kwargs["request"].FILES.getlist("tan_doc")
    doc["gstin_no"] = kwargs["request"].POST.get("gstin_no")
    gst_doc = kwargs["request"].FILES.getlist("gst_doc")

    files = {
        "pan_card": pan_card,
        "tan_doc": tan_doc, 
        "gst_doc": gst_doc, 
    }

    if doc["constitution"] == "Proprietorship":
        doc["proprietors's_name"] = kwargs["request"].POST.get("proprietors's_name")
        doc["p_father's_name"] = kwargs["request"].POST.get("p_father's_name")
        doc["p_addLine1"] = kwargs["request"].POST.get("p_addLine1")
        doc["p_addLine2"] = kwargs["request"].POST.get("p_addLine2")
        doc["p_city"] = kwargs["request"].POST.get("p_city")
        doc["p_district"] = kwargs["request"].POST.get("p_district")
        doc["p_state"] = kwargs["request"].POST.get("p_state")
        doc["p_pin"] = kwargs["request"].POST.get("p_pin")
        
        doc["p_aadhar_no"] = kwargs["request"].POST.get("p_aadhar_no")
        p_aadhar_card = kwargs["request"].FILES.getlist("p_aadhar_card")
        files["p_aadhar_card"] = p_aadhar_card

    elif doc["constitution"] == "Partnership" or doc["constitution"] == "LLP":
        no_partners = kwargs["request"].POST.get("no_partners")
        doc["no_partners"] = no_partners

        partners = []
        for i in range(no_partners):
            dt = {
                "partner's_name": kwargs["request"].POST.get("fs1-" + str(i) + "-partner's_name"),
                "pa_father's_name": kwargs["request"].POST.get("fs1-" + str(i) + "-pa_father's_name"),
                "pa_addLine1": kwargs["request"].POST.get("fs1-" + str(i) + "-pa_addLine1"),
                "pa_addLine2": kwargs["request"].POST.get("fs1-" + str(i) + "-pa_addLine1"),
                "pa_city": kwargs["request"].POST.get("fs1-" + str(i) + "-pa_city"),
                "pa_district": kwargs["request"].POST.get("fs1-" + str(i) + "-pa_district"),
                "pa_state": kwargs["request"].POST.get("fs1-" + str(i) + "-pa_state"),
                "pa_pin": kwargs["request"].POST.get("fs1-" + str(i) + "-pa_pin"),                
                "pa_pan_no": kwargs["request"].POST.get("fs1-" + str(i) + "-pa_pan_no"),
                "pa_aadhar_no": kwargs["request"].POST.get("fs1-" + str(i) + "-pa_aadhar_no"),                
                "pa_interest_pct": kwargs["request"].POST.get("fs1-" + str(i) + "-pa_interest_pct"),
            }
            partners.append(dt)

            pa_pan_card = kwargs["request"].FILES.getlist("fs1-" + str(i) + "-pa_pan_card")
            files["fs1-" + str(i) + "-pa_pan_card"] = pa_pan_card

            pa_aadhar_card = kwargs["request"].FILES.getlist("fs1-" + str(i) + "-pa_aadhar_card")
            files["fs1-" + str(i) + "-pa_aadhar_card"] = pa_aadhar_card

        doc["partners"] = partners
        
    elif doc["constitution"] == "Private Limited Company":
        no_directors = kwargs["request"].POST.get("no_directors")
        doc["no_directors"] = no_directors

        no_promoters = kwargs["request"].POST.get("no_promoters")
        doc["no_promoters"] = no_promoters

        doc["cin_no"] = kwargs["request"].POST.get("cin_no")
        cin_doc = kwargs["request"].FILES.getlist("cin_doc")
        files["cin_doc"] = cin_doc

        directors = []
        for i in range(no_directors):
            dt = {
                "director's_name": kwargs["request"].POST.get("fs1-" + str(i) + "-director's_name"),
                "d_father's_name": kwargs["request"].POST.get("fs1-" + str(i) + "-d_father's_name"),
                "d_addLine1": kwargs["request"].POST.get("fs1-" + str(i) + "-d_addLine1"),
                "d_addLine2": kwargs["request"].POST.get("fs1-" + str(i) + "-d_addLine1"),
                "d_city": kwargs["request"].POST.get("fs1-" + str(i) + "-d_city"),
                "d_district": kwargs["request"].POST.get("fs1-" + str(i) + "-d_district"),
                "d_state": kwargs["request"].POST.get("fs1-" + str(i) + "-d_state"),
                "d_pin": kwargs["request"].POST.get("fs1-" + str(i) + "-d_pin"),                
                "d_pan_no": kwargs["request"].POST.get("fs1-" + str(i) + "-d_pan_no"),
                "d_aadhar_no": kwargs["request"].POST.get("fs1-" + str(i) + "-d_aadhar_no"),                
                "d_director_type": kwargs["request"].POST.get("fs1-" + str(i) + "-d_director_type"),
                "d_din_no": kwargs["request"].POST.get("fs1-" + str(i) + "-d_din_no"),
                "d_valid_upto": kwargs["request"].POST.get("fs1-" + str(i) + "-d_valid_upto")
            }
            directors.append(dt)

            d_pan_card = kwargs["request"].FILES.getlist("fs1-" + str(i) + "-d_pan_card")
            files["fs1-" + str(i) + "-d_pan_card"] = d_pan_card

            d_aadhar_card = kwargs["request"].FILES.getlist("fs1-" + str(i) + "-d_aadhar_card")
            files["fs1-" + str(i) + "-d_aadhar_card"] = d_aadhar_card

            d_din_doc = kwargs["request"].FILES.getlist("fs1-" + str(i) + "-d_din_doc")
            files["fs1-" + str(i) + "-d_din_doc"] = d_din_doc

        doc["directors"] = directors

        promoters = []
        for i in range(no_promoters):
            dt = {
                "promoter's_name": kwargs["request"].POST.get("fs1-" + str(i) + "-promoter's_name"),
                "pr_father's_name": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_father's_name"),
                "pr_addLine1": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_addLine1"),
                "pr_addLine2": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_addLine1"),
                "pr_city": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_city"),
                "pr_district": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_district"),
                "pr_state": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_state"),
                "pr_pin": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_pin"),
                "pr_pan_no": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_pan_no"),
                "pr_aadhar_no": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_aadhar_no"),
                "pr_din_no": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_din_no"),
                "pr_valid_upto": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_valid_upto"),
                "pr_pct_share": kwargs["request"].POST.get("fs1-" + str(i) + "-pr_pct_share")
            }
            promoters.append(dt)

            pr_pan_card = kwargs["request"].FILES.getlist("fs1-" + str(i) + "-pr_pan_card")
            files["fs1-" + str(i) + "-pr_pan_card"] = pr_pan_card

            pr_aadhar_card = kwargs["request"].FILES.getlist("fs1-" + str(i) + "-pr_aadhar_card")
            files["fs1-" + str(i) + "-pr_aadhar_card"] = pr_aadhar_card

            pr_din_doc = kwargs["request"].FILES.getlist("fs1-" + str(i) + "-pr_din_doc")
            files["fs1-" + str(i) + "-pr_din_doc"] = pr_din_doc

        doc["promoters"] = promoters

    return [doc, files]

def getUserData(_id=None, **kwargs):
    id = db.getNextId("Settings", "UserMaster")
    doc = {}
    doc["_id"] = "U" + str(id) if len(_id) == 0 else _id
    doc["username"] = kwargs["request"].POST.get("username")
    doc["password"] = kwargs["request"].POST.get("password")
    doc["user_type"] = kwargs["request"].POST.get("user_type")
    doc["full_name"] = kwargs["request"].POST.get("full_name")
    doc["designation"] = kwargs["request"].POST.get("designation")

    files = {}

    return [doc, files]