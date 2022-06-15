import random
import os

def ConsoleClear() : # creates function to clear the console
  os.system("cls")
  
WordList =  """ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra""".split()

WordChosen = random.choice(WordList)
Attempts = 7
LettersGuessed = []
GuessedWord = False
while GuessedWord == False :
  if Attempts == 1 : # prints the hangman
    print('''
    +-----+
    |     |
    |     O
    |    /|\ ''')
    print("    |    /")
    print("    |")
    print("    ========")
  
  if Attempts == 2 :
    print('''
    +-----+
    |     |
    |     O
    |    /|\ ''')
    print("    |")
    print("    |")
    print("    ========")
          
  
  if Attempts == 3 :
    print('''
    +-----+
    |     |
    |     O
    |    /|
    |
    |
    ========
          ''')
  
  if Attempts == 4 :
    print('''
    +-----+
    |     |
    |     O
    |     |
    |
    |
    ========
          ''')
  
  if Attempts == 5 :
    print('''
    +-----+
    |     |
    |     O
    |
    |
    |
    ========
          ''')
  
  if Attempts == 6 :
    print('''
    +-----+
    |     |
    |
    |
    |
    |
    ========
          ''')
  
  if Attempts == 7 :
    print('''
    +-----+
    |
    |
    |
    |
    |
    ========
          ''')
  
  if Attempts > 0 :
    for x in WordChosen : 
      if x.lower() in LettersGuessed :
        test = print(x, end='') # print the letter you guessed if in word
      else :
        print('_', end='') # prints underscores if you havent guessed that letter
    print(' ')
    print('You have ', Attempts, 'Attemps Left') # tells you how many words you have left
    UserGuessCheck = False
    UserGuess = input() # lets you guess a word
    if len(UserGuess) != 1 : # makes sure you only enter one character
      print('Enter only one character!')
      UserGuessCheck = True
      while UserGuessCheck == True :
        UserGuess = input()
        if len(UserGuess) == 1 :
          UserGuessCheck = False
    if UserGuess in LettersGuessed : # stops you from guessing the same character
      print('You have already guessed this character!')
      UserGuessCheck = True
      while UserGuessCheck == True :
        UserGuess = input()
        if UserGuess not in LettersGuessed :
          UserGuessCheck = False
    LettersGuessed.append(UserGuess)
    ConsoleClear() # clears console
    if UserGuess.lower() not in WordChosen : # wrong guesses
      Attempts -= 1
    if Attempts == 0 : # loss condition
      print('''
    +-----+
    |     |
    |     O
    |    /|\ ''')
      print("    |    / \ ")
      print("    | ")
      print("    ======== ") 
      print("You lost the word was :", WordChosen)
      break
    if all([a in LettersGuessed for a in WordChosen]) == True : # checks if you have guessed all the letters in the word
      GuessedWord = True
  if GuessedWord == True :
    print('You won the word was :', WordChosen)
    GuessedWord = True