import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    numList = line.split(',')
    uniqueList = []
    for num in numList:
        if uniqueList.count(num) == 0:
            uniqueList.append(num)
    result = ""
    for num in uniqueList:
        result += num + ','
    print result.strip(',')
