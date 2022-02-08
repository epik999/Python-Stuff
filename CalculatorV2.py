import math

def DisplayResult(OP, NUMS) :
# Squaring
    if OP.upper() == 'SQ' :
        TheResult = float(Numbers[0]) * float(Numbers[0])
# Square Root    
    elif OP.upper() == 'SQRT' :
        TheResult = math.sqrt(float(Numbers[0]))
# Power of    
    elif OP.upper() == '^' :
        TheResult = float(Numbers[0]) ** float(Numbers[1])
# Adding 
    elif OP.upper() in ('ADD', '+') :
        TheResult = float(Numbers[0]) + float(Numbers[1])
# Subtracting 
    elif OP.upper() in ('SUBTRACT', '-') :
        TheResult = float(Numbers[0]) - float(Numbers[1])
# Multiplying
    elif OP.upper() in ('MULTIPLY', '*') :
        TheResult = float(Numbers[0]) * float(Numbers[1])
# Dividing
    elif OP.upper() in ('DIVIDE', '/') :
        TheResult = float(Numbers[0]) / float(Numbers[1])
    
    print("{:.2f}".format(TheResult))


RepeatQuestion = True
while RepeatQuestion == True :
    Numbers = [0, 0]
    print('what operation do you want? : ')
    Operation = input('*, /, +, -, ^, sqrt or sq : ')

    if Operation.upper() in ('SQ', 'SQRT') :
        NumberCount = 1
    else :
        NumberCount = 2
    
    for x in range(NumberCount) :
        Numbers[x] = input('Enter Number ' + str(x + 1) + ': ')
    
    DisplayResult(Operation, Numbers)
    Repeat = input('would you like to repeat? ( Y or N) : ')
    if Repeat.upper() == 'Y':
        RepeatQuestion = True
    else:
        RepeatQuestion = False