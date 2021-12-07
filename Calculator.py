import math
#loop
i = 'on'
while i == 'on':
#first number
    print('enter a number:')
    a = input()
#operation
    print('what operation do you want?:')
    c = input('*, /, +, -, sqrt or sq')
#square
    if c== 'sq':
        print(int(a) * int(a))
#square root
    if c == 'sqrt':
        print(math.sqrt(int(a)))
#second number
    if c == 'sqrt':
        print('would you like to repeat?')
        x = input('y or n')
        if x == 'y':
            i = 'on'
        else:
            i = 'off'
            exit()
    if c == 'sq':
        print('would you like to repeat? (yes or no)')
        x = input()
        if x == 'yes':
            i = 'on'
        else:
            i = 'off'
    else:
        print('enter another number:')
        b = input()

#adding
        if c == 'add':
            print(int(a) + int(b))
        if c == '+':
            print(int(a) + int(b))
#subtracting
        if c == 'subtract':
            print(int(a) - int(b))
        if c == '-':
            print(int(a) - int(b))
#multiplying
        if c == 'multiply':
            print(int(a) * int(b))
        if c == '*':
            print(int(a) * int(b))
#dividing
        if c == 'divide':
            print(int(a) / int(b))
        if c == '/':
            print(int(a) / int(b))
#looping
        print('would you like to repeat? (yes or no)')
        d = input()
        if d == 'yes':
            i = 'on'
        else:
            i = 'off'
            