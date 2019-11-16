def isWordGuessed(secretWord, lettersGuessed):
    letter = True
    for x in lettersGuessed:
        letter = x in secretWord
        
        if letter == False:
            break
       
    return letter
        
def getGuessedWord(secretWord, lettersGuessed):
    Guessed = []
    for x in secretWord:
        if x in lettersGuessed:
            Guessed.append(x)
        else: 
            Guessed.append('_')
    return ' '.join(Guessed)

def getAvailableLetters(lettersGuessed):
    import string
   
    unused=[]
    smallletters = string.ascii_lowercase
   
    for x in smallletters:
        if x not in lettersGuessed:
            unused.append(x)
    
    return ' '.join(unused)

def Hangaroo(secretWord):
    import string
    lettersGuessed=[]
    list(lettersGuessed)
    mistakes= 0
    nword=len(secretWord)
    Guess = ''
     
    print('Hangaroooo!!!')
    print ('Guess the word that is',nword,'letters long')
    print(getGuessedWord(secretWord,lettersGuessed))
    
    
    while getGuessedWord(secretWord,lettersGuessed)!=  getGuessedWord(secretWord,secretWord):
        Guess = input('Enter a letter:(press 0 to quit): ')
        GuessInLowerCase= Guess.lower()
        
        if Guess =='0':break
        elif len(GuessInLowerCase) != 1 or (GuessInLowerCase in string.ascii_lowercase) == False :
            print('Invalid input, try again')
            print ('--------------')
            
        elif (GuessInLowerCase in secretWord) == False and (GuessInLowerCase in lettersGuessed) == False:
            mistakes += 1
            print ('Wrong, try again')
            print('mistakes made: ', mistakes)
            lettersGuessed.append(GuessInLowerCase)
            
        elif (GuessInLowerCase in lettersGuessed) == True : 
            print ('You have already guessed that-so try again!')
       
        else:
            print('You have made a right guess')
            lettersGuessed.append(GuessInLowerCase)
            
        print(getGuessedWord(secretWord,lettersGuessed))
        print('Letters Available: ', getAvailableLetters(lettersGuessed))
            
    if  Guess == '0':
        print('You did not guess the secret word. The secret word is ',secretWord)
        
    elif getGuessedWord(secretWord,lettersGuessed)== getGuessedWord(secretWord,secretWord):
        print('')    
        print('WINNER WINNER HANGAROO DINNER','The secret Word is',secretWord)
    return