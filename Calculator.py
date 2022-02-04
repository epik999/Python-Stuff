import math

# loop
Loop = True
while Loop == True:

#first number
    print('enter a number:')
    Number1 = input()

#operation
    print('what operation do you want?:')
    Operation = input('*, /, +, -, sqrt or sq')

#square
    if Operation.upper() == 'sq':
        print(int(Number1) * int(Number1))
        Repeat = input('would you like to repeat? ( Y or N)')
        if Repeat.upper() == 'Y':
            Loop = True
        else:
            Loop = False

#square root
    if Number1 == 'sqrt':
        print(math.sqrt(int(Number1)))
        Repeat = input('would you like to repeat? ( Y or N )')
        if Repeat.upper() == 'Y':
            Loop = True
        else:
            Loop = False
            quit()
# Second number
    else:
        print('enter another number:')
        Number2 = input()

#adding
        if Operation.upper() == 'add' or '+':
            print(int(Number1) + int(Number2))
            
#subtracting
        if Operation.upper() == 'subtract' or '-':
            print(int(Number1) - int(Number2))

#multiplying
        if Operation.upper() == 'multiply' or '*':
            print(int(Number1) * int(Number2))
#dividing
        if Operation.upper() == 'divide' or '/':
            print(int(Number1) / int(Number2))
#looping
        RestartLoop = input('would you like to repeat? ( Y or N )')
        if RestartLoop.upper() == 'Y':
            Loop = True
        else:
            Loop = False
            
            
