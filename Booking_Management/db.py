from pymongo import MongoClient
from gridfs import GridFS

#connection_string = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
connection_string = "mongodb+srv://admin:admin@cluster0.vlkpb.mongodb.net/test?authSource=admin&replicaSet=atlas-uip17y-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true&ssl_cert_reqs=CERT_NONE"

try:
    client = MongoClient(connection_string)
except:
    pass

def getNextId(dbName, collectionName):
    db = client[dbName]
    collection = db[collectionName]
    return collection.count() + 1

def verifyUser(username, password, dbName="Settings", collectionName="UserMaster"):
    return True

def getUsers(dbName="Settings", collectionName="UserMaster"):
    userDetails = []
    db = client[dbName]
    collection = db[collectionName]

    for x in collection.find({}):
        userDetails.append(x)
    return userDetails

def getProjects(dbName="Master", collectionName="Project"):
    projectDetails = []
    db = client[dbName]
    collection = db[collectionName]

    for x in collection.find({}):
        projectDetails.append(x)
    return projectDetails

def getProjectByName(project_name, dbName="Master", collectionName="Project"):
    projectDetails = []

    db = client[dbName]
    collection = db[collectionName]
    query = { "project_name": project_name }

    documents = collection.find(query)

    for document in documents:
        projectDetails.append(document)    
    return projectDetails[0]

def getOccupations(dbName="Master", collectionName="Customer"):
    occupations_list = []
    db = client[dbName]
    collection = db[collectionName]
    for item in collection.find({}):
        if item["occupation"] != "BUSINESS" and  item["occupation"] != "SELF-EMPLOYED" and item["occupation"] != "SERVICE" :
            occupations_list.append(item["occupation"])    
    return list(set(occupations_list))

def getCastes(dbName="Master", collectionName="Customer"):
    castes_list = []
    db = client[dbName]
    collection = db[collectionName]
    for item in collection.find({}):
        if item["caste"] != "SC" and  item["caste"] != "ST" :
            castes_list.append(item["caste"])    
    return list(set(castes_list))

def getCustomers(dbName="Master", collectionName="Customer"):
    customerDetails = []
    db = client[dbName]
    collection = db[collectionName]

    for x in collection.find({}):
        customerDetails.append(x)
    return customerDetails

def getCustomerByName(customer_name, dbName="Master", collectionName="Customer"):
    customerDetails = []
    fname = customer_name.split(' ')[0]
    mname = customer_name.split(' ')[1]
    lname = customer_name.split(' ')[2]

    db = client[dbName]
    collection = db[collectionName]
    query = [
        { "customer_fname": fname },
        { "customer_mname": mname },
        { "customer_lname": lname }]

    documents = collection.find({"$and": query})

    for document in documents:
        customerDetails.append(document)    
    return customerDetails[0]

def InsertData(dbName, collectionName, doc, files):
    db = InsertDoc(dbName, collectionName, doc)
    if files:
        for file in files:
            pass
            #UploadFile(db, file, doc)

def InsertDoc(dbName, collectionName, doc):
    db = client[dbName]
    collection = db[collectionName]
    collection.insert_one(doc)
    return db

def UpdateData(dbName, collectionName, doc, files_dt):
    db = UpdateDoc(dbName, collectionName, doc)
    if files_dt:
        for files in files_dt:
            if files_dt[files]:
                UploadFile(db, files_dt[files], doc)

def UpdateDoc(dbName, collectionName, doc):
    db = client[dbName]
    collection = db[collectionName]
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

def DownloadFile(dbName, fileName):    
    db = client[dbName]
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

def ViewFile(dbName, fileName):
    if DownloadFile(dbName, fileName):
        path = "C:/Temp/" + fileName
        import os
        os.system('"' + path + '"')

def GetFilesByMetaData(dbName, _id):
    files_lst = []
    db = client[dbName]
    fs = GridFS(db)
    files = db.fs.files.find({})
    for file in files:
        if file["metadata"]["_id"] == _id:
            files_lst.append(file)
    return files_lst