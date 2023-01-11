import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
#db_client = MongoClient(os.getenv('MONGO_URI'), serverSelectionTimeoutMS=5000).MONGO_DB_NAME
try:
    db_client = pymongo.MongoClient(
        os.getenv('MONGO_URI'), 
        serverSelectionTimeoutMS=5000).MONGO_DB_NAME
    print("INFO:\t  Mongo DB konektatua OK.....")
except Exception:
    print("BAD NEWS:\t Unable to connect to the server.")
 

####*************************
""" def connect_db(url):
    try:
        db_client = pymongo.MongoClient(url, serverSelectionTimeoutMS=5000)
        print("INFO:\t  Mongo DB konektatua OK.....")
    except Exception:
        print("Unable to connect to the server.")
 """
