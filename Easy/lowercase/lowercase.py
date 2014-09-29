import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip()
    print line.lower()
