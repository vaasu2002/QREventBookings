import os
from util.internetWorking import connect
import pymongo
from pymongo.errors import ConnectionFailure
# from exception import custonException
from ensure import ensure_annotations
# from logger import logger

# DATABASE_NAME = os.getenv("DATABASE_NAME")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")
DATABASE_NAME = 'QREventBooking'
COLLECTION_NAME = 'Test1'

@ensure_annotations
def connectToDatabase()->pymongo.collection.Collection:
    try:
        online = False
        if connect():
            # MONGODB_URL = os.getenv("MONGODB_URL")
            MONGODB_URL = "mongodb+srv://vaasu:pcvaasu9dps@cluster0.wydi0u7.mongodb.net/13digital?retryWrites=true&w=majority"
            online = True
        else:
            MONGODB_URL = "mongodb://localhost:27017/"
        
        client = pymongo.MongoClient(MONGODB_URL)
        collection = None
        print(f"Connected to database. Online: {online}")

        if COLLECTION_NAME in client[DATABASE_NAME].list_collection_names():
                collection = client[DATABASE_NAME][COLLECTION_NAME]        
            
        else:
            print("Collection does not exist")

            # raise custonException(
            #         f"Collection object is None. Check if the collection {COLLECTION_NAME} exists in the database {DATABASE_NAME}"
            #     )

        print(f"Collection {COLLECTION_NAME} found in database {DATABASE_NAME}")

        if collection is not None:
            collection.create_index('regNo', unique=True)
            return collection
        
    except:
        print("Failed to connect to database")