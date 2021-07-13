import boto3
import os
from naas_drivers import airtable
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime


load_dotenv()

pd.set_option('display.width', 980)
pd.set_option('display.max_colwidth', 180)
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_column', 200)
pd.set_option('display.float_format', '{:,.2f}'.format)

AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
AIRTABLE_BASE_ID = os.environ.get('AIRTABLE_BASE_ID')
S3_ACCESS_KEY = os.environ.get('S3_ACCESS_KEY')
S3_SECRET = os.environ.get('S3_SECRET')
AIRTABLE_TABLE_NAME = 'Resources'
AIRTABLE_VIEW = 'All Data (by username)'


today = datetime.today()
Day = f"{today.strftime('%d')}"
Month = f"{today.strftime('%m')}"
Year = f"{today.strftime('%Y')}"
Time = f"{today.strftime('%H')}{today.strftime('%M')}{today.strftime('%S')}"
io_key = f'rMsia_{Day}{Month}{Year}_{Time}'

""" Airtable Part """
json_out = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'rMalaysiaFoodBank', 'rFoodBank', 'airtable',
                        'pandas.json')


data = airtable.connect(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME).get(view=AIRTABLE_VIEW)
df = pd.DataFrame(data)
print(df.shape)

df.reset_index(drop=True, inplace=True)
df.drop(['createdTime'], axis=1, inplace=True)

# df.to_json(json_out, orient='split', date_format='iso')


# """ AWS Part """
# client = boto3.client(
#     's3',
#     aws_access_key_id = S3_ACCESS_KEY,
#     aws_secret_access_key=S3_SECRET
# )
#
# for file in os.listdir():
#     if 'pandas.json' in file:
#         bucket = 'r-malaysia-white-flag-project'
#         key = f'input/{io_key}.json'
#         client.upload_file(file, bucket, key)
#         print(f'uploaded to: {bucket}/{key}')
