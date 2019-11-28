import openpyxl

path="D:\Python\TestData1.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook.active

for r in range(1,6):
    for c in range(1,5):
        sheet.cell(row=r,column=c).value="Welcome"


workbook.save(path)