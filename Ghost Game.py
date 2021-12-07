#Ghost Game
import random
import time
print('Ghost Game')
Brave = True
score = 0
while Brave:
    ghost_door = random.randint(1, 3)
    print('Three doors ahead... A ghost behind one door')
    print('Which door will you choose?')
    door = input('1, 2 or 3?')
    door_num = int(door)
    if door_num == ghost_door:
        print('A GHOST!')
        Brave = False
    else:
        print('No ghost, you enter the next room')
        score = score +1
print('Game Over, You run away')
print('You scored', score)
time.sleep(2); exit()