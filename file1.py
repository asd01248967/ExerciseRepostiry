#fruits = ['apple', 'cherry', 'pear', 'banana','strawberry']
fruits = ['apple']
dict = {'a':1, 'p':2, 'l':3, 'e':4, 'c':5, 'h':6, 'r':7, 'y':8, 'b':9, 'n':10, 's':11, 't':12, 'w':13}
for split in fruits:
    split_list = list(split)
    split_lenght = len(split)
    split_first = split_list[0]
    number = split_lenght - 1
    split_end = split_list[number]
    for total in range(0, split_lenght):
        print(dict[split_list[total]])
