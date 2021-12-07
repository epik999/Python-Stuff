import time
#loop start
i = 'on'
while i == 'on':
#main
    print('enter a word:')
    name = input()
    print(name[::-1])
#Loop ans
    print('Would you like to go again?')
    ans = input('y or n : ')
#looping
    if ans == 'y':
        i = 'on'
    else:
        print('Thanks for using!')
        i = 'off'
        time.sleep(2); exit()