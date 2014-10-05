import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    hexNumber = line.rstrip()
    print int(hexNumber, 16)
