from get_top10 import *
from openpyxl import load_workbook
import pandas as pd
from datetime import date
import os

today = str(date.today())
# today = '2024-03-23'

excel_file = 'top10.xlsx'
sheet_name = 'TOP10'

# If daily top10 was already stored, don't do anything, else append it or store it if the file doesn't exist
if os.path.exists(excel_file):
    df = pd.read_excel(excel_file, sheet_name=sheet_name, index_col=0)
    if today not in df.index:
        df.loc[today] = get_top10()
else:
    df = pd.DataFrame(index=[today], columns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    df.loc[today] = get_top10()

# Write DataFrame to Excel
df.to_excel(excel_file, sheet_name=sheet_name)

# Define common column width
wb = load_workbook(excel_file)
ws = wb[sheet_name]
columns = "ABCDEFGHIJK"
for column in columns:
    ws.column_dimensions[column].width = 20
wb.save(excel_file)
wb.close()

# print(df.to_string(index=False))                                            # all dataframe
# print(df.loc[['2024-03-23', '2024-03-12'], 3].to_string(index=False))       # n-th position in day(s) x
# print(df[[1, 2]])                                                           # n-th position(s)
# print(df.loc[['2024-03-12', '2024-03-23']].to_string())                     # full day X and/or Y (if just one day, with just one [] column print)
# print(df[[3, 4]].loc[['2024-03-23', '2024-03-12']].to_string(index=False))  # n-th position(s) in day(s) x