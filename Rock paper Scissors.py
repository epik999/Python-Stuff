# Rock paper Scissors
import random

# function to start game
def rps() :

    start = input('Would you like to Play? ( Y or N ) ')
    if start.upper() == "Y":

        # Possible Choices
        Choice = ('ROCK', 'PAPER', 'SCISSORS')

        # Player makes choice
        PlayerChosen = input('Rock, Paper or Scissors : ')

        # Computer makes choice
        Computerchoice = random.choice(Choice)

        # draw
        if PlayerChosen.upper() == Computerchoice :
            print('You Drew')
        # win
        elif PlayerChosen.upper() == 'ROCK' and Computerchoice == 'SCISSORS':
            print('You Win')
        elif PlayerChosen.upper() == 'PAPER' and Computerchoice == 'ROCK' :
          print('You Win')
        elif PlayerChosen.upper() == 'SCISSORS' and Computerchoice == 'PAPER' :
            print('You Win')
        # loss 
        else :
            print('You Lost')

    else:
        quit()

rps()