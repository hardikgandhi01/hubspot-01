import datetime
from dateutil.relativedelta import relativedelta

def get_date_filter(period="last_week"):
    now = datetime.datetime.now(datetime.timezone.utc)
    
    if period == "last_week":
        # Get the date for one week ago
        start_date = now - datetime.timedelta(weeks=1)
    elif period == "last_month":
        # Get the date for one month ago
        start_date = now - relativedelta(months=1)
    elif period == "yesterday":
        # Get the date for yesterday
        start_date = now - datetime.timedelta(days=1)

    else:
        start_date = now
    
    return start_date
   

from hubspot import HubSpot
import os
from dotenv import load_dotenv

load_dotenv()


access_token = os.getenv("HUBSPOT_API_KEY")
print(f"Access Token: {access_token}")  

api_client = HubSpot(access_token= access_token)

from hubspot.crm.contacts import ApiException


all_contacts = None
try:
    # updated_since = get_date_filter("last_week")
    all_contacts = api_client.crm.contacts.get_all()
except ApiException as e:
    print("Exception when requesting contact by id: %s\n" % e) 
    
print(all_contacts)

# for contact in all_contacts:
#     print(contact, "\n")
    
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



uri = "mongodb+srv://developer:developerMongo@demo.y9gix.mongodb.net/?retryWrites=true&w=majority&appName=demo"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

DATABASE_NAME = 'hubspot-demo'
COLLECTION_NAME = 'contacts'

# Create MongoDB client

db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]


def insert_contact_to_mongo(contact_data):
    try:
        filter_query = {'id': contact_data['id']}
        
        # Perform update if the company exists, otherwise insert it
        collection.update_one(
            filter_query,     # Filter by company ID
            {'$set': contact_data},  # Update document with the new data
            upsert=True  # Insert if no document matches the filter
        )
        print(f"Upserted company with ID: {contact_data['id']}")
        # collection.insert_one(contact_data)
        # print(f"Inserted contact with ID: {contact_data['id']}")
    except Exception as e:
        print(f"Error inserting contact: {e}")
        
        
# insert code goes here
if all_contacts:
    for contact in all_contacts:
        # Assuming 'to_dict()' method converts the contact object to a dictionary
        contact_dict = contact.to_dict()
        insert_contact_to_mongo(contact_dict)
        print(f"contact inserted: {contact_dict}")

client.close()