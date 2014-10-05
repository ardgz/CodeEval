import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    numberStr = line.rstrip()
    i = 0
    result = 1
    while i < len(numberStr):
        if numberStr.count(str(i)) != int(numberStr[i]):
            result = 0
            break
        i += 1
    if result == 0:
        print 0
    else:
        print 1
    
