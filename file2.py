#!/usr/bin/env python
import time
tStart = time.time()
import openpyxl

book = openpyxl.load_workbook('C:\\Users\\Jasper\\Desktop\\100.xlsx')

sheet = book.active

newlist = []

for number in range(1,10):
    if sheet.cell(row=number, column=1).value == None:
        pass
    else:
        newlist.append(sheet.cell(row=number, column=1).value)
        print(newlist)

tEnd = time.time()
print("It cost %f sec" % (tEnd - tStart))
print(tEnd - tStart)