#Hangman style game
#Be able to draw basic shapes
#draw line, circle, square for example 
#learn how arrays function

import tkinter
import time
import random
from tkinter.constants import TRUE, X, Y
#window
Window1 = tkinter.Tk()
Window1.title('Shapes')
#canvas
Canvas1 = tkinter.Canvas(Window1, bg="black", height=300, width=300)
Canvas1.pack()
# draw lines
#line = c.create_line(50, 50, 50, 100, fill = 'red', width = 1.25)

#draw square(painful method)
# sq1 = c.create_line(100, 50, 100, 100, fill = 'green', width = 1.25)
# sq2 = c.create_line(100, 50, 150, 50, fill = 'green', width = 1.25)
# sq3 = c.create_line(150, 50, 150, 100, fill = 'green', width = 1.25)
# sq4 = c.create_line(150, 100, 100, 100, fill = 'green', width = 1.25)


#draw square(easier-ish method)
#sqr1 = c.create_rectangle(200, 0, 250, 50, outline='blue', width = 1.25)

#draw circle
CircleX1 = 0
CircleY1 = 150
CircleX2 = 50
CircleY2 = 200
Circle1 = Canvas1.create_oval(CircleX1, CircleY1, CircleX2, CircleY2, outline='pink', width = 1.25)
LabelText = 'X=' + str(CircleX1) + ' , Y=' + str(CircleY1) + '    '
label1 = tkinter.Label(Canvas1, text = (LabelText), bg='black', fg='white')
label1.place(relx=0.1, rely=0.1)
#moving the shapes
MoveInPixelsX = 5
MoveInPixelsY = random.randint(1,15)

while TRUE:
    LabelText = 'X=' + str(CircleX1) + ' , Y=' + str(CircleY1) + ' , mY=' + str(MoveInPixelsY) + '   '
    label1 = tkinter.Label(Canvas1, text = (LabelText), bg='black', fg='white')
    label1.place(relx=0.1, rely=0.1)
    CircleX1 = CircleX1 + MoveInPixelsX
    if CircleX1 > 250 or CircleX1 == 0:
        MoveInPixelsX = MoveInPixelsX * -1
    CircleY1 = CircleY1 + MoveInPixelsY
    if CircleY1 >= 250 or CircleY1 <= 0:
        if MoveInPixelsY <= 0:
            MoveInPixelsY = random.randint(1,15)
            Canvas1.moveto(Circle1, CircleX1, 0)
            CircleY1 = 0        
        else:
            MoveInPixelsY = random.randint(1,15)
            MoveInPixelsY = MoveInPixelsY * -1
            Canvas1.moveto(Circle1, CircleX1, 250)
            CircleY1 = 250
    Canvas1.move(Circle1, MoveInPixelsX, MoveInPixelsY)
    time.sleep(0.025)
    Canvas1.update()

#ending window
Window1.mainloop()
