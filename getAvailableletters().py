def getAvailableLetters(lettersGuessed):
    import string
    
    unused=[]
    smallletters = string.ascii_lowercase
   
    for x in smallletters:
        if x not in lettersGuessed:
            unused.append(x)
    
    return ' '.join(unused)