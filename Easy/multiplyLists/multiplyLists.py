import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    sidesList = line.split('|')

    leftSide = sidesList[0].strip().split(' ')
    rightSide = sidesList[1].strip().split(' ')
    
    i = 0
    productList = []
    while i < len(leftSide):
        productList.append(int(leftSide[i]) * int(rightSide[i]))
        i += 1
    
    i = 0
    result = ""
    while i < len(productList):
        result += str(productList[i]) + " "
        i += 1
    print result.strip()
    
        
