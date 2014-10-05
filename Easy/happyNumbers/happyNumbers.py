import sys
import math

lines = file(sys.argv[1], 'r')

for line in lines:
    numStr = line.strip() # Remove newline and assign to num as int
    
    num = None
    counter = 0
    uniqueNumbers = []
    
    while num != 1:
        if uniqueNumbers.count(numStr) > 1: # If numStr was already evaluated
            num = None
            break
        uniqueNumbers.append(numStr)
        if len(numStr) == 1: # Square number
            num = int(math.pow(int(numStr), 2))
            numStr = str(num)
        else: # Sum squares of digits
            sum = 0
            for d in numStr:
                sum += int(math.pow(int(d), 2))
            num = sum
            numStr = str(num)
            
    if num == None:
        print 0
    else:
        print num
