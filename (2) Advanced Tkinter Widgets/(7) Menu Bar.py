from tkinter import *
from tkinter import ttk

# Creating Object for The Window
root = Tk()

# Declaring Title For The Window
root.title('Menu Bar')

# Creating The menu Bar Object
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Adding Menu's

# Creating Object's for the menu
file = Menu(menu_bar,tearoff=0)
option = Menu(menu_bar,tearoff=0)
about = Menu(menu_bar,tearoff=0)
help = Menu(menu_bar,tearoff=0)

# Displaying The Object

# Adding File menu
menu_bar.add_cascade(label='File',menu=file)
file.add_command(label='New')
file.add_separator()
file.add_command(label='Save')
file.add_command(label='Save As')
file.add_command(label='Exit',command=root.destroy)

# Adding Option menu
menu_bar.add_cascade(label='Edit',menu=option)
option.add_command(label='Font')

# Adding About menu
menu_bar.add_cascade(label='About',menu=about)

# Adding Help menu
menu_bar.add_cascade(label='Help',menu=help)

# Fixing The Size Of The Window
root.geometry('500x500')

# Displaying The Window
root.mainloop()