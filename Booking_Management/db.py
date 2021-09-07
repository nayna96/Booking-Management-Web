from pymongo import MongoClient

connection_string = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
connection_string = "mongodb+srv://admin:admin@cluster0.vlkpb.mongodb.net/test?authSource=admin&replicaSet=atlas-uip17y-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"

try:
    client = MongoClient(connection_string)
except:
    pass

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
    return None

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
    myquery = [
        { "customer_fname": fname },
        { "customer_mname": mname },
        { "customer_lname": lname }]

    documents = collection.find({"$and": myquery})

    for document in documents:
        customerDetails.append(document)    
    return customerDetails[0]

def InsertData(dbName, collectionName, doc):
    db = client[dbName]
    collection = db[collectionName]
    collection.insert_one(doc)

