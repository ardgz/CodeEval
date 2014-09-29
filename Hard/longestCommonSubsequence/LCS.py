import sys

#XMJYAUZ;MZJAWXU


#BASE;TIME
#E;E
def removeUniqueChars(leftStr, rightStr):
    """ Remove chars from leftStr not found in rightStr """
    resultStr = ""

    for i in leftStr:
        matchingChar = False
        for j in rightStr:
            if i == j:
                matchingChar = True
                break
        if matchingChar == True:
            resultStr += i
    return resultStr

def findLongestCommonSubstring(leftStr, rightStr):
    """ Find longest common substring from in leftStr and rightStr """
    LCS = ""

    i = 0
#XMJAUZ;MZJAXU
#E;EIO
#EIO;E    
    while i < len(leftStr):
        currentSequence = ""
        j = i
        k = 0
        while j < len(leftStr):
            m = j
            while k < len(rightStr):
                if m >= len(leftStr):  # index of leftStr out of bounds
                    if len(currentSequence) > len(LCS):
                        LCS = currentSequence
                    currentSequence = "" # reset substring
                    m = j
                elif leftStr[m] == rightStr[k]: # chars match
                    currentSequence += rightStr[k]
                    m += 1
                    k += 1
                else:  # chars don't match, keep trying to find substring
                    k += 1
                #print currentSequence # DEBUG
            if len(currentSequence) > len(LCS):
                LCS = currentSequence

            currentSequence = "" # reset substring since rightStr index is out of bounds
            j += 1
        i += 1
    return LCS

lines = file(sys.argv[1], 'r')
for line in lines:
    leftString, rightString = line.partition(';')[0:3:2]
    rightString = rightString[0:len(rightString)-1] # Strip newline char
 
    leftString = removeUniqueChars(leftString, rightString)
    rightString = removeUniqueChars(rightString, leftString)
    
    #print leftString, rightString, " -> ", # DEBUG
    r1 = findLongestCommonSubstring(leftString, rightString)
    r2 = findLongestCommonSubstring(rightString, leftString)
    
    if len(r1) > len(r2):
        result = r1
    else:
        result = r2
    print result
