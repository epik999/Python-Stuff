import time
import colorama
#setup loop
i = 'on'
while i == 'on':
#Lower Boundary
    print('What is the Lower Boundary?')
    lb = input()
#Upper Boundary
    print('What is the Upper Boundary?')
    hb = input()
#Loop
    for x in range(int(lb),int(hb)):
#Mulitples Var
        mult3 = x % 3 
        mult5 = x % 5
#multiples
        if mult3 == 0 and mult5 == 0:
            print(colorama.Fore.RED + 'Fizzbuzz' + colorama.Fore.WHITE)
        elif x % 3 == 0:
            print(colorama.Fore.RED + 'Fizz' + colorama.Fore.WHITE)
        elif x % 5 == 0:
            print(colorama.Fore.RED + 'Buzz' + colorama.Fore.WHITE)
        else:
            print(x)
#ending loop
    print('would you like to continue?')
    ans = input('y or n')
    if ans == 'y' :
        i = 'on'
    else:
        i = 'off'
        time.sleep(2); exit()
