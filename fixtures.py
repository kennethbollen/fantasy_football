import datetime
import pandas as pd

#where the files are located
user_dir = ''
next_five = []
current_date = datetime.datetime.now()

print('setting up team fixtures...')
print()
df_fix = pd.read_csv(user_dir + '/fixtures_1819/csv')
df_fix.index = df_fix['Teams']

print('finding next five gameweek fixtures...')
print()
df_dates = pd.read_csv(user_dir + '/gw_cal.csv')
#convert date attribute from string to datetime
df_dates['Date'] = pd.to_datetime(df_dates['Date'], format='%d/%m/%Y')
#convert the index into datetime index
df_dates.index = df_dates['Date']
#remove the redundent dates attribute
del(df_dates['Date'])
#convert the gameweek numbers into strings to be used in .loc function
df_dates['Gameweek'] = df_dates['Gameweek'].astype('str')

#extract the gameweek numbers for the next five fixtures 
for i in range(len(df_dates)):
    if df_dates.index[i] > current_date:
        next_five.append(df_dates.iloc[i:i+6,1])
        break
    else:
        continue

#print the next five fixtures based on the current date
print(df_fix.loc[: , next_five[0][0]: next_five[0][-1]])
