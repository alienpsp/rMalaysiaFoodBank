import time
import webbrowser

from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

dataProjectSheets = client.open(r'r/Malaysia Data Project').worksheet('Input Queue')


for i in range(322):
    flag_check = dataProjectSheets.cell(i+12, 2).value # start from row after done
    comment_check = dataProjectSheets.cell(i+12, 3).value
    url_check = dataProjectSheets.cell(i+12, 5).value
    if flag_check != 'TRUE' and comment_check is None:
        webbrowser.open(f'{dataProjectSheets.cell(i + 12, 5).value}', new=2)
        time.sleep(1)
        print('check again')
    else:
        print(f'row: {i+12}, {flag_check}, {comment_check}, {url_check}')
        time.sleep(1)



'''
Write cell
dataProjectSheets.update_cell(7, 6, 'Hello World')  # (row, column, value)

Read cell
dataProjectSheets.cell(i, 2).value # use i because of loop, and 2nd column
'''
