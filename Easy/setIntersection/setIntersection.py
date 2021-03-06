import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    leftStr, rightStr = line.split(';')
    leftStrList = leftStr.split(',')
    rightStrList = rightStr.split(',')
    leftList = [int(string) for string in leftStrList]
    rightList = [int(string) for string in rightStrList]
    
    intersection = list( set(leftList) & set(rightList) )
    intersection.sort()
    print ','.join(str(s) for s in intersection)
    
