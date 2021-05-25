from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Creating Object for The Window and Theme
root = tk.ThemedTk() # Creating Theme Object

root.get_themes()
root.set_theme('radiance')

# Themes :- radiance,aquativo,arc,black,blue,clearlooks,elegance,itft1,kroc

# Creating The Title for the window
root.title('Dictionary App')

# Fixing The Size Of The Window
root.geometry('400x400')

# Creating Title
title = ttk.Label(root,text='Dictionary Application',font=('timesnewroman',16,'bold')).pack(pady=10)

# Creating Frames

# Creating Frame 1
frame_1 = Frame(root,width=300,height=30)
frame_1.pack()

# Creating Label and Entry Field on Frame1
label1 = ttk.Label(frame_1,text='Enter The Word :',font=('timesnewroman',10),justify=LEFT).pack(side=LEFT)
user_input = ttk.Entry(frame_1,width=30)
user_input.focus()
user_input.pack(padx=20)

# Creating Frame 2
frame_2 = Frame(root,width=300,height=30)
frame_2.pack(pady=10)

# Creating Label and combo box
label2 = ttk.Label(frame_2,text='Language : ',font=('timesnewroman',10)).pack(side=LEFT)

# Creating variable
com_val = StringVar()

# Setting variable
com_val.set('English')

# Creating combo box
combo = ttk.Combobox(frame_2,textvariable=com_val,values=('Tamil','English','Telugu','Hindi','Japanese','French'),state='readonly')
combo.pack(padx=60)

# Creating Frame 3
frame_3 = Frame(root,width=300,height=20)
frame_3.pack(pady=10)

# Creating Textbox
text_box = Text(frame_3,width=35,height=10,font='timesnewroman 10',wrap=WORD,)
text_box.pack()

# Creating Button
button = ttk.Button(frame_3,text='Find Meaning').pack(pady=10)

# Displaying The Window
root.mainloop()