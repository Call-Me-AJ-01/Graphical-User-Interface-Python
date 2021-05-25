from tkinter import *
from tkinter import ttk

# Creating Object For The Window
root = Tk()

# Creating The Title Of The Window
root.title('Place Geometry Manager')

# Fixing The Size Of The Window
root.geometry('400x250+500+500') #(width x height + place of window in x points + place of window in y points)

# Label 1
label_title = Label(root,text='Welcome To AJ Industries',font=(('Timenewroman'),15,'bold')).place(x=80,y=20)

# Label 2
label_name = Label(root,text='Enter Your Name :',font=(20)).place(x=20,y=70)
# Entry Field 1
name_input = Entry(root,width=30).place(x=160,y=74)

# Label 3
label_password = Label(root,text='Enter Your Password :',font=20).place(x=20,y=120)
# Entry Field 2
password_input = Entry(root,width=30,show='*').place(x=183,y=123)

# Button
button = ttk.Button(root,text='Save').place(relx=0.5,rely=0.75,anchor='center')

# Displaying The Window
root.mainloop()