def isWordGuessed(secretWord, lettersGuessed):
    letter = True
    for x in lettersGuessed:
        letter = x in secretWord
        
        if letter == False:
            break
       
    return letter