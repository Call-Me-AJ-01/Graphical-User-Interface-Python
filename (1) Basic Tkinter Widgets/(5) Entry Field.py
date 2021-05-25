from tkinter import *
from tkinter import ttk

# Adjusting The Screen Resolution Graphics For Better View
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Creating Object For The Window
root = Tk()

# Creating The Function To Display
def display():
    print("Your Name Is :",entry1.get())
    print("Your Password Is :",entry2.get())

# Title Of The Window
root.title('Entry Field Widget')

# Fixing The Size Of The Window
root.geometry('410x200')

# Creating The Entry Field's

# Entry Field 1
entry1 = Entry(root,width=35)
entry1.insert(0,"Please Enter Your Name") # Creating Place Holder
entry1.pack()

# Entry Field 2
entry2 = Entry(root,width=35)
entry2.config(show='*') # Getting Input From The User in Password Format
entry2.pack()

# Entry Field 3
entry3 = Entry(root,width=35)
entry3.insert(0,"This Entry Field Is Disabled")
entry3.config(state='disabled')
entry3.pack()

# Entry Field 4
entry4 = Entry(root,width=35)
entry4.insert(0,"This Entry Field Is In Read Only Format")
entry4.config(state='readonly')
entry4.pack()

# Creating Button And Extracting The Text From The Entry Field
button = ttk.Button(root,text='Click Me..!',command=display)
button.pack()

# Displaying The Window
root.mainloop()
