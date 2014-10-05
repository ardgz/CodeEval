import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    num = int(line.rstrip())
    if num % 2 == 0:
        print 1
    else:
        print 0
    
