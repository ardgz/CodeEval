import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    x, n = line.split(',')
    
    x = int(x)
    n = int(n)
    total = n
    
    while total < x:
        total += n
    print total
