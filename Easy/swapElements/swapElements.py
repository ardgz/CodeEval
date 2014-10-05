import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.rstrip() # Remove newline char
    numbers, swapPositions = line.split(' : ')
    swapPositionsList = swapPositions.split(', ')
    numList = numbers.split(' ')

    for swapCommand in swapPositionsList:
        pos1, pos2 = swapCommand.partition('-')[0:3:2]
        numList[int(pos1)], numList[int(pos2)] = numList[int(pos2)], numList[int(pos1)]
    print ' '.join(numList)
