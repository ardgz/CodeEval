import sys

lines = file(sys.argv[1], 'r')

morseCodeDict = {'.-':'A',
                 '-...':'B',
                 '-.-.':'C',
                 '-..':'D',
                 '.':'E',
                 '..-.':'F',
                 '--.':'G',
                 '....':'H',
                 '..':'I',
                 '.---':'J',
                 '-.-':'K',
                 '.-..':'L',
                 '--':'M',
                 '-.':'N',
                 '---':'O',
                 '.--.':'P',
                 '--.-':'Q',
                 '.-.':'R',
                 '...':'S',
                 '-':'T',
                 '..-':'U',
                 '...-':'V',
                 '.--':'W',
                 '-..-':'X',
                 '-.--':'Y',
                 '--..':'Z',
                 '-----':'0',
                 '.----':'1',
                 '..---':'2',
                 '...--':'3',
                 '....-':'4',
                 '.....':'5',
                 '-....':'6',
                 '--...':'7',
                 '---..':'8',
                 '----.':'9',}
for line in lines:
    line = line.strip() # Remove newline char
    i = 0
    character = ''
    result = ''
    while i < len(line):
        if line[i] != ' ':
            character += line[i]
        else:
            if character != '':
                result += morseCodeDict[character]
                if line[i+1] == ' ':
                    result += ' '
            character = ''
        i += 1
    result += morseCodeDict[character]
    print result
            
