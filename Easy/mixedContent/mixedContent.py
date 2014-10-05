import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.rstrip()
    mixedList = line.split(',')
    
    numList, wordList = [], []
    for element in mixedList:
        if element.isdigit():
            numList.append(element)
        else:
            wordList.append(element)
    if len(numList) == 0:
        print ','.join(wordList)
    elif len(wordList) == 0:
        print ','.join(numList)
    else:
        print ','.join(wordList) + '|' + ','.join(numList)
