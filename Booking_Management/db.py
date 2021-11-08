from pymongo import MongoClient
from gridfs import GridFS
from functools import reduce
import bson

#connection_string = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
connection_string = "mongodb+srv://admin:admin@cluster0.vlkpb.mongodb.net/test?authSource=admin&replicaSet=atlas-uip17y-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true&ssl_cert_reqs=CERT_NONE"

try:
    client = MongoClient(connection_string)
except:
    pass
    
def ifExistsDoc(db_name, collection_name, filters):
    db = client[db_name]
    collection = db[collection_name]

    count = collection.find({"$and": filters}).count()

    if count > 0:
        return True
            
    return False
        
def getNextId(db_name, collection_name):
    db = client[db_name]
    collection = db[collection_name]
    for doc in collection.find().sort("_id", -1):
        return int(doc["_id"][-1]) + 1

def verifyUser(username, password):
    if username != "" and password != "":
        pwd = getUserDetailsByName(username)["password"]
        if password == pwd:
            return True
    return True

def getDocById(db_name, collection_name, _id):
    db = client[db_name]
    collection = db[collection_name]

    filter = {"_id": _id}

    return collection.find_one(filter)

def getDetails(db_name, collection_name):
    details = []
    db = client[db_name]
    collection = db[collection_name]

    for x in collection.find({}):
        for key, value in x.items():
            if type(value) == list:
                for el in value:
                    for k,v in el.items():
                        if isinstance(v, bson.dbref.DBRef):
                            doc = getDocById(v.database, v.collection, v.id)
                            if k == "bank_name":
                                el["bank_name"] = doc["short_bank_name"]
                            else:
                                el[k] = doc[k]
            else:
                if isinstance(value, bson.dbref.DBRef):
                    doc = getDocById(value.database, value.collection, value.id)
                    if key == "customer_name":
                        x["customer_name"] = doc["customer_fname"] + " " + doc["customer_mname"] + " " + doc["customer_lname"]
                    else:
                        x[key] = doc[key]
        details.append(x)
    return details

#Project Master
def getProjectsList(db_name="Master", collection_name="Project"):
    lst = []

    db = client[db_name]
    collection = db[collection_name]

    filter = {}

    documents = collection.find(filter)

    for document in documents:
        value = document["project_name"]
        if isinstance(value, bson.dbref.DBRef):
            doc = getDocById(value.database, value.collection, value.id)
            document["project_name"] = doc["project_name"]
        lst.append(document["project_name"])

    return reduce(lambda acc,elem: acc+[elem] if not elem in acc else acc , lst, [])

def getProjectDetailsByName(project_name, db_name="Master", collection_name="Project"):
    db = client[db_name]
    collection = db[collection_name]

    filter = { "project_name": project_name }
    document = collection.find_one(filter)

    for bank in document["approved_banks"]:
        doc = getDocById(bank["bank_name"].database, bank["bank_name"].collection, bank["bank_name"].id)
        bank["bank_name"] = doc["short_bank_name"]

    return document

def getProjectStatus(project_name, db_name="Master", collection_name="Project"):
    details = getProjectDetailsByName(project_name)
    return details["project_status"]

#Block Master
def getBlockDetailsByProject(project_name, db_name="Master", collection_name="Block"):
    db = client[db_name]
    collection = db[collection_name]

    p_id = getProjectDetailsByName(project_name)["_id"]
    filter = { "project_name.$id": p_id }

    document = collection.find_one(filter)
    document["project_name"] = project_name
    return document
    
def getBlocksListByProject(project_name, db_name="Master", collection_name="Block"):
    blocks_list = []

    db = client[db_name]
    collection = db[collection_name]

    p_id = getProjectDetailsByName(project_name)["_id"]
    filter = { "project_name.$id": p_id }

    documents = collection.find(filter)
    for document in documents:
        blocks = document["blocks"]
        for block in blocks:
            blocks_list.append(block["block_name"])

    return reduce(lambda acc,elem: acc+[elem] if not elem in acc else acc , blocks_list, [])
        
def getFloorsListByBlock(project_name, block_name, 
                        db_name="Master", collection_name="Block"):
    floors_list = []

    db = client[db_name]
    collection = db[collection_name]

    p_id = getProjectDetailsByName(project_name)["_id"]
    filter = { "project_name.$id": p_id }

    documents = collection.find(filter)
    for document in documents:
        blocks = document["blocks"]
        for block in blocks:
            if block["block_name"] == block_name:
                floors_list.append(block["floor_no"])

    return floors_list

def getFlatDetailsByFloor(project_name, block_name, floor_no, 
                        db_name="Master", collection_name="Flat"):
    db = client[db_name]
    collection = db[collection_name]

    p_id = getProjectDetailsByName(project_name)["_id"]
    filter = [
        { "project_name.$id": p_id },
        { "block_name":block_name },
        { "floor_no": floor_no }
    ]
    document = collection.find_one({"$and": filter})
    document["project_name"] = project_name
    return document

def getFlatsListByFloorNo(project_name, block_name, floor_no, share_type, save_update):
    if save_update == "Save":
        flat_status = ["OPEN"]
    else:
        flat_status = ["OPEN", "BOOKED"]

    lst = []

    entry = getFlatDetailsByFloor(project_name, block_name, floor_no)
    if len(entry) > 0:
        flats = entry["flats"]
    else:
        flats = []
    
    for flat in flats:
        if len(share_type) > 0:
            if flat["flat_status"] in flat_status and share_type == flat["ownership_status"]:
                lst.append(flat["flat_no"])
        else:
            lst.append(flat["flat_no"])
    return lst

def getFlatDetailsByFlatNo(project_name, block_name, floor_no, flat_no):
    entry = getFlatDetailsByFloor(project_name, block_name, floor_no)
    flats = entry["flats"]
    for flat in flats:
        if flat["flat_no"] == flat_no:
            return flat

def getNoFlatsByFloor(project_name, block_name, floor_no, 
    db_name="Master", collection_name="Block"):

    no_flats = 0
    
    db = client[db_name]
    collection = db[collection_name]

    p_id = getProjectDetailsByName(project_name)["_id"]
    filter = { "project_name.$id": p_id }

    documents = collection.find(filter)
    for document in documents:
        blocks = document["blocks"]
        for block in blocks:
            if block["block_name"] == block_name and block["floor_no"] == floor_no:
                no_flats = block["no_flats"]
    
    return no_flats

def updateFlatStatus(project_name, block_name, floor_no, flat_no, flat_status,
    db_name="Master", collection_name="Flat"):

    db = client[db_name]
    collection = db[collection_name]

    filter = {
        "project_name": project_name ,
        "block_name":block_name ,
        "floor_no": floor_no
        }
 
    update = { "$set": { "flats.$[f].flat_status" : flat_status } }
    array_filters=[{"f.flat_no" : flat_no }]

    collection.update_one(filter, update, array_filters=array_filters)
    
#Customer Master
def getOccupations(db_name="Master", collection_name="Customer"):
    occupations_list = []
    db = client[db_name]
    collection = db[collection_name]
    for item in collection.find({}):
        if item["customer_occupation"] != "BUSINESS" and  item["customer_occupation"] != "SELF-EMPLOYED" and item["customer_occupation"] != "SERVICE" :
            occupations_list.append(item["customer_occupation"])    
    return reduce(lambda acc,elem: acc+[elem] if not elem in acc else acc , occupations_list, [])

def getCastes(db_name="Master", collection_name="Customer"):
    castes_list = []
    db = client[db_name]
    collection = db[collection_name]
    for item in collection.find({}):
        if item["customer_caste"] != "SC" and  item["customer_caste"] != "ST" :
            castes_list.append(item["customer_caste"])    
    return reduce(lambda acc,elem: acc+[elem] if not elem in acc else acc , castes_list, [])

def ifPhNoExists(ph_no, db_name="Master", collection_name="Customer"):
    db = client[db_name]
    collection = db[collection_name]
    for item in collection.find({}):
        if item["mobile_no"] == ph_no:    
            return True
    return False
        
def getCustomersList(db_name="Master", collection_name="Customer"):
    lst = []

    db = client[db_name]
    collection = db[collection_name]

    filter = {}

    documents = collection.find(filter)

    for document in documents:
        lst.append(document["customer_fname"] + " " + document["customer_mname"] + " " + document["customer_lname"])

    return lst

def getCustomerDetailsByName(customer_name, db_name="Master", collection_name="Customer"):
    customerDetails = []
    fname = customer_name.split(' ')[0]
    mname = customer_name.split(' ')[1]
    lname = customer_name.split(' ')[2]

    db = client[db_name]
    collection = db[collection_name]
    filter = [
        { "customer_fname": fname },
        { "customer_mname": mname },
        { "customer_lname": lname }]

    return collection.find_one({"$and": filter})

def getCustomerDetailsByFlatNo(project_name, block_name, floor_no, 
        flat_no, collection_name, db_name="Transaction"):
    db = client[db_name]
    collection = db[collection_name]

    p_id = getProjectDetailsByName(project_name)["_id"]

    filter = [
        { "project_name.$id": p_id },
        { "block_name": block_name },
        { "floor_no": floor_no },
        { "flat_no": flat_no }
    ]

    documents = collection.find({"$and": filter})

    customer_name = ""
    for document in documents:
        if "customer_name" in document:
            customer_name = document["customer_name"]
            doc = getDocById(customer_name.database, customer_name.collection, customer_name.id)
            customer_name = doc["customer_fname"] + " " + doc["customer_mname"] + " " + doc["customer_lname"]
        elif "customer_fname" in document and "customer_mname" in document and "customer_lname" in document:
            customer_name = document["customer_fname"] + " " + document["customer_mname"] + " " + document["customer_lname"]
        break

    if len(customer_name) > 0:
        if collection_name == "BookingEntry":
            return getCustomerDetailsByName(customer_name)                        
        else:
            return getCustomerDetailsByName(customer_name, "Transaction", collection_name)
    else:
        return {}
        
def getBanksList(db_name="Master", collection_name="Bank"):
    lst = []

    db = client[db_name]
    collection = db[collection_name]

    filter = {}
    fields = {"short_bank_name":1, "_id":0}

    documents = collection.find(filter, fields)

    for document in documents:
        lst.append(document["short_bank_name"])

    return lst

def getBankDetailsByName(bank_name=None, short_bank_name = None, db_name="Master", collection_name="Bank"):
    db = client[db_name]
    collection = db[collection_name]

    if bank_name != None:   
        filter = { "bank_name": bank_name }
    elif short_bank_name != None:
        filter = { "short_bank_name": short_bank_name }

    document = collection.find_one(filter)

    for project in document["approved_projects"]:
        doc = getDocById(project["project_name"].database, project["project_name"].collection, project["project_name"].id)
        project["project_name"] = doc["project_name"]

    return document

def updateBankDetails(approved_banks, project_name, 
                        db_name = "Master", collection_name = "Bank"):        
    db = client[db_name]
    collection = db[collection_name]

    p_id = getProjectDetailsByName(project_name)["_id"]

    #remove selected project from all banks
    lst = list(collection.find({}))
    for el in lst:
        array = el["approved_projects"]            

        reference_dt = {
            "$ref": "Project",
            "$id": p_id,
            "$db": "Master"
        }    
        doc = { "project_name" : reference_dt }
        for element in array:
            if doc["project_name"]["$id"] == element["project_name"].id:    
                array.remove(element)

        filter = { "bank_name": el["bank_name"] }
        update = { "$set": { "approved_projects" : array } }
        collection.update_one(filter, update)

    #add project name in required bank
    for approved_bank in approved_banks:
        if len(approved_bank) > 0:
            doc = getDocById(approved_bank["$db"], approved_bank["$ref"], approved_bank["$id"])
            filter1 = { "short_bank_name" : doc["short_bank_name"] }
            array1 = collection.find_one(filter1)["approved_projects"]
            
            reference_dt = {
                "$ref": "Project",
                "$id": p_id,
                "$db": "Master"
            }
            doc1 = { "project_name" : reference_dt }
            array1.append(doc1)            
            
            update1 = { "$set": { "approved_projects" : array1 } }
            collection.update_one(filter1, update1)

def getBanks(db_name="Transaction", collection_name="BookingEntry"):
    banks_list = []
    db = client[db_name]
    collection = db[collection_name]
    for item in collection.find({}):
        for el in item["payment_details"]:
            if el["bank_name"] != "CASH":
                banks_list.append(el["bank_name"])    
    return reduce(lambda acc,elem: acc+[elem] if not elem in acc else acc , banks_list, [])

def getBrokersList(db_name="Master", collection_name="Broker"):
    lst = []

    db = client[db_name]
    collection = db[collection_name]

    filter = {}
    
    documents = collection.find(filter)

    for document in documents:
        lst.append(document["broker_name"])

    return lst

def getBrokerDetailsByName(broker_name, db_name="Master", collection_name="Broker"):
    db = client[db_name]
    collection = db[collection_name]

    filter = { "broker_name": broker_name }
    
    return collection.find_one(filter)

def getBookingEntryByReferenceId(reference_id, db_name = "Transaction", collection_name = "BookingEntry"):
    db = client[db_name]
    collection = db[collection_name]

    filter = { "_id": reference_id }

    document = collection.find_one(filter)

    value = document["customer_name"]
    doc = getDocById(value.database, value.collection, value.id)
    document["customer_name"] = doc["customer_fname"] + " " + doc["customer_mname"] + " " + doc["customer_lname"]
    
    value = document["project_name"]
    doc = getDocById(value.database, value.collection, value.id)
    document["project_name"] = doc["project_name"]

    if "broker_name" in document:
        if document["broker_name"] != "DIRECT":
            value = document["broker_name"]
            doc = getDocById(value.database, value.collection, value.id)
            document["broker_name"] = doc["broker_name"]

    return document

def getUserDetailsByName(username, db_name = "Settings", collection_name = "UserMaster"):
    db = client[db_name]
    collection = db[collection_name]

    filter = { "username": username }
    return collection.find_one(filter)    
        
def InsertData(db_name, collection_name, doc, files):
    db = InsertDoc(db_name, collection_name, doc)
    if files:
        for file in files:
            pass
            #UploadFile(db, file, doc)

def InsertDoc(db_name, collection_name, doc):
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_one(doc)
    return db

def UpdateData(db_name, collection_name, doc, files_dt):
    db = UpdateDoc(db_name, collection_name, doc)
    if files_dt:
        for files in files_dt:
            if files_dt[files]:
                UploadFile(db, files, files_dt[files], doc)

def UpdateDoc(db_name, collection_name, doc):
    db = client[db_name]
    collection = db[collection_name]
    filter = { "_id": doc["_id"] }

    for el in doc:
        update = { "$set": { el : doc[el] } }
        collection.update_one(filter, update)    
    return db
    
def UploadFile(db, docname, files, doc):
    for file in files:
        meta_data = {
            "_id": doc["_id"],
            "doc_name": docname
        }

        data = file.read()
        fs = GridFS(db)
        fs.put(data, filename=file.name, 
        metadata=meta_data)

def DownloadFile(db_name, filters):
    db = client[db_name]
    fs = GridFS(db)

    files = GetFiles(db_name, filters)     
    for file in files:
        _id = file["_id"]
        if _id._pid == 0:    
            return False

        data = fs.get(_id).read()
        path = "C:/Temp/" + file["filename"]
        output = open(path, "wb")
        output.write(data)
        output.close()
    return True

def ViewFile(db_name, filters):
    if DownloadFile(db_name, filters):
        fileName = filters[0]["filename"]
        path = "C:/Temp/" + fileName
        import os
        os.system('"' + path + '"')
        '''if os.path.exists('"' + path + '"'):
            os.remove('"' + path + '"')'''

def RemoveFile(db_name, filters):
    files = GetFiles(db_name, filters)
    db = client[db_name]

    for file in files:        
        fs = GridFS(db)
        fs.delete(file["_id"])
        break    
                                          
def GetFiles(db_name, filters):
    files_lst = []

    db = client[db_name]
    fs = GridFS(db)        
    files = db.fs.files.find({"$and": filters})

    for file in files:        
        files_lst.append(file)
    return files_lst