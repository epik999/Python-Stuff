import time

Loop = True
while Loop == True :
    print('enter a word:')
    Word = input()
    print(Word[::-1])
    print('Would you like to go again?')
    Answer = input('y or n : ')
    if Answer.upper() in ('YES', 'Y') :
        Loop = True
    else:
        Loop = False
        time.sleep(2); exit()
