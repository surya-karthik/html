import openpyxl
import os
os.chdir("C:\tmp")

workbook= openpyxl.load_workbook('example.xlsx')
type(workbook)
