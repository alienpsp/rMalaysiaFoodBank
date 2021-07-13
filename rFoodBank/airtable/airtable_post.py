import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
AIRTABLE_BASE_ID = os.environ.get('AIRTABLE_BASE_ID')
AIRTABLE_TABLE_NAME = 'Resources'
POST_ENDPOINT = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

load_csv = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'rMalaysiaFoodBank', 'rFoodBank', 'airtable',
                        'raw_input.csv')

# TODO: add in pd read_csv and loop data for post

# python requests
headers = {
    'Authorization': f'Bearer {AIRTABLE_API_KEY}',
    'Content-Type': 'application/json'
}

data = {
  "records": [
    {
      "fields": {
        "Resource Name": "",
        "Launch URL": "",
        "Launch URL Languge": [
          ""
        ],
        "Organisation Name": "",
        "Launch URL Date": "",
        "Resources Offered": [
          "",
          ""
        ],
        "How to Access": [
          ""
        ],
        "Operating Hours": "",
        "Freeform Address": "",
        "Postcode": ,
        "State/WP": "",
        "City": "",
        "GPS Coordinates": "",
        "Contact Method(s)": [
          ""
        ],
        "Contact Number(s)": "",
        "Latest Social Media Post URL": "",
        "Latest Social Media Post Date": "",
        "Your username!": "",
        "Info Source": ""
      }
    }
  ]
}

# TODO: add loop to request.post
r = requests.post(GET_ENDPOINT, data=data, headers=headers)



'''
RATE LIMITS
The API is limited to 5 requests per second per base. If you exceed this rate, you will receive a 429 status code and will need to wait 30 seconds before subsequent requests will succeed.

The official JavaScript client has built-in retry logic.

If you anticipate a higher read volume, we recommend using a caching proxy. This rate limit is the same for all plans and increased limits are not currently available.


'''