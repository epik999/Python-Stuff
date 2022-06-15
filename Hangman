Attempts = 7
WordList = ['abc']
WordChosen = random.choice(WordList)
LettersGuessed = []
GuessedWord = False
while GuessedWord == False :
  if Attempts > 0 :
    print('You have ', Attempts, 'Attemps Left') # tells you how many words you have left
    for x in WordChosen : 
      if x.lower() in LettersGuessed :
        test = print(x, end='') # print the letter you guessed if in word
      else :
        print('_', end='') # prints underscores if you havent guessed that letter
    print(' ')
    UserGuess = input() # lets you guess a word
    LettersGuessed.append(UserGuess)
    if UserGuess.lower() not in WordChosen : # wrong guesses
      Attempts -= 1
    if Attempts == 0 : # loss condition
      print('You Lost')
      break
    
    CorrectWord = [characters in LettersGuessed for characters in WordChosen]
    HaveCorrectWord = all(CorrectWord)

    if HaveCorrectWord == True :
      GuessedWord = True
       
  if GuessedWord == True :
    print(WordChosen)
    print('You Won')
    exit()  
