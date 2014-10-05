import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    elementsList = line.split(',')
    N = len(elementsList) / 2
    
    uniqueList = []
    uniqueCounts = []
    result = None
    
    for element in elementsList:
        if element not in uniqueList:
            uniqueList.append(element)

    for element in uniqueList:
        if elementsList.count(element) > N:
            result = element
            break
    
    #print uniqueList

    if result == None:
        print "None"
    else:
        print result
