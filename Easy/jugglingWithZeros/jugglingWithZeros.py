import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char

    # 00 flag - change following zeros into ones and append to binary string
    # 0 flag - append following zeros to binary string
    zerosList = line.split(' ')
    flag = ''
    binaryString = ''
    
    for value in zerosList:
        if flag == '':
            flag = value
        else:
            if flag == '00':
                ones = ""
                for i in xrange(len(value)):
                    ones += '1'
                binaryString += ones
            elif flag == '0':
                binaryString += value
            flag = ''
    print int(binaryString, 2)
