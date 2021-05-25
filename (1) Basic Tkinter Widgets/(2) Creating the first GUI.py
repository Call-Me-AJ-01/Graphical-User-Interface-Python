from tkinter import *
from tkinter import ttk

# Adjusting The Screen Resolution Graphics For Better View
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Creating The Object for The Window
root = Tk()

#Fixing The size of the window
root.geometry("250x250") # (Width x Height)

# Creating The Title For The Window
root.title('My First GUI')

#Difference Between tkinter widgets and ttk widgets
button1=Button(root,text='Tkinter Button').pack()
button2=ttk.Button(root,text='TTk Button').pack() # This one will look better

root.mainloop()