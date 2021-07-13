import os
import time
import numpy as np
import pandas as pd

T1 = time.time()
print('Preparing...')

pd.set_option('display.width', 980)
pd.set_option('display.max_colwidth', 180)
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_column', 20)
pd.set_option('display.float_format', '{:,.2f}'.format)

input_file = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'rMalaysiaFoodBank', 'local',
                          'r_Malaysia Data Project.xlsx')
output_file = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'rMalaysiaFoodBank', 'local',
                          'r_Malaysia_Data_Project.xlsx')

workDF1 = pd.read_excel(input_file, sheet_name='Input Queue', skiprows=10)

workDF1['comment_f'] = pd.isnull(workDF1['Questions, Comments'])

workDF1 = workDF1[['Done?', 'Questions, Comments', 'Name', 'Link to Foodbank', 'Language(s)', 'comment_f']]

FB_df = workDF1.rename(
    columns={'Done?': 'done', 'Questions, Comments': 'comment', 'Name': 'name', 'Link to Foodbank': 'link',
             'Language(s)': 'language'})

FB_df.done.fillna(0, inplace=True)
FB_df['done'] = FB_df.done.astype(np.int64)

FB_wdf = FB_df

print(FB_wdf.head(3))
print('\n')
print('\n')

# FB_wdf.to_excel(output_file, index=False)

for i in FB_wdf.iterrows():
    # print(i[0]) # index
    flag_check = f'{i[1][0]}'
    comment_check = f'{i[1][5]}'
    url_check = f'{i[1][3]}'
    if flag_check == '0' and comment_check == 'True':
        print(url_check)
        time.sleep(0.5)
        key = input('s for skip, c for chinese, m for malay, i for indian, e for english, p for private')
        if key == 's':
            continue
        elif key == 'c':
            FB_wdf.at[i[0], 'language'] = 'Chinese'
            print('\n')
            print(FB_wdf.loc[[i[0]]])
            FB_wdf.to_excel(output_file)
            continue
        elif key == 'm':
            FB_wdf.at[i[0], 'language'] = 'Malay'
            print('\n')
            print(FB_wdf.loc[[i[0]]])
            FB_wdf.to_excel(output_file)
            continue
        elif key == 'i':
            FB_wdf.at[i[0], 'language'] = 'Indian'
            print('\n')
            print(FB_wdf.loc[[i[0]]])
            FB_wdf.to_excel(output_file)
            continue
        elif key == 'e':
            FB_wdf.at[i[0], 'language'] = 'English'
            print('\n')
            print(FB_wdf.loc[[i[0]]])
            FB_wdf.to_excel(output_file)
            continue
        elif key == 'p':
            FB_wdf.at[i[0], 'language'] = 'Private'
            print('\n')
            print(FB_wdf.loc[[i[0]]])
            FB_wdf.to_excel(output_file)
            continue
    else:
        print(f'row: {i[0]}, {flag_check}, {comment_check}')
        time.sleep(0.5)

FB_wdf.to_excel(output_file)



'''
# i[1][0] # done
# i[1][1] # comment
# i[1][2] # name
# i[1][3] # link 
# i[1][4] # language
# i[1][5] # comment_f

'''