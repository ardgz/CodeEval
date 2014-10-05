import sys
import re

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    
    if len(line) <= 0:  # Skip blank lines
        continue

    labeled_IDs = re.findall('Label\s(\w+)\D', line) # Gather ID values from line using regex
        
    sum = 0
    for ID in labeled_IDs:
        sum += int(ID)
    print sum
