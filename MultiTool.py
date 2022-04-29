# Libraries
import random
import math

#  Loop
while True :
    # Tool Choice
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

     0: Exit
     1: Rock Paper Scissors
     2: Calculator
     3: Dice Roll








    ''')

    ToolChoice = input("Choose a Tool : ")

    # Rock Paper Scissors Function
    def Player1() :

        # Loss
        if Start.upper() == "ROCK" and Player2 == "PAPER" :
            print("You Lost" + " The AI chose " + Player2)

        if Start.upper() == "PAPER" and Player2 == "SCISSORS" :
            print("You Lost" + " The AI chose " + Player2)

        if Start.upper() == "SCISSORS" and Player2 == "ROCK" :
            print("You Lost" + " The AI chose " + Player2)

        # Draw
        if Start.upper() == Player2 :
            print("You Drew" + " The AI chose " + Player2)

        # Win
        if Start.upper() == "PAPER" and Player2 == "ROCK" :
            print("You Win" + " The AI chose " + Player2)

        if Start.upper() == "SCISSORS" and Player2 == "PAPER" :
            print("You Win" + " The AI chose " + Player2)

        if Start.upper() == "ROCK" and Player2 == "SCISSORS" :
            print("You Win" + " The AI chose " + Player2)

    # Calculator Function
    def Calculator() :
        INTCheck1 = False
        INTCheck2 = False

        # Asks for first number
        Number1 = input("Enter Number : ")

        # Checks for Number1 is an integer
        if str.isdigit(Number1) == False :
            INTCheck1 = True
            while INTCheck1 == True :
                print("Please enter an Integer!")
                Number1 = input("Enter Number : ")
                if str.isdigit(Number1) == True :
                    INTCheck1 = False

        # Asks for Operation
        Operation = input("Enter Operation : ")
        if Operation.upper() in ("SQUARE", "SQ") :
            print(float(Number1)*float(Number1))
        if Operation.upper() in ("SQRT", "SQUARE ROOT") :
            print(math.sqrt(float(Number1)))
        else :
            # Asks for second number if operation is not squaring or square root
            Number2 = input("Enter another Number : ")

            # Checks if Number2 is an integer
            if str.isdigit(Number2) == False :
                INTCheck2 = True
                while INTCheck2 == True :
                    print("Please enter an Integer!")
                    Number2 = input("Enter another Number : ")
                    if str.isdigit(Number2) == True :
                        INTCheck2 = False

            # Adding
            if Operation.upper() in ("ADD", "PLUS", "+") :
                print(int(Number1)+int(Number2))

            # Subtracting
            if Operation.upper() in ("TAKE AWAY", "SUBTRACT", "-") :
                print(int(Number1)-int(Number2))

            # Dividing
            if Operation.upper() in ("/", "DIVIDE") :
                print(int(Number1)/int(Number2))

            # Multiplying
            if Operation.upper() in ("*", "MULTIPLY", "TIMES") :
                print(int(Number1)*int(Number2))

    # Dice Function
    def Dice() :
        DiceAmount = input("How many Dice? : ")
        DiceAmountCheck = False

        # Checks if DiceAmount is an integer
        if str.isdigit(DiceAmount) == False:
            DiceAmountCheck = True
            while DiceAmountCheck == True :
                print("Enter a Number!")
                DiceAmount = input("How many Dice : ")
                if str.isdigit(DiceAmount) == True :
                    DiceAmountCheck = False
        
        # Dice Sides
        DiceSides = input("How many Sides? : ")
        DiceSidesCheck = False

        # Checks if DiceSides is an integer
        if str.isdigit(DiceSides) == False :
            DiceSidesCheck = True
            while DiceSidesCheck == True :
                print("Enter a Number!")
                DiceSides = input("How many Sides? : ")
                if str.isdigit(DiceSides) == True :
                    DiceSidesCheck = False
        
        # Rolls Dice
        for x in range(int(DiceAmount)) : 
            print(random.randint(1,int(DiceSides)))

    # Exit (Tool 0)
    if ToolChoice == "0" :
        exit()

    # Rock Paper Scissors (Tool 1)
    if ToolChoice == "1" :

        Choices = ("ROCK", "PAPER", "SCISSORS")
        Player2 = random.choice(Choices)
        Start = input("Rock, Paper or Scissors? : ")

        Player1()

    # Calculator (Tool 2)
    if ToolChoice == "2":

        Calculator()

    # Dice Roll (Tool 3)
    if ToolChoice == "3" :

        Dice()


