from get_top10 import *
import pandas as pd
from openpyxl import load_workbook

top10 = get_top10()

df = pd.DataFrame(top10, index=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'], columns=["Top10"])

# Specify Excel file name
excel_file = "top10.xlsx"

# Write DataFrame to Excel
df.to_excel(excel_file, sheet_name="TOP10")

wb = load_workbook(excel_file)
ws = wb["TOP10"]

alphabet = 'BCDEFGHIJKLMNOPQRSTUVWXYZ'

for letter in alphabet:

    try:
        length = len(ws[letter + '1'].value)
    except:
        break

    max_width = 0

    for row_number in range(1, ws.max_row + 1):
        if len(ws[f'{letter}{row_number}'].value) > max_width:
            max_width = len(ws[f'{letter}{row_number}'].value)

    ws.column_dimensions[letter].width = max_width + 1

wb.save(excel_file)