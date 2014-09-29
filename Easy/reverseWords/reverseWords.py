import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line[0:len(line)-1] # Remove newline char
    words = line.split(' ')
    i = len(words) - 1
    while i >= 0:
        if i == 0:
            print words[i]
        else:
            print words[i],
        i -= 1
