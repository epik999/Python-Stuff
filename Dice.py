import random
for x in range(1,11):
    t1 = random.randint(1,6)
    t2 = random.randint(1,6)
    total = t1 + t2
    print(total)
    if total == 5:
        print('You rolled a 5!')
    if total == 10:
        print('You rolled a 10!')
    if t1 == t2:
        print ('You rolled a double!')

