import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    line = line.strip() # Remove newline char
    sentence, hints = line.split(';')
    wordsList = sentence.split(' ')
    hintList = hints.split(' ')
    constructedSentence = ["" for x in xrange(len(wordsList))]
    
    # Change elements of constructedSentence at positions listed from hintList
    # Unchanged position will still contain ""
    i = 0
    while i < len(hintList):
        constructedSentence[int(hintList[i]) - 1] = wordsList[i]
        i += 1
        
    # Grab index of unchanged position
    missingIndex = constructedSentence.index("")

    # Fill in unchanged element with remaining word from wordsList
    constructedSentence[missingIndex] = wordsList[-1]
    
    # Construct sentence string from elements of constructedSentence list
    sentence = "" 
    for w in constructedSentence:
        sentence += w + " "
    sentence = sentence.strip()
    print sentence
