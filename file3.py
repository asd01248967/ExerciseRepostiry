import re
fruits = ['able@(adj.4)能;有能力的', 'above@(adj.5)上文的,前述的', 'adult@(adj.5)成年的;成熟的;色情的', 'afraid@(adj.6)害怕', 'all@(adj.3)所有的;全部', 'alone@(adj.5)單獨的;孤單的', 'angry@(adj.5)生氣的', 'another@(adj.7)另一個', 'any@(adj.3)任何的', 'back@(adj.4)後面的;拖欠的;過去的', 'bad@(adj.3)壞的']
list2 = ['able@(adj.4)能;有能力的']
for element in fruits:
    z = re.findall("^[^@]+", element)
    print(z)