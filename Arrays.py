#arrays
import tkinter
import random
wordlist = ('Welcome', 'Python', 'Monopoly', 'Coding')
randword = random.choice(wordlist)
window = tkinter.Tk()
window.geometry('300x300')
window.title('Words')
label = tkinter.Label(window, text = (randword))
label.place(relx=0.5, rely=0.5, anchor='center')
window.mainloop()
