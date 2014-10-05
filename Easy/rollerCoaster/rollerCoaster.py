import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    
    capital = True # Toggle

    rollerCoasterString = ""
    for c in line:
        if c.isalpha():
            if capital == True:
                rollerCoasterString += c.upper()
                capital = False
            elif capital == False:
                rollerCoasterString += c.lower()
                capital = True
        else:
            rollerCoasterString += c
    print rollerCoasterString
