import sys

def matchOneOrMoreChars(string, substring):
    if len(substring) < 1:
        return True

    i = 0
    j = 0
    char = substring[0]
    while i < len(string):
        if string[i] == char: # Matches char of substring, regex matching stops 
            j += 1
            i += 1
        else:   # Doesn't match char, keep regex matching
            i += 1
    if j >= len(substring):  # substring found in string
        return True
    else:  # substring still left for matching, go back to regular matching
        return isSubString(string[i:len(string)], substring[j:len(substring)]) 

def isSubString(string, substring):
    i = 0
    j = 0
    
    #CEval, C*Eval
    while i < len(string):
        if string[i] == substring[j]:
            j += 1
            if j == len(substring):  # Whole substring matched
                return True
        elif substring[j] == '\\': # \ detected in substring
            if substring[j+1] == '*':   # \* detected in substring
                if string[i] == '*':
                    j += 2
                    if j == len(substring):
                        return True
                else:
                    if j > 0:
                        j = 0
                        continue
                    else:
                        i += 1
                        continue
        elif substring[j] == '*': # * Detected, match zero or more chars
            # Match zero chars case
            if j + 1 < len(substring):
                splitJob1 = isSubString(string[i:len(string)], substring[j+1:len(substring)])
            else:
                splitJob1 = True
            # Match more than zero chars case
            #splitJob2 = isSubString(string[i+1:len(string)], substring[j:len(substring)])
            splitJob2 = matchOneOrMoreChars(string[i+1:len(string)], substring[j+1:len(substring)])

            if splitJob1 == True or splitJob2 == True:
                return True
        else:  # current chars don't match, don't iterate i to recheck with new j
            if j > 0:
                j = 0
                continue
            else:
                i += 1
                continue

        i += 1
    return False

lines = file(sys.argv[1], 'r')

for line in lines:
    
    #commaIndex = 0
    
    #while commaIndex < len(string):
    #    if string[commaIndex] == ',':
    #        break
    #    else:
    #        commaIndex += 1
    string, substring = line.partition(",")[0:3:2]

    substring = substring[0:len(substring) - 1]  #Remove newlines from end
    
    result = isSubString(string, substring)
    if result == True:
        print "true"
    else:
        print "false"
