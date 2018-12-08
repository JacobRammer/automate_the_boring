import openpyxl
import os


work_book = openpyxl.load_workbook("example.xlsx")

sheet = work_book.get_sheet_by_name("Sheet1")

cell = sheet["A1"]

print(str(cell.value))
