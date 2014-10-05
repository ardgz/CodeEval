import sys

lines = file(sys.argv[1], 'r')

def fibonacci(n):
    if fibonacci.values[n] != 0:
        return fibonacci.values[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibonacci.values[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

for line in lines:
    line = line.strip() # Remove newline char
    n = int(line)
    fibonacci.values = [0 for x in xrange(n+1)]
    
    print fibonacci(n)
