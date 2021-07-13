# import requests
# import os
# import json
# from dotenv import load_dotenv
#
# load_dotenv()
#
# AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
# AIRTABLE_BASE_ID = os.environ.get('AIRTABLE_BASE_ID')
# AIRTABLE_TABLE_NAME = 'Resources'
# GET_ENDPOINT = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}?maxRecords=450&view=All%20Data%20%28by%20username%29'
#
# json_out = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'rMalaysiaFoodBank', 'rFoodBank', 'airtable',
#                         'Resources_150.json')
#
# # python requests
# headers = {
#     'Authorization': f'Bearer {AIRTABLE_API_KEY}',
#     'Content-Type': 'application/json'
# }
#
# r = requests.get(GET_ENDPOINT, headers=headers)
# data = r.json()
#
# print(data)
#
# with open(json_out, 'w') as f:
#     json.dump(data, f)
import pandas as pd
import requests
import os

import json
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
AIRTABLE_BASE_ID = os.environ.get('AIRTABLE_BASE_ID')
AIRTABLE_TABLE_NAME = 'Resources'

global offset
offset = '0'
result = []

while True:
    GET_ENDPOINT = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
    querystring = {
        "view": "All Data (by username)",
        "api_key": AIRTABLE_API_KEY,
        "offset": offset
    }

    try:
        response = requests.get(GET_ENDPOINT, params=querystring)
        response_Table = response.json()
        records = list(response_Table['records'])
        result.append(records)
        # print(f'record: {records[0]["id"]} , len: {len(records)} ')
        print(f'{response_Table} \n \n')

        try:
            offset = response_Table['offset']
            print(f'offset: {offset}')

        except Exception as ex:
            print(ex, offset)
            break

    except os.error as e:
        print(e)



print(len(result))
# json_out = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'rMalaysiaFoodBank', 'rFoodBank', 'airtable',
#                         'Resources_150.json')
#
# # python requests
# headers = {
#     'Authorization': f'Bearer {AIRTABLE_API_KEY}',
#     'Content-Type': 'application/json'
# }
#
# r = requests.get(GET_ENDPOINT, headers=headers)
# data = r.json()
#
# print(data)
#
# with open(json_out, 'w') as f:
#     json.dump(data, f)
