import sys
import re
import math

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    xValues = re.findall('[(](-*\d+),', line) # Grab x values using regexp
    yValues = re.findall(',\s(-*\d+)', line) # Grab y values using regexp
    
    differenceX = int(xValues[0]) - int(xValues[1])
    differenceY = int(yValues[0]) - int(yValues[1])
    distance = math.sqrt( math.pow(differenceX, 2) + math.pow(differenceY, 2) )
    print int(distance)
