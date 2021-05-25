from tkinter import *
from tkinter import ttk

# Adjusting The Screen Resolution Graphics For Better View
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

count=0

def callback():
    global count
    count+=1
    label.config(text='Clicked Me : '+str(count),fg='green')

# Creating Object For The Window
root = Tk()

# Creating Title For The Window
root.title('Buttons')

# Fixing The Size Of the Window
root.geometry('250x100')

# Creating Label
label = Label(root,text='Clicked Me : '+str(count),fg='red',padx=20,pady=20)
label.pack()

# Creating The Button
button = ttk.Button(root,text='Click Me...!',command=callback)
button.pack()

# Diabling The Button
# button.config(state='disabled')


# Displaying The Window
root.mainloop()
