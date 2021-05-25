from tkinter import *
from tkinter import ttk

# Adjusting The Screen Resolution Graphics For Better View
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Creating Object for the Window
root = Tk()

# Title For The Window
root.title('Grid Layout')

# Fixing The Size Of The Window
root.geometry('410x200')

# Creating label's

# Title Label
label_title = Label(root,text='AJ Industries',font='timesnewroman 20 bold underline',pady=10)
# Label 1
label1 = Label(root,text='Enter Your Name : ',pady=5)
# Label 2
label2 = Label(root,text='Enter Yout Password : ',pady=5)

# Creating Entry Box's

# Entry Box 1
entry1 = Entry(root,width=30)
# Entry Box 2
entry2 = Entry(root,width=30)
entry2.config(show='*')

# Creating Function For The Button
def Display():
    print('Name :',entry1.get())
    print('Password :',entry2.get())
    if check.get()==1:
        a='Yes'
    else:
        a='No'
    print('Remember :',a)

# Creating Button
button = ttk.Button(root,text='Login',command=Display)

# Declaring a Variable for The CheckBox
check = IntVar()

# Initially setting the value of check button to 0 Which Means Unchecked
check.set(0)

# Creating CheckBox
check_button = Checkbutton(root,text='Remember',font='arial 10',variable=check)

# Using Grid Layout
label_title.grid(row=0,column=0,columnspan=2)
label1.grid(row=1,column=0,sticky=W)
label2.grid(row=2,column=0,sticky=W)
entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)
check_button.grid(row=3,column=1,sticky=W)
button.grid(row=4,column=1,sticky=W+E)

# Displaying The Window
root.mainloop()