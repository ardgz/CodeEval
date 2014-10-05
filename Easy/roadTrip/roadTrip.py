import sys
import re

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    numStrList = re.findall('\d+', line)
    numList = [int(num) for num in numStrList]
    numList.sort()

    diffList = []
    i = 1
    while i < len(numList):
        diffList.append( int(numList[i]) - int(numList[i-1]) )
        i += 1
    
    resultList = []
    resultList.append( str(numList[0]) )
    for num in diffList:
        resultList.append( str(num) )
    print ','.join(resultList)
        
