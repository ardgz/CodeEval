import sys

def main():
    if len(sys.argv) == 4:
        A = int(sys.argv[1])
        B = int(sys.argv[2])
        N = int(sys.argv[3])

        currentValue = 1
        result = ""

        while currentValue <= N:
            if currentValue % A == 0:      #currentValue divisible by A
                result += "F"

            if currentValue % B == 0:      #currentValue divisible by B
                result += "B"

            if result == "":                #currentValue not divisible by A and B
                result += str(currentValue)
            
            print result,

            currentValue += 1    #iterate currentValue
            result = ""          #set result back to empty
            
    elif len(sys.argv) < 4:
        print "Not enough arguments provided. Please use only three"

    else:
        print "Too many arguments provided. Please use only three."

if __name__ == "__main__":
   main()
