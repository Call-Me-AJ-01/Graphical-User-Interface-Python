from tkinter import *
from tkinter import ttk

# Creating The Object For The Window
root = Tk()

#Title of The Window
root.title('Text Editor')

#Creating a function to display
def display():
    print(text.get(0.1,END))
# Creating The Text Field
text = Text(root,width=30,height=10,font=('Timesnewroman 10 bold'),wrap=WORD)
text.insert(INSERT,'Comment')
text.grid(row=0,column=0,padx=25,pady=10)

# Creating The Button
button = ttk.Button(root,text='Submit',command=display).grid(row=1,column=0)
# Fixing The Size Of The Window
root.geometry('260x240')

#Displaying The Window
root.mainloop()