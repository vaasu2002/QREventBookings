from QRBooking.Entry.database import connectToDatabase
from bson.objectid import ObjectId
import json

# from database import connectToDatabase

collection = connectToDatabase()

def verifyEntry(data: str):
    print(data)
    try:
        document = collection.find_one({"QRCode": data})
        print(document['name'])
    except:
        print("NOT FOUND")