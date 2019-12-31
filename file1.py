listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
test = set(listOfElems)
len1 = len(listOfElems)
len2 = len(test)



def checkIfDuplicates_1(listOfElems):
#''' Check if given list contains any duplicates '''
if len1 == len2:
    print('yes')
else:
    print('no')


result = checkIfDuplicates_1(listOfElems)

if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')    