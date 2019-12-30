#!/usr/bin/env python
import time
tStart = time.time()
import openpyxl

book = openpyxl.load_workbook('C:\\Users\\Jasper\\Desktop\\7000.xlsx')

sheet = book.active

sheetlist = book.sheetnames

for sheettest in sheetlist:
    print(sheettest)

newlist = []

for number in range(1,2000):
    if sheet.cell(row=number, column=1).value == None:
        pass
    else:
        newlist.append(sheet.cell(row=number, column=1).value)


tEnd = time.time()
# print(len(newlist))
# print(newlist[1248])
# print("It cost %f sec" % (tEnd - tStart))
# print(tEnd - tStart)