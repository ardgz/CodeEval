# Print out 12 by 12 multiplication table
i = 1
j = 1

while i <= 12:
    line = ""
    while j <= 12:
        value = str(i * j)
        line += '{0: >4}'.format(value)
        j += 1
    print line
    i += 1
    j = 1
