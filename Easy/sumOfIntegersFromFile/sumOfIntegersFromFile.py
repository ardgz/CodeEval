import sys

lines = file(sys.argv[1], 'r')

sum = 0
for line in lines:
    sum += int(line.strip()) # Remove newline char and add value to sum
print sum
