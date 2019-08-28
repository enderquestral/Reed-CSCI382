import english

def isReducible(word): #returns true if word is reducible, false otherwise.
    if len(list(word)) <=1 and english.isEnglishWord(word):
        return True
    if english.isEnglishWord(word): #Only loops if current word is valid
        #Get a list of words that can be formed using one letter
        holdlistofpossiblewords = []
        for i in range(len(word)):
            possibleword = word[:i] + word[i+1:] #Get the word from the first i-sections + the character after i-section+1, thereby eliminating one character temp
            if english.isEnglishWord(possibleword):
                holdlistofpossiblewords.append(possibleword)
        
        for x in holdlistofpossiblewords:#Use word as a list of characters
            return isReducible(x) #find out if x word is reducible?
    return False