import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    sum = 0
    for n in line:
        sum += int(n)
    print sum
