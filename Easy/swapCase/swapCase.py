import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    words = line.rstrip().split()
    sentence = ''
    for word in words:
        sentence += word.swapcase() + ' '
    print sentence.rstrip()
