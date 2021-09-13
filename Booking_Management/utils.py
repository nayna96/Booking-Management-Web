from . import db

def getUserData(request, _id=None):
    id = db.getNextId("Settings", "UserMaster")
    doc = {}
    doc["_id"] = "U" + str(id) if _id == None else _id
    doc["username"] = request.POST.get("username")
    doc["password"] = request.POST.get("password")
    doc["user_type"] = request.POST.get("user_type")
    doc["full_name"] = request.POST.get("ful_name")
    doc["designation"] = request.POST.get("designation")

    return doc

def getCustomerData(request, _id=None):
    id = db.getNextId("Master", "Customer")
    doc = {}
    doc["_id"] = "C" + str(id) if _id == None else _id     
    doc["customer_salutation"] = request.POST.get("customer_salutation")
    doc["customer_fname"] = request.POST.get("customer_fname")
    doc["customer_mname"] = request.POST.get("customer_mname")
    doc["customer_lname"] = request.POST.get("customer_lname")
    doc["customer_dob"] = request.POST.get("customer_dob")
    doc["customer_gender"] = request.POST.get("customer_gender")

    doc["co-owner_salutation"] = request.POST.get("co-owner_salutation")
    doc["co-owner_fname"] = request.POST.get("co-owner_fname")
    doc["co-owner_mname"] = request.POST.get("co-owner_mname")
    doc["co-owner_lname"] = request.POST.get("co-owner_lname")
    doc["co-owner_dob"] = request.POST.get("co-owner_dob")
    doc["co-owner_gender"] = request.POST.get("co-owner_gender")

    doc["email"] = request.POST.get("email")
    doc["mobile_no"] = request.POST.get("mobile_no")
    doc["whatsapp_no"] = request.POST.get("whatsapp_no")
    
    doc["father_husband's_salutation"] = request.POST.get("father_husband's_salutation")
    doc["father_husband's_name"] = request.POST.get("father_husband's_name")
    doc["relation"] = request.POST.get("relation")

    doc["copy_present"] = request.POST.get("copy_present", None)

    doc["pr_addLine1"] = request.POST.get("pr_addLine1")
    doc["pr_addLine2"] = request.POST.get("pr_addLine2")
    doc["pr_district"] = request.POST.get("pr_district")
    doc["pr_city"] = request.POST.get("pr_city")
    doc["pr_state"] = request.POST.get("pr_state")
    doc["pr_pincode"] = request.POST.get("pr_pincode")

    doc["pe_addLine1"] = request.POST.get("pe_addLine1")
    doc["pe_addLine2"] = request.POST.get("pe_addLine2")
    doc["pe_district"] = request.POST.get("pe_district")
    doc["pe_city"] = request.POST.get("pe_city")
    doc["pe_state"] = request.POST.get("pe_state")
    doc["pe_pincode"] = request.POST.get("pe_pincode")

    doc["copy_from"] = request.POST.get("copy_from")
    doc["contact_p_salutation"] = request.POST.get("contact_p_salutation")
    doc["contact_p_name"] = request.POST.get("contact_p_name")
    doc["contact_p_phone_no"] = request.POST.get("contact_p_phone_no")

    doc["broker's_salutation"] = request.POST.get("broker's_salutation")
    doc["broker's_name"] = request.POST.get("broker's_name")
    
    doc["occupation"] = request.POST.get("occupation")
    doc["caste"] = request.POST.get("caste")

    doc["username"] = request.POST.get("username")
    doc["password"] = request.POST.get("password")
    passport_photo = request.FILES.getlist("passport_photo")

    doc["bank_name"] = request.POST.get("bank_name")
    doc["branch_name"] = request.POST.get("branch_name")
    doc["account_type"] = request.POST.get("account_type")
    doc["account_no"] = request.POST.get("account_no")

    doc["aadhar_no"] = request.POST.get("aadhar_no")
    aadhar_card = request.FILES.getlist("aadhar_card")
    doc["pan_no"] = request.POST.get("pan_no")
    pan_card = request.FILES.getlist("pan_card")
    doc["voter_id"] = request.POST.get("voter_id")
    voter_id_card = request.FILES.getlist("voter_id_card")
    doc["gst_no"] = request.POST.get("gst_no")
    gst_doc = request.FILES.getlist("gst_doc")
    other_docs = request.FILES.getlist("other_docs")

    files = {
        "passport_photo": passport_photo, 
        "aadhar_card": aadhar_card, 
        "pan_card": pan_card, 
        "voter_id_card": voter_id_card,
        "gst_doc": gst_doc, 
        "other_docs": other_docs
    }

    return [doc, files]