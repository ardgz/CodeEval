import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    numberList = line.rstrip().split()
    #print numberList
    times = -1
    number = -1
    resultList = []
    for num in numberList:
        if number != int(num):
            if times == -1:
                number = int(num)
                times = 1
            else:
                resultList.append(times)
                resultList.append(number)
                number = int(num)
                times = 1
        else:
            times += 1
    resultList.append(times)
    resultList.append(number)
    print ' '.join(str(num) for num in resultList)
