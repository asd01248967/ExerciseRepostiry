fruits = ['apple', 'cherry', 'pear', 'banana','strawberry']
for split in fruits:
    split_list = list(split)
    split_lenght = len(split)
    split_first = split_list[0]
    number = split_lenght - 1
    split_end = split_list[number]
    print(split_first)
    print(split_end)
    # for test in range(split_first, split_lenght):
    #     pass
    # else:
    #     pass


#list元素是從0開始的，所以長度要-1才會是最後的item