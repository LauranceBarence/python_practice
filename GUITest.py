from tkinter import *

top = Tk()

li = ['Assassin\'s Creed', 'God of War', 'Devil May Cry']
listb = Listbox(top)
for item in li:
    listb.insert(0,item)
listb.pack()
top.mainloop()
