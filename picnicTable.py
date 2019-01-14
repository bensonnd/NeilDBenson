def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {
    'corn': 4,
    'apples': 126750,
    'cups': 4,
    'cookies': 820,
    'ice': 2}

def GetMaxDictLen(keyValues):
    return max(len(k) for k,v in keyValues.items()), max(len(str(v)) for k,v in keyValues.items())

leftTableWidth = GetMaxDictLen(picnicItems)[0] + 5
rightTableWidth = GetMaxDictLen(picnicItems)[1] + 3

printPicnic(picnicItems, leftTableWidth, rightTableWidth)