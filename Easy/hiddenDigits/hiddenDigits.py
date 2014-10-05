OBimport sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.rstrip()
    result = ''
    for char in line:
        if char.isdigit():
            result += char
        elif char == 'a':
            result += str(0)
        elif char == 'b':
            result += str(1)
        elif char == 'c':
            result += str(2)
        elif char == 'd':
            result += str(3)
        elif char == 'e':
            result += str(4)
        elif char == 'f':
            result += str(5)
        elif char == 'g':
            result += str(6)
        elif char == 'h':
            result += str(7)
        elif char == 'i':
            result += str(8)
        elif char == 'j':
            result += str(9)
    if result != '':
        print result
    else:
        print 'NONE'
