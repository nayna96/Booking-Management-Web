from pymongo import MongoClient
from gridfs import GridFS

connection_string = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
#connection_string = "mongodb+srv://admin:admin@cluster0.vlkpb.mongodb.net/test?authSource=admin&replicaSet=atlas-uip17y-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true&ssl_cert_reqs=CERT_NONE"

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
    return collection.count() + 1

def verifyUser(username, password, db_name="Settings", collection_name="UserMaster"):
    return True

def getDetails(db_name, collection_name):
    details = []
    db = client[db_name]
    collection = db[collection_name]

    for x in collection.find({}):
        details.append(x)
    return details

#Project Master
def getProjectsList(db_name="Master", collection_name="Project"):
    lst = []

    db = client[db_name]
    collection = db[collection_name]

    filter = {}
    fields = {"project_name":1, "_id":0}

    documents = collection.find(filter, fields)

    for document in documents:
        lst.append(document["project_name"])

    return lst

def getProjectByName(project_name, db_name="Master", collection_name="Project"):
    projectDetails = []

    db = client[db_name]
    collection = db[collection_name]

    filter = { "project_name": project_name }
    documents = collection.find(filter)

    for document in documents:
        projectDetails.append(document)

    return projectDetails[0]

#Block Master
def getBlockDetailsByProject(project_name, db_name="Master", collection_name="Block"):
    lst = []

    db = client[db_name]
    collection = db[collection_name]

    filter = { "project_name": project_name }
    documents = collection.find(filter)

    for document in documents:
        lst.append(document)
    
    return lst[0]

def getBlocksListByProject(project_name, db_name="Master", collection_name="Block"):
    blocks_list = []

    db = client[db_name]
    collection = db[collection_name]

    filter = { "project_name": project_name }
    documents = collection.find(filter)

    for document in documents:
        blocks = document["blocks"]
        for block in blocks:
            blocks_list.append(block["block_name"])

    return list(set(blocks_list))
        
def getFloorsListByBlock(project_name, block_name, 
                        db_name="Master", collection_name="Block"):
    floors_list = []

    db = client[db_name]
    collection = db[collection_name]

    filter = { "project_name": project_name }
    documents = collection.find(filter)

    for document in documents:
        blocks = document["blocks"]
        for block in blocks:
            if block["block_name"] == block_name:
                floors_list.append(block["floor_no"])

    return floors_list

def getFlatDetailsByFloor(project_name, block_name, floor_no, 
                        db_name="Master", collection_name="Flat"):
    
    lst = []

    db = client[db_name]
    collection = db[collection_name]

    filter = [
        { "project_name": project_name },
        { "block_name":block_name },
        { "floor_no": floor_no }
    ]
    documents = collection.find({"$and": filter})

    for document in documents:
        lst.append(document)
    
    if len(lst) > 0:
        return lst[0]
    else:
        return lst

def getFlatsListByFloorNo(project_name, block_name, floor_no, share_type):
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

def updateFlatStatus(project_name, block_name, floor_no, flat_no, flat_status,
    db_name="Master", collection_name="Flat"):

    db = client[db_name]
    collection = db[collection_name]

    filter = {"$and": 
    [
        { "project_name": project_name },
        { "block_name":block_name },
        { "floor_no": floor_no }
    ]}

    #collection.find({"$and": filter})

    update = { "$set": { "flats.$[f].flat_status" : flat_status } }
    array_filters=[{"f.flat_no" : { "$in" : flat_no }}]

    collection.update_one(filter, update, array_filters=array_filters)
    
'''def getFlatsByProjectName(db_name, collection_name, project_name):
    db = client[db_name]
    collection = db[collection_name]
    result = collection.Find(a => a["project_name"] == projectName)

    for item in result.ToEnumerable():
        entry.Add(item.ToDictionary())
    
    return entry

def getNoFlatsByFloor(db_name, collection_name, 
    project_name, block_name, floor_no):

    db = client[db_name]
    collection = db[collection_name]

    var projectfilter = Builders<BsonDocument>.Filter.Eq("project_name", projectName);
    List<BsonDocument> lst = collection.Find(projectfilter).ToList();

    if (lst.Count > 0)
    {
        BsonArray array = (BsonArray)lst[0]["blocks"];
        no_flats = array.FirstOrDefault(l => l["block_name"] == blockName && l["floor_no"] == floorNo)["no_flats"];
    }

    return no_flats;
} 
'''

#Customer Master
def getOccupations(db_name="Master", collection_name="Customer"):
    occupations_list = []
    db = client[db_name]
    collection = db[collection_name]
    for item in collection.find({}):
        if item["occupation"] != "BUSINESS" and  item["occupation"] != "SELF-EMPLOYED" and item["occupation"] != "SERVICE" :
            occupations_list.append(item["occupation"])    
    return list(set(occupations_list))

def getCastes(db_name="Master", collection_name="Customer"):
    castes_list = []
    db = client[db_name]
    collection = db[collection_name]
    for item in collection.find({}):
        if item["caste"] != "SC" and  item["caste"] != "ST" :
            castes_list.append(item["caste"])    
    return list(set(castes_list))

def getCustomersList(db_name="Master", collection_name="Customer"):
    lst = []

    db = client[db_name]
    collection = db[collection_name]

    filter = {}

    documents = collection.find(filter)

    for document in documents:
        lst.append(document["customer_fname"] + " " + document["customer_mname"] + " " + document["customer_lname"])

    return lst

def getCustomerByName(customer_name, db_name="Master", collection_name="Customer"):
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

    documents = collection.find({"$and": filter})

    for document in documents:
        customerDetails.append(document)    
    return customerDetails[0]

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

def getBankDetailsByName(bank_name, db_name="Master", collection_name="Bank"):
    bankDetails = []

    db = client[db_name]
    collection = db[collection_name]

    filter = { "bank_name": bank_name }
    documents = collection.find(filter)

    for document in documents:
        bankDetails.append(document)

    return bankDetails[0]

def updateBankDetails(approved_banks, project_name, 
                        db_name = "Master", collection_name = "Bank"):        
    db = client[db_name]
    collection = db[collection_name]

    #remove selected project from all banks
    lst = list(collection.find({}))
    for el in lst:
        array = el["approved_projects"]            
            
        doc = { "name" : project_name }
        if doc in array:    
            array.remove(doc)

        filter = { "bank_name": el["bank_name"] }
        update = { "$set": { "approved_projects" : array } }
        collection.update_one(filter, update)

    #add project name in required bank
    for approved_bank in approved_banks:
        if len(approved_bank) > 0:
            filter1 = { "short_bank_name" : approved_bank }
            array1 = list(collection.find(filter1))[0]["approved_projects"]
           
            doc1 = { "name" : project_name }
            array1.append(doc1)            
            
            update1 = { "$set": { "approved_projects" : array1 } }
            collection.update_one(filter1, update1)

def getBookingEntryByReferenceId(reference_id, db_name = "Transaction", collection_name = "BookingEntry"):
    entry = []

    db = client[db_name]
    collection = db[collection_name]

    filter = { "_id": reference_id }
    documents = collection.find(filter)

    for document in documents:
        entry.append(document)

    return entry[0]    
        
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
                UploadFile(db, files_dt[files], doc)

def UpdateDoc(db_name, collection_name, doc):
    db = client[db_name]
    collection = db[collection_name]
    filter = { "_id": doc["_id"] }

    for el in doc:
        update = { "$set": { el : doc[el] } }
        collection.update_one(filter, update)    
    return db
    
def UploadFile(db, files, doc):
    for file in files:
        meta_data = {
            "_id": doc["_id"],
            "doc_name": file.field_name
        }

        data = file.read()
        fs = GridFS(db)
        fs.put(data, filename=file.name, 
        metadata=meta_data)

def DownloadFile(db_name, fileName):    
    db = client[db_name]
    fs = GridFS(db)
    filter = { "filename": fileName }    
    file = db.fs.files.find_one(filter)
    _id = file["_id"]
    if _id._pid == 0:    
        return False

    data = fs.get(_id).read()
    path = "C:/Temp/" + file["filename"]
    output = open(path, "wb")
    output.write(data)
    output.close()
    return True

def ViewFile(db_name, fileName):
    if DownloadFile(db_name, fileName):
        path = "C:/Temp/" + fileName
        import os
        os.system('"' + path + '"')

def GetFilesByMetaData(db_name, _id):
    files_lst = []
    db = client[db_name]
    fs = GridFS(db)
    files = db.fs.files.find({})
    for file in files:
        if file["metadata"]["_id"] == _id:
            files_lst.append(file)
    return files_lst