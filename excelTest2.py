import openpyxl

wb = openpyxl.load_workbook('./file/Marvel.xlsx')

sheet = wb['new title']
sheetname = wb.sheetnames

A1_cell = sheet['A1']
A1_value = A1_cell.value
print(A1_value)