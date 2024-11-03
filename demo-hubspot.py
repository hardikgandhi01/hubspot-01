import os
from dotenv import load_dotenv
from hubspot import HubSpot
from hubspot.crm.contacts import ApiException

# Load environment variables from .env file
load_dotenv()

# Retrieve the access token from environment variable
access_token = os.getenv("HUBSPOT_API_KEY")
print(f"Access Token: {access_token}")  # For debugging

# Initialize the HubSpot client
api_client = HubSpot(access_token=access_token)

try:
    all_contacts = api_client.crm.contacts.get_all()
    print(all_contacts)
except ApiException as e:
    print(f"Exception when requesting contacts: {e}")
