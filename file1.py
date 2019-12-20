fruits = ['apple', 'cherry', 'pear', 'banana','strawberry']
for split in fruits:
    split_list = list(split)
    split_lenght = len(split)
    split_first = split[0]
    split_end = split[split_lenght]
    print(split_list[0])
    # for test in range(split_first, split_lenght):
    #     pass
    # else:
    #     pass


#list元素是從0開始的，所以長度要-1才會是最後的item