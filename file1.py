fruits = ['apple', 'cherry', 'pear', 'banana','strawberry']
dict = {'a':1, 'p':2, 'l':3, 'e':4, 'c':5, 'h':6, 'r':7, 'y':8, 'b':9, 'n':10, 's':11, 't':12, 'w':13}
for split in fruits:
    split_list = list(split)
    split_lenght = len(split)
    #split_first = split_list[0]
    a = 0
    for total in range(0, split_lenght):
        a += dict[split_list[total]]
    print(a)