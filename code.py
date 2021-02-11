
import pandas as pd
from datetime import date, timedelta

#I'm using datetime so I can add the date to my file. It is usefull when you have to have to keep doing it every month 

# building the date for the file's name
first_day_current_month= date.today().replace(day=1)
last_day_prev_month = first_day_current_month - timedelta(days=1)
lastmonth_name = last_day_prev_month.strftime('%B')
# print(lastmonth_name)

now = date.today()
last_month = now.month-1 if now.month > 1 else 12

currentyear = now.year
if last_month > 11:
    currentyear = now.year - 1
elif last_month <12:
    currentyear = now.year

# print(currentyear)

# reading the csv
data = pd.read_csv(r'Path to your file.csv')
# US
# print(data)

split_column = data['column with the values to be used as a reference for splitting the files'].unique()
# print(split_value)



# splitting the files

for value in split_column:

    df = data[data['Distributor'] == value]
    output_file_name = "Name_your_file " + str(value) + "_" + str(lastmonth_name) + "_" + str(currentyear) + ".csv"
    df.to_csv(output_file_name)
