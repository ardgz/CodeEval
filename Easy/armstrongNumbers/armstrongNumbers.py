import sys
import math

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.rstrip()
    
    n = float(len(line))
    sumPowers = 0
    for num in line:
        sumPowers += int( math.pow(int(num), n) )
    if int(line) == sumPowers:
        print True
    else:
        print False
    
