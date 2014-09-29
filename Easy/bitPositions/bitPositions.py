import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip()
    
    number, p1, p2 = line.split(',')
    number = int(number)
    p1 = int(p1)
    p2 = int(p2)
    # p1 and p2 are 1 based [1...n]
    
    bitSequence = ""
    base = 1
    
    # Calculate base value
    while base < number:
        base *= 2
    if base != number:
        base /= 2

    # Generate bitsequence
    while number > 0 or base != 0:
        if number >= base:
            bit = 1
        else:
            bit = 0
        bitSequence += str(bit)
        number = number % base
        base /= 2
        
    # Compare bits
    m = len(bitSequence) - p1
    n = len(bitSequence) - p2
    
    if bitSequence[m] == bitSequence[n]:
        print "true"
    else:
        print "false"
