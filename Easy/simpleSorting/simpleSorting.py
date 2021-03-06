import sys

lines = file(sys.argv[1], 'r')

def sort(numList):
    i = 0
    while i < len(numList):
        minValue = numList[i]
        minIndex = None
        j = i + 1
        while j < len(numList):
            if numList[j] < minValue:
                minValue = numList[j]
                minIndex = j
            j += 1
        if minIndex != None:
            numList[i], numList[minIndex] = numList[minIndex], numList[i]
        i += 1
        
    return numList

for line in lines:
    line = line.strip() # Remove newline char
    #numList = ["{0:.3f}".format(float(i)) for i in line.split(' ')]
    numList = [float(i) for i in line.split(' ')]
    numList = sort(numList)
    
    resultLine = ""
    for num in numList:
        resultLine += "{:.3f}".format(num) + " "
    print resultLine.strip()
