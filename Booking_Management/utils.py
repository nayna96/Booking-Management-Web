from . import db

def getProjectData(_id, **kwargs):
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
    pass

def getFlatData(_id=None, **kwargs):
    pass

def getCustomerData(_id=None, **kwargs):
    id = db.getNextId("Master", "Customer")
    doc = {}
    doc["_id"] = "C" + str(id) if _id == None else _id     
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

def getBankData(_id=None, **kwargs):
    id = db.getNextId("Master", "Bank")
    doc = {}
    doc["_id"] = "B" + str(id) if _id == None else _id   

def getBookingEntry(_id=None, **kwargs):
    pass

def getCustomerRequest(_id=None, **kwargs):
    pass

def getUserData(_id=None, **kwargs):
    id = db.getNextId("Settings", "UserMaster")
    doc = {}
    doc["_id"] = "U" + str(id) if _id == None else _id
    doc["username"] = kwargs["request"].POST.get("username")
    doc["password"] = kwargs["request"].POST.get("password")
    doc["user_type"] = kwargs["request"].POST.get("user_type")
    doc["full_name"] = kwargs["request"].POST.get("ful_name")
    doc["designation"] = kwargs["request"].POST.get("designation")

    return doc