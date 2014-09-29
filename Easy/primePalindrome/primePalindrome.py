import math

def generatePrimes():
    value = 1
    SIZE = 1000
    primes = []

    while (value < SIZE):    
        if value == 1:     # 1 is not a prime
            value += 1
            continue
        elif value == 2:   # 2 is a prime
            primes.append(value)
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
            primes.append(value)    # add prime to primeList
                    
        value += 1
    return primes

def longestPrimePalindrome(primeList):
    palindrome = None
    for prime in primeList:
        if len(str(prime)) == 1:
            palindrome = prime
            continue
        else:
            i = 0
            j = len(str(prime)) - 1
            primeString = str(prime)

            while (i != j):
                if (primeString[i] == primeString[j]):
                    i += 1
                    j -= 1
                    if i == j or i > j:
                        palindrome = prime
                        break
                else:
                    break
    return palindrome

primeList = generatePrimes()

result = longestPrimePalindrome(primeList)
print result
