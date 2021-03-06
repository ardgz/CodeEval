import math

value = 1
sum = 0
numPrimes = 0
MAX_PRIME_NUMBERS = 1000

while (numPrimes != MAX_PRIME_NUMBERS):    
    if value == 1:     # 1 is not a prime
        value += 1
        continue
    elif value == 2:   # 2 is a prime
        sum += value
        numPrimes += 1
        value += 1
        continue

    if value % 2 == 0:
        value += 1
        continue

    prime = True
    oddValue = 1
        
    while oddValue <= math.sqrt(value):
        if value % oddValue == 0 and oddValue != 1:
            prime = False
            oddValue += 2
            break
        else:    
            oddValue += 2
    if prime == True:
        sum += value
        numPrimes += 1      
    value += 1
print sum
