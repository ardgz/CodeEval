import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip()
    parts = line.split('|')
    letters, key = parts[0], parts[1]
    keyList = key.lstrip().split(' ')
    
    result = ''
    for k in keyList:
        result += letters[int(k) - 1]
        
    print result
