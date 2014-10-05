import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    numbers, pattern = line.split(' ')
    
    if pattern.find('+') != -1: # + is in pattern
        symbolIndex = pattern.find('+')
        addNumbers = True
    else:                       # - is in pattern
        symbolIndex = pattern.find('-')
        addNumbers = False
    
    leftOperand = numbers[0:symbolIndex]
    rightOperand = numbers[symbolIndex:len(numbers)]
    if addNumbers:
        result = int(leftOperand) + int(rightOperand)
    else:
        result = int(leftOperand) - int(rightOperand)
    print result
    
    
