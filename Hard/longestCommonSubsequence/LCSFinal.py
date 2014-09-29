import sys

def lengthLCSTabulate(leftStr, rightStr, sizeLeft, sizeRight):
    """ Return length of LCS using tabulation """
    m = sizeLeft
    n = sizeRight
    tableLengthLCS = [[0 for x in xrange(n+1)] for x in xrange(m+1)]
    i, j = 0, 0

    while i <= m:
        while j <= n:
            if i == 0 or j == 0:
                tableLengthLCS[i][j] = 0
            elif leftStr[i-1] == rightStr[j-1]:
                tableLengthLCS[i][j] = tableLengthLCS[i-1][j-1] + 1
            else:
                tableLengthLCS[i][j] = max(tableLengthLCS[i-1][j], tableLengthLCS[i][j-1])
            j += 1
        i += 1
        j = 0
    
    i = m
    j = n
    LCS = ""

    while i > 0 and j > 0:
        if leftStr[i-1] == rightStr[j-1]:
            LCS += leftStr[i-1]
            i -= 1
            j -= 1
        elif tableLengthLCS[i-1][j] > tableLengthLCS[i][j-1]:
            i -= 1
        else:
            j -= 1
    return LCS[::-1]

lines = file(sys.argv[1], 'r')
for line in lines:
    leftString, rightString = line.partition(';')[0:3:2]
    rightString = rightString[0:len(rightString)-1] # Strip newline char
    LCS = lengthLCSTabulate(leftString, rightString, len(leftString), len(rightString))
    print LCS
