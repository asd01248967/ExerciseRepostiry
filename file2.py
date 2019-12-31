#!/usr/bin/env python
# import time
# tStart = time.time()
import openpyxl

newlist = []

book = openpyxl.load_workbook('C:\\Users\\Jasper\\Desktop\\7000.xlsx')

#sheet = book.active
####################################

sheetlist = book.sheetnames

for s_name in sheetlist:
    sheet = book[s_name]
    #print(sheet.max_row)
    for number in range(1,sheet.max_row+1):
        if sheet.cell(row=number, column=1).value == None:
            pass
        else:
            newlist.append(sheet.cell(row=number, column=1).value)
    print(len(newlist))
    print(newlist[-1])

            

####################################
#tEnd = time.time()

# print(len(newlist))
# print(newlist[1248])
# print("It cost %f sec" % (tEnd - tStart))
# print(tEnd - tStart)