import sys

lines = file(sys.argv[1], 'r')

def majorElementExists(uniqueList, uniqueCounts, N):
    i = 0
    while i < len(uniqueCounts):
        if uniqueCounts[i] > N:
            return uniqueList[i]
        i += 1
    return -1

for line in lines:
    line = line.strip() # Remove newline char
    elementsList = line.split(',')
    N = len(elementsList) / 2
    
    uniqueList = []
    uniqueCounts = []
    result = None
    for element in elementsList:
        if uniqueList.count(element) == 0:
            uniqueList.append(element)
            uniqueCounts.append(1)
        else:
            index = uniqueList.index(element)
            uniqueCounts[index] += 1
        
        result = majorElementExists(uniqueList, uniqueCounts, N)
        if result != -1:
            break
        #print "List:", uniqueList
        #print "Counts:", uniqueCounts
    print "List:", uniqueList
    print "Counts:", uniqueCounts

    if result == -1:
        print "None"
    else:
        print result
