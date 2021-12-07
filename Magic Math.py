import random
import time
import colorama
#first number
num1 = random.randint(1,20)
#operation
opc = ('+', '-', '*', '/')
op = random.choice(opc)

#second number
num2 = random.randint(1,20)
#print question
print('What is the answer to :', num1, op, num2)
#answer to question
#
#Plus
if op == '+':
    opplus = 'on'
    ans1 = (num1 + num2)
    while opplus == 'on':
        uans1 = input()
        intuans1 = int(uans1)
        if intuans1 != ans1:
            print(colorama.Fore.RED + 'That is not correct, try again' + colorama.Fore.WHITE)
            opplus = 'on'
        if intuans1 == ans1:
            print(colorama.Fore.GREEN + 'That is correct')
            opplus = 'off'
        #End Plus
        if opplus == 'off':
            print(colorama.Fore.WHITE + 'Thanks for playing')
            time.sleep(2); exit()
#
#Subtract
if op == '-':
    opminus = 'on'
    ans2 = (num1 - num2)
    while opminus == 'on':
        uans2 = input()
        intuans2 = int(uans2)
        if intuans2 != ans2:
            print(colorama.Fore.RED + 'That is not correct, try again' + colorama.Fore.WHITE)
            opminus = 'on'
        if intuans2 == ans2:
            print(colorama.Fore.GREEN + 'That is correct')
            opminus = 'off'
        #End Minus
        if opminus == 'off':
            print(colorama.Fore.WHITE + 'Thanks for playing')
            time.sleep(2); exit()
#
#Multiply
if op == '*':
    opmult = 'on'
    ans3 = (num1 * num2)
    while opmult == 'on':
        uans3 = input()
        intuans3 = int(uans3)
        if intuans3 != ans3:
            print(colorama.Fore.RED + 'That is not correct, try again' + colorama.Fore.WHITE)
            opmult = 'on'
        if intuans3 == ans3:
            print(colorama.Fore.GREEN + 'That is correct')
            opmult = 'off'
        #end multiply
        if opmult == 'off':
            print(colorama.Fore.WHITE + 'Thanks for playing')
            time.sleep(2); exit()
#
#Divide
if op == '/':
    opdivide = 'on'
    ans4 = (num1 / num2)
    while opdivide == 'on':
        uans4 = input()
        intuans4 = int(uans4)
        if intuans4 != ans4:
            print(colorama.Fore.RED + 'That is not correct' + colorama.Fore.WHITE)
            opdivide = 'on'
        if intuans4 == ans4:
            print(colorama.Fore.GREEN + 'That is correct')
            opdivide = 'off'
        if opdivide == 'off':
            print(colorama.Fore.WHITE + 'Thanks for playing')
            time.sleep(2); exit()
