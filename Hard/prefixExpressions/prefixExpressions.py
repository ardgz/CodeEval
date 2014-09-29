import sys

def main():
    class Stack:
        def __init__(self):
            self.stack = []
        def push(self, x):
            self.stack.append(x)
        def pop(self):
            if len(self.stack) > 0:
                return self.stack.pop()
            else:
                return None
        def isEmpty(self):
            if len(self.stack) == 0:
                return True
            else:
                return False
        def printData(self):
            print self.stack
        def printElementTypes(self):
            for value in self.stack:
                print type(value),
            print ""

    class Queue:
        def __init__(self):
            self.queue = []
        def push(self, x):
            self.queue.append(x)
        def pop(self):
            if len(self.queue) > 0:
                return self.queue.pop(0)
            else:
                return None
        def isEmpty(self):
            if len(self.queue) == 0:
                return True
            else:
                return False
        def printData(self):
            print self.queue
        def printElementTypes(self):
            for value in self.queue:
                print type(value),
            print ""

    lines = file(sys.argv[1], 'r')

    for line in lines:
        tokenList = []
        tokenList = line.split()
        
        operatorStack = Stack()
        operandQueue = Queue()
        for token in tokenList:
            if token == "+" or token == "*" or token == "/":
                operatorStack.push(token)
            else:    # Number
                if "." in token:
                    operandQueue.push(float(token))
                else:
                    operandQueue.push(int(token))
    
        #Evaluate Expression
        leftValue = operandQueue.pop()
        rightValue = operandQueue.pop()
        operator = operatorStack.pop()
    
        while rightValue != None:
            if operator == "+":
                leftValue = leftValue + rightValue
            elif operator == "*":
                leftValue = leftValue * rightValue
            elif operator == "/":
                leftValue = leftValue / float(rightValue)
            else:
                print "Invalid operator detected!"
                return
            rightValue = operandQueue.pop()

            if rightValue != None:
                operator = operatorStack.pop()
        
        print int(leftValue)
if __name__ == "__main__":
    main()
