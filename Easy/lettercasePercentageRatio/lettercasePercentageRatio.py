import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    uppercaseCount = 0
    lowercaseCount = 0

    for c in line:
        if c.isupper():
            uppercaseCount += 1
        else:
            lowercaseCount += 1
    lowerPercent = float(lowercaseCount) / len(line) * 100
    upperPercent = float(uppercaseCount) / len(line) * 100
    lowerPercent = "{:.2f}".format(lowerPercent)
    upperPercent = "{:.2f}".format(upperPercent)
    print "lowercase:", lowerPercent, "uppercase:", upperPercent

    
