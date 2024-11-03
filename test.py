from pymongo import MongoClient
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_url = os.getenv("MONGODB_URL")

# Connect to MongoDB
client = MongoClient(
    mongodb_url
)  
db = client['hubspot-demo']  
collection = db['companies']  

# Helper function to get entries updated on a specific day
def get_entries_updated_on(date):
    # Start and end of the day (midnight to midnight)
    start_of_day = datetime.combine(date, datetime.min.time())
    end_of_day = start_of_day + timedelta(days=1)
    
    query = {
        "updated_at": {
            "$gte": start_of_day,  # Greater than or equal to the start of the day
            "$lt": end_of_day      # Less than the end of the day
        }
    }
    return list(collection.find(query))

# Get yesterday's date
yesterday = datetime.now() - timedelta(days=1)

# Fetch entries updated yesterday
entries_yesterday = get_entries_updated_on(yesterday)
print(f"Entries updated yesterday: {entries_yesterday}")

# Fetch entries updated within the last week
one_week_ago = datetime.now() - timedelta(weeks=1)
four_weeks_ago = datetime.now() - timedelta(weeks=4)


entries_last_week = collection.find({
    "updated_at": {
        "$gte": one_week_ago,  # Greater than or equal to one week ago
        "$lt": datetime.now()  # Less than now
    }
})
print(f"Entries updated last week: {list(entries_last_week)}")

# Fetch entries updated within the last two weeks
entries_last_four_weeks = collection.find({
    "updated_at": {
        "$gte": four_weeks_ago,  # Greater than or equal to two weeks ago
        "$lt": datetime.now()    # Less than now
    }
})
print(f"Entries updated in last four weeks: {list(entries_last_four_weeks)}")