import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    numbers = line.split(';')
    
    result = ""

    for num in numbers:
        if num == 'zero':
            result += str(0)
        elif num == 'one':
            result += str(1)
        elif num == 'two':
            result += str(2)
        elif num == 'three':
            result += str(3)
        elif num == 'four':
            result += str(4)
        elif num == 'five':
            result += str(5)
        elif num == 'six':
            result += str(6)
        elif num == 'seven':
            result += str(7)
        elif num == 'eight':
            result += str(8)
        elif num == 'nine':
            result += str(9)
    print result
            
