import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    letterValue = dict({'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 
                       'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 
                       'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 
                       'x':24, 'y':25, 'z':26})
    beautySum = 0
    letterCount = [0 for x in xrange(26)]
    
    # Edit letterCount to contain the number of times a letter appears in
    # a sentence
    for c in line:
        if c.isalpha():
            letterIndex = letterValue[c.lower()] - 1
            letterCount[letterIndex] += 1
    
    # Set for remaining loop
    pointValue = 26  # Max beauty value
    maxCount = max(letterCount)
    
    # Use the letterCount to calculate the beautySum
    nextCountSet = False
    while maxCount > 0:
        numberOfCurrentCount = letterCount.count(maxCount)
        while numberOfCurrentCount > 0:
            beautySum += maxCount * pointValue
            numberOfCurrentCount -= 1
            pointValue -= 1
        while nextCountSet == False and maxCount > 0:
            maxCount -= 1
            if maxCount in letterCount:
                nextCountSet = True
            else:
                maxCount -= 1
        nextCountSet = False
    
    print beautySum

