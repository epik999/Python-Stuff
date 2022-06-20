import random

WordsAmount = input('How many different words? : ') # Self explanatory
WordsArray = []

for b in range(int(WordsAmount)) :
  WordsArray.append(input('Word ' + str(b+1) + ' of ' + WordsAmount + ': ')) # tells you what word you are entering

RandomWords = []
PrintAmount = input('How many times to print? : ') # self explanatory again

for x in range(int(PrintAmount)) :
  RandomWords.append(random.choice(WordsArray)) # chooses a random word from the words the user chose

print(str(RandomWords)) # prints all the words randomly chosen
print(' ')

for x in range(int(WordsAmount)) :
  print(WordsArray[x] + ' found ' + str(RandomWords.count(WordsArray[x])) + ' times') # counts how many times each word appears and prints it
