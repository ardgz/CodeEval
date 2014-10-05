import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    words = line.rstrip().split(' ')
    sentence = ''
    for word in words:
        sentence += word[0].capitalize() + word[1:len(word)] + ' '
    print sentence.rstrip()
        
