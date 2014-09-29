#!/usr/bin/python

import sys  # For handling command line arguments

def longestWord(sentence):
    words = sentence.split()

    maxWord = None
    length = 0

    for word in words:
        if len(word) > length:
            maxWord = word
            length = len(word)

    return maxWord

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        file = open(filename, 'r')
    
        for line in file:
            print longestWord(line)

    elif len(sys.argv) < 2:
        print "Please provide a filepath"

if __name__ == "__main__":
    main()
