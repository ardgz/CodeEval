import sys
import math

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.rstrip()
    number, mod = line.partition(',')[0:len(line):2]
    quotient = int(number) / int(mod)
    value = float(number) / float(mod)
    result = (value - float(quotient)) * float(mod)
    print int(round(result))
