listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
print(listOfElems)
print(type(listOfElems))
print(len(listOfElems))

test = set(listOfElems)

print(test)
print(type(test))
print(len(test))

if len(listOfElems) == len(test):
    print('No duplicates found in list')
else:
    print('Yes, list contains duplicates')
# len1 = len(listOfElems)
# len2 = len(test)



# def checkIfDuplicates_1(listOfElems):
# #''' Check if given list contains any duplicates '''
# if len1 == len2:
#     print('yes')
# else:
#     print('no')


# result = checkIfDuplicates_1(listOfElems)

# if result:
#     print('Yes, list contains duplicates')
# else:
#     print('No duplicates found in list')    