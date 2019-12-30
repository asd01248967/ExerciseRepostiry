# import pandas as pd
# dataframe = pd.read_excel(io='C:\\Users\\Jasper\\Desktop\\10.xlsx',sheet_name=None,header=None)
# content = list(dataframe)
# print(content)

#匯入openpyxl套件庫
from openpyxl import load_workbook
#透過load_workbook讀取xlsx檔案為wb
wb = load_workbook(filename="C:\\Users\\Jasper\\Desktop\\10.xlsx")
#設定sheets為str內容元素類型的list，類似['1級', '2級', '3級', '4級', '5級', '6級']
sheets = (wb.sheetnames)
#取得頁籤的內容
ws = wb[sheets[0]]

print(ws)
print(type(ws))