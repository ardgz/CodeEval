import sys

def main():
    stack = []

    lines = file(sys.argv[1], 'r')
    
    for line in lines:
        stack = line.split()
        counter = 1
        while (len(stack) > 0):
            if counter % 2 != 0:
                print stack.pop(),
            else:
                stack.pop()
            counter += 1
        print ''

if __name__ == "__main__":
    main()
