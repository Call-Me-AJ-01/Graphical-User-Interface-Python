from tkinter import *

# Creating Object for The Window
root = Tk()

# Declaring The Title for The Window
root.title('Scroll Bar')

# Fixing The Size Of The Window
root.geometry('500x450')

# Creating The Textfield
textbox = Text(root,width=60,height=20,wrap=WORD)
textbox.grid(row=0,column=0)

# Example Content
textbox.insert(INSERT,"Please Copy and Paste Some Contents on The TextField In Order To Check The Scroll Button")

# Creating The Scroll Bar
scroll = Scrollbar(root,orient=VERTICAL,command=textbox.yview)
scroll.grid(row=0,column=1,sticky=N+S)

# To Reflect The Scrolled Actions On The Textbox
textbox.config(yscrollcommand=scroll.set)

# Displaying The Window
root.mainloop()