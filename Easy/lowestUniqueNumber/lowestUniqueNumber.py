import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    numList = line.strip().split(' ') # Remove newline and add to numList
    i = 0
    winner = None
    winnerIndex = None
    while i < len(numList):
        if numList.count(numList[i]) == 1:
            if winner == None:
                winner = int(numList[i])
                winnerPos = i + 1
            elif int(numList[i]) < winner:
                winner = int(numList[i])
                winnerPos = i + 1
        i += 1

    if winner == None:
        print 0
    else:
        print winnerPos
