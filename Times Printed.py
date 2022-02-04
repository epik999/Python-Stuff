import random
import colorama

# original lists
ChooseFrom = ('Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5')
list = []


# list maker
for x in range(100):
    printer = random.choice(ChooseFrom) 
    list.append(str(printer))

# Printing List
print(str(list))

# space
print(' ')

# Word Count
Option1 = print( ' Option 1 appears : ' + (str(list.count('Option 1'))) + ' times!' )
Option2 = print( ' Option 2 appears : ' + (str(list.count('Option 2'))) + ' times!' )
Option3 = print( ' Option 3 appears : ' + (str(list.count('Option 3'))) + ' times!' )
Option4 = print( ' Option 4 appears : ' + (str(list.count('Option 4'))) + ' times!' )
Option5 = print( ' Option 5 appears : ' + (str(list.count('Option 5'))) + ' times!' )
