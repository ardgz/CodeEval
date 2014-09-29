import sys

def main():
    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        number = int(test)
        numOnes = 0
        divisor = 1
        while (divisor < number):
            divisor *= 2
        divisor /= 2

        while (number != 0):
            if number % divisor != number:
                numOnes += 1
            number %= divisor
            divisor /= 2

        print numOnes

if __name__ == "__main__":
    main()
