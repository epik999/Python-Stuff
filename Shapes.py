#Hangman style game
#Be able to draw basic shapes
#draw line, circle, square for example 
#learn how arrays function

import tkinter
import time
from tkinter.constants import X, Y
#window
window = tkinter.Tk()
#canvas
c = tkinter.Canvas(window, bg="black", height=300, width=300)
c.pack()
# draw lines
line = c.create_line(50, 50, 50, 100, fill = 'red', width = 1.25)

#draw square(painful method)
# sq1 = c.create_line(100, 50, 100, 100, fill = 'green', width = 1.25)
# sq2 = c.create_line(100, 50, 150, 50, fill = 'green', width = 1.25)
# sq3 = c.create_line(150, 50, 150, 100, fill = 'green', width = 1.25)
# sq4 = c.create_line(150, 100, 100, 100, fill = 'green', width = 1.25)


#draw square(easier-ish method)
sqr1 = c.create_rectangle(200, 0, 250, 50, outline='blue', width = 1.25)
#draw circle
circ1 = 0
circ2 = 250
circ3 = 50
circ4 = 300
circle = c.create_oval(circ1, circ2, circ3, circ4, outline='pink', width = 1.25)
#moving the shapes
i = '1'
while i == '1':
    for a in range(50):
        #forward
        sqx = 0
        sqy = 5
        cx = 5
        cy = 0
        c.move(circle, cx, cy)
        c.move(sqr1, sqx, sqy)
        time.sleep(0.025)
        c.update()
        #backwards
    for a2 in range(50):
        cx1 = -5
        sqy1 = -5
        c.move(sqr1, sqx, sqy1)
        c.move(circle, cx1, cy)
        time.sleep(0.025)
        c.update()

#ending window
window.mainloop()
