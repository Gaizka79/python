### En desuso
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

try:
    db_client = pymongo.MongoClient(os.getenv('MONGO_URI'), serverSelectionTimeoutMS=5000)
    #print(client.server_info())
    print("INFO:\t  Mongo DB konektatua OKkkkk.....")
except Exception:
    print("Unable to connect to the server.")