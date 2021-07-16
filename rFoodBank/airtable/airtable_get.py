import os
import json
import boto3
import requests
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
        # print(f'{response_Table} \n \n')

        try:
            offset = response_Table['offset']
            print(f'offset: {offset}')

        except Exception as ex:
            print(ex, offset)
            break

    except os.error as e:
        print(e)

# print(len(result))

sd = bytes(json.dumps().encode('UTF-8'))

# json_out = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'rMalaysiaFoodBank', 'rFoodBank', 'airtable',
#                         'rWhiteFlagProject.json')

# with open(json_out, 'w') as f:
#     json.dump(result, f)

# S3_ACCESS_KEY = os.environ.get('S3_ACCESS_KEY')
# S3_SECRET = os.environ.get('S3_SECRET')
# client = boto3.client(
#     's3',
#     aws_access_key_id=S3_ACCESS_KEY,
#     aws_secret_access_key=S3_SECRET
# )
#
# for file in os.listdir():
#     if 'rWhiteFlagProject.json' in file:
#         bucket = 'whiteflagproject'
#         key = f'rWhiteFlagProject.json'
#         client.upload_file(file, bucket, key)
#         print(f'uploaded to: {bucket}/{key}')
