import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    parts = line.rstrip().split(',')
    sentence = parts[0]
    char = parts[1]
    i = len(sentence) - 1
    while i >= 0:
        if sentence[i] == char:
            index = i
            break
        i -= 1
    print index
