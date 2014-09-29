import sys

def sortList(strList):  #Selection Sort
    i = 0
    for i in range(len(strList) - 1):
        min = len(strList[i])
        minPos = None
        j = i + 1
        
        for j in range(j, len(strList)):
            if len(strList[j]) < min:
                min = len(strList[j])
                minPos = j
        if minPos != None:
            strList[i], strList[minPos] = strList[minPos], strList[i] # Swap

    return strList

def main():
    test_cases = file(sys.argv[1], 'r')    
    N = None
    strList = []
    for test in test_cases:
        #print type(test)  # Debug
        if (N == None):
            N = int(test)
            continue
        
        strList.append(test)
    strList = sortList(strList)

    i = 0
    for i in range(N):
        if len(strList) != 0:
            print strList.pop(),
            
if __name__ == "__main__":
    main()
