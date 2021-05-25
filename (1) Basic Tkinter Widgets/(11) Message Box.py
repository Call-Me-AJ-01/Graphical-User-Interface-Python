from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Creating object for the window
root = Tk()

# Title For The Window
root.title('Message Box')

# Creating Function
def msg1():
    msg_in=messagebox.askquestion("Delete",'Are You Sure..?')
    if msg_in=='yes':
        print('Deleted')
    else:
        print('Not Deleted')

def msg2():
    messagebox.showinfo("Success",'Well Done')
    print('Clicked Info Button')

# Creating the Button
button1 = ttk.Button(root,text='Delete',command=msg1).grid(row=0,column=0,padx=25,pady=25)
button2 = ttk.Button(root,text='Info',command=msg2).grid(row=0,column=1,padx=25,pady=25)

# Fixing The size of the window
root.geometry('250x80')

# Displaying The Window
root.mainloop()