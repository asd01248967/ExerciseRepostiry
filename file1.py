import pandas as pd
from collections import OrderedDict
dataframe = pd.read_excel(io='C:\\Users\\Jasper\\Desktop\\10.xlsx',sheet_name="1級",header=None)
print(dataframe)


vocabulary= list(dataframe.items())

#fruits = ['apple', 'cherry', 'pear', 'banana', 'strawberry', 'whiskey', 'intellect', 'chimpanzee', 'grape', 'attitude']
#dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,}
#match = []


for split2 in vocabulary:
    print(len(split2))

# for split in fruits:
#     print(type(split))
#     split_list = list(split)
#     split_lenght = len(split)
#     a = 0
#     for total in range(0, split_lenght):
#         a += dict[split_list[total]]
#     if a == 100:
#         match.append(split)
# print(match)