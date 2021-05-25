from tkinter import *
from tkinter import ttk

# Creating Object For The Window
root = Tk()

# Declaring The Title For The Window
root.title('Frames')

# Fixing The Size Of The Window
root.geometry('500x500')
root.config(bg='yellow')

# Creating Frames
frame_obj = Frame(root,height=300,width=300,bg='red',bd='3',relief=SUNKEN)
frame_obj.pack(fill=X)

# Creating Button On Frame
button1 = ttk.Button(frame_obj,text='button 1')
button1.pack(padx=20,pady=20,side='left')

button2 = ttk.Button(frame_obj,text='button 2')
button2.pack(padx=20,pady=20,side='left')

# Creating Button On Root
button3 = ttk.Button(root,text='button 1')
button3.place(x=20,y=100)

button4 = ttk.Button(root,text='button 2')
button4.place(x=140,y=100)

# Displaying The Window
root.mainloop()