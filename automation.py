#import openpyxl
#wb = openpyxl.load_workbook('example.xlsx')
#wb.get_sheet_names()
import openpyxl
import os

if __name__ == '__main__':
    os.chdir("X:\sravan")
    print (os.getcwd())
    wb = openpyxl.Workbook()
    #ws1 = wb.create_sheet("Mysheet")
    wb = openpyxl.load_workbook('example.xlsx')
    print(wb.get_sheet_names())
    sheet = wb.get_sheet_by_name('Sheet1')
    sheet['A1']
    for rowOfCellObjects in sheet['A1':'C3']:
         for cellObj in rowOfCellObjects:
             print(cellObj.coordinate, cellObj.value)
             print('--- END OF ROW ---')
