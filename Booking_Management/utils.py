from pymongo import MongoClient

host = "localhost:27017"
username = ""
password = ""
#host = "cluster0.vlkpb.mongodb.net"
#username = "admin"
#password = "admin"

def get_db_handle(db_name):
    client = MongoClient(host=host,                    
                         username=username,
                         password=password
                        )
    db_handle = client[db_name]
    return db_handle, client

def get_collection_handle(db_handle, collection_name):
    return db_handle[collection_name]