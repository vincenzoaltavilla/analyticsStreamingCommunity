from get_top10 import *
from openpyxl import load_workbook
import pandas as pd
from datetime import date
import os

today = str(date.today())

# Specify Excel file name and sheet name
excel_file = 'top10.xlsx'
sheet_name = 'TOP10'

if os.path.exists(excel_file):
    df = pd.read_excel(excel_file, sheet_name=sheet_name, index_col=0)
    if today not in df.columns:
        top10 = get_top10()
        df[today] = top10
else:
    top10 = get_top10()
    df = pd.DataFrame(top10, index=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'], columns=[today])

# Write DataFrame to Excel
df.to_excel(excel_file, sheet_name=sheet_name)

print(len(df.columns))

wb = load_workbook(excel_file)
ws = wb[sheet_name]
alphabet = 'BCDEFGHIJKLMNOPQRSTUVWXYZ'

for letter in alphabet:
    try:
        length = len(ws[letter + '2'].value)
    except:
        break

    max_width = 0

    for row_number in range(1, ws.max_row + 1):
        if len(ws[f'{letter}{row_number}'].value) > max_width:
            max_width = len(ws[f'{letter}{row_number}'].value)

    ws.column_dimensions[letter].width = max_width + 1

wb.save(excel_file)