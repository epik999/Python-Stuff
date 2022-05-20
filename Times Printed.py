import random

# original lists
ChooseFrom = ('Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5')
list = []

optioncount = 5


# list maker
for x in range(100):
    printer = random.choice(ChooseFrom)
    list.append(str(printer))

# Printing List
print(str(list))

# space
print(' ')

# Word Count
for x in range(0, optioncount) :
    print( ' Option '+ str(x + 1) + ' appears : ' + (str(list.count('Option ' + str(x + 1)))) + ' times!' )