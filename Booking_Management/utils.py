from . import db

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
        dt={
            "bank_name": kwargs["request"].POST.get("fs1-" + str(i) + "-bank_name")
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
            "area": kwargs["request"].POST.get("fs2-" + str(i) + "-area")
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

    files = {
        "land_docs": land_docs,
        "agreements_doc": agreements_doc,
        "pow": pow,
        "dev_auth_approval": dev_auth_approval,
        "rera_certificate": rera_certificate
    }

    return [doc, files]    

def getBlockData(_id=None, **kwargs):
    project_name = kwargs["request"].POST.get("project_name")
    p_id = db.getProjectByName(project_name)["_id"]

    doc = {}
    doc["_id"] = p_id + "B" if len(_id) == 0 else _id
    doc["project_name"] = project_name
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
    p_id = db.getProjectByName(project_name)["_id"]

    block_name = kwargs["request"].POST.get("block_name")
    floor_no = kwargs["request"].POST.get("floor_no")

    doc = {}
    doc["_id"] =  p_id + "_" + block_name + "_" + floor_no + "F" if len(_id) == 0 else _id
    doc["project_name"] = project_name
    doc["block_name"] = block_name
    doc["floor_no"] = floor_no

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
    doc["customer_fname"] = kwargs["request"].POST.get("customer_fname")
    doc["customer_mname"] = kwargs["request"].POST.get("customer_mname")
    doc["customer_lname"] = kwargs["request"].POST.get("customer_lname")
    doc["customer_dob"] = kwargs["request"].POST.get("customer_dob")
    doc["customer_gender"] = kwargs["request"].POST.get("customer_gender")

    doc["co-owner_salutation"] = kwargs["request"].POST.get("co-owner_salutation")
    doc["co-owner_fname"] = kwargs["request"].POST.get("co-owner_fname")
    doc["co-owner_mname"] = kwargs["request"].POST.get("co-owner_mname")
    doc["co-owner_lname"] = kwargs["request"].POST.get("co-owner_lname")
    doc["co-owner_dob"] = kwargs["request"].POST.get("co-owner_dob")
    doc["co-owner_gender"] = kwargs["request"].POST.get("co-owner_gender")

    doc["email"] = kwargs["request"].POST.get("email")
    doc["mobile_no"] = kwargs["request"].POST.get("mobile_no")
    doc["whatsapp_no"] = kwargs["request"].POST.get("whatsapp_no")
    
    doc["father_husband's_salutation"] = kwargs["request"].POST.get("father_husband's_salutation")
    doc["father_husband's_name"] = kwargs["request"].POST.get("father_husband's_name")
    doc["relation"] = kwargs["request"].POST.get("relation")

    doc["copy_present"] = kwargs["request"].POST.get("copy_present", None)

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

    doc["copy_from"] = kwargs["request"].POST.get("copy_from")
    doc["contact_p_salutation"] = kwargs["request"].POST.get("contact_p_salutation")
    doc["contact_p_name"] = kwargs["request"].POST.get("contact_p_name")
    doc["contact_p_phone_no"] = kwargs["request"].POST.get("contact_p_phone_no")

    doc["broker's_salutation"] = kwargs["request"].POST.get("broker's_salutation")
    doc["broker's_name"] = kwargs["request"].POST.get("broker's_name")
    
    doc["occupation"] = kwargs["request"].POST.get("occupation")
    doc["caste"] = kwargs["request"].POST.get("caste")

    doc["username"] = kwargs["request"].POST.get("username")
    doc["password"] = kwargs["request"].POST.get("password")
    passport_photo = kwargs["request"].FILES.getlist("passport_photo")

    doc["bank_name"] = kwargs["request"].POST.get("bank_name")
    doc["branch_name"] = kwargs["request"].POST.get("branch_name")
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

    files = {
        "passport_photo": passport_photo, 
        "aadhar_card": aadhar_card, 
        "pan_card": pan_card, 
        "voter_id_card": voter_id_card,
        "gst_doc": gst_doc, 
        "other_docs": other_docs
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
    doc["approved_projects"] = approved_projects if approved_projects != None else []

    list_docs = kwargs["request"].FILES.getlist("list_docs")
    agreements_doc = kwargs["request"].FILES.getlist("agreements_doc")

    files = {
        "list_docs": list_docs, 
        "agreements_doc": agreements_doc
    }

    return [doc, files]   

def getBookingEntry(_id=None, **kwargs):
    doc = {}
    reference_id = kwargs["request"].POST.get("reference_id")
    doc["_id"] = reference_id if len(_id) == 0 else _id
    doc["booking_date"] = kwargs["request"].POST.get("booking_date") 
    doc["customer_name"] = kwargs["request"].POST.get("customer_name") 
    doc["landowner_company_share"] = kwargs["request"].POST.get("landowner_company_share") 
    doc["project_name"] = kwargs["request"].POST.get("project_name") 
    doc["block_name"] = kwargs["request"].POST.get("block_name") 
    doc["floor_no"] = kwargs["request"].POST.get("floor_no") 
    doc["flat_no"] = kwargs["request"].POST.get("flat_no") 
    doc["flat_condn"] = kwargs["request"].POST.get("flat_condn")
    doc["sellable_area"] = kwargs["request"].POST.get("sellable_area")
    doc["sellable_area_rate"] = kwargs["request"].POST.get("sellable_area_rate")
    doc["sellable_area_amount"] = kwargs["request"].POST.get("sellable_area_amount")
    doc["car_parking_chgs"] = kwargs["request"].POST.get("car_parking_chgs")
    doc["dg_chgs"] = kwargs["request"].POST.get("dg_chgs")
    doc["trans_substation_chgs"] = kwargs["request"].POST.get("trans_substation_chgs")
    doc["discount"] = kwargs["request"].POST.get("discount")
    doc["cash_discount"] = kwargs["request"].POST.get("cash_discount")
    doc["add_gst_pct"] = kwargs["request"].POST.get("add_gst_pct")

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

def getUserData(_id=None, **kwargs):
    id = db.getNextId("Settings", "UserMaster")
    doc = {}
    doc["_id"] = "U" + str(id) if len(_id) == 0 else _id
    doc["username"] = kwargs["request"].POST.get("username")
    doc["password"] = kwargs["request"].POST.get("password")
    doc["user_type"] = kwargs["request"].POST.get("user_type")
    doc["full_name"] = kwargs["request"].POST.get("ful_name")
    doc["designation"] = kwargs["request"].POST.get("designation")

    files = {}

    return [doc, files]