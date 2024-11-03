import datetime
from dateutil.relativedelta import relativedelta
import os
from dotenv import load_dotenv
from hubspot import HubSpot
from hubspot.crm.companies import ApiException
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Load environment variables from .env file
load_dotenv()

# Function to get date filter
def get_date_filter(period="last_week"):
    now = datetime.datetime.now(datetime.timezone.utc)
    if period == "last_week":
        start_date = now - datetime.timedelta(weeks=1)
    elif period == "last_month":
        start_date = now - relativedelta(months=1)
    elif period == "yesterday":
        start_date = now - datetime.timedelta(days=1)
    else:
        start_date = now
    return start_date

# HubSpot setup
access_token = os.getenv("HUBSPOT_API_KEY")
print(f"Access Token: {access_token}")  # For debugging
api_client = HubSpot(access_token=access_token)

# MongoDB setup
uri = "mongodb+srv://developer:developerMongo@demo.y9gix.mongodb.net/?retryWrites=true&w=majority&appName=demo"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['hubspot-demo']
collection = db['companies']  # Use a collection specifically for companies

# Function to insert company data into MongoDB
def insert_company_to_mongo(company_data):
    try:
        filter_query = {'id': company_data['id']}
        collection.update_one(
            filter_query,       # Filter by company ID
            {'$set': company_data},  # Update with new data
            upsert=True         # Insert if no document matches the filter
        )
        # print(f"Upserted company with ID: {company_data['id']}")
    except Exception as e:
        print(f"Error inserting company: {e}")

# Fetch all companies from HubSpot API
all_companies = None
try:
    all_companies = api_client.crm.companies.get_all()
except ApiException as e:
    print(f"Exception when requesting companies: {e}")

# Insert each company into MongoDB
if all_companies:
    for company in all_companies:
        company_dict = company.to_dict()  # Convert the company object to a dictionary
        insert_company_to_mongo(company_dict)
        print(f"Company inserted: {company_dict}")
else:
    print("No companies retrieved from HubSpot API.")

# Close MongoDB client connection
client.close()
