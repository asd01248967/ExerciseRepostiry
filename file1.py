import pandas as pd
dataframe = pd.read_excel(io='C:\\Users\\Jasper\\Desktop\\Book1.xlsx',sheet_name=None,header=None)
print(type(dataframe))
# fruits = ['apple', 'cherry', 'pear', 'banana', 'strawberry', 'whiskey', 'intellect', 'chimpanzee', 'grape', 'attitude']
#dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,}
#match = []

# for split in dataframe:
#     print(split)

# for split in fruits:
#     split_list = list(split)
#     split_lenght = len(split)
#     a = 0
#     for total in range(0, split_lenght):
#         a += dict[split_list[total]]
#     if a == 100:
#         match.append(split)
# print(match)