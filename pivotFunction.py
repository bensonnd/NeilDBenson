def listsPivot(pivotInput):
    """This function takes a list of lists, and rotates the 'grid' 90
degrees clockwise. ex. listToInvert[8,0] becomes listToInvert[0,0],
listToInvert[0,0] becomes listToInvert[0,5] in 5x9 'grid'."""
    masterList = []
    for i in range(len(grid[0])):	   #012 - indeces of the first row
        listHolder = []
        for j in range(len(grid)):	   #012345 - indeces of the first column
            tempVar = grid[j][i]       #invert the indeces
            listHolder.append(tempVar) #updates the list with the inverted value. Creates a list for each row.
        masterList.append(listHolder)  #adds each new inverted row to the masterList
    return masterList


grid = [['1', '2', 'A', '4', '5', '6'],
        ['1', '2', '3', 'F', '5', '6'],
        ['1', '43', '3', '4', '5', '6']]

print(listsPivot(grid))
