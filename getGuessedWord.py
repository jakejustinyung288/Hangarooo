def getGuessedWord(secretWord, lettersGuessed):
    Guessed = []
    for x in secretWord:
        if x in lettersGuessed:
            Guessed.append(x)
        else: 
            Guessed.append('_')
    return ' '.join(Guessed)
