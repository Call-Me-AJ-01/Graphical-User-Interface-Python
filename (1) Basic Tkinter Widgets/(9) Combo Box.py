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
root.geometry('500x270')

# Creating label's

# Title Label
label_title = Label(root,text='                AJ Industries',font='timesnewroman 20 bold ',pady=10)
# Label 1
label1 = Label(root,text='Enter Your Name : ',pady=5)
# Label 2
label2 = Label(root,text='Enter Yout Password : ',pady=5)
# Label 3
label3 = Label(root,text='Gender : ',pady=5)
# Label 4
label4 = Label(root,text='Birth-Day Month : ',pady=5)

# Creating Entry Box's

# Entry Box 1
entry1 = Entry(root,width=30)
# Entry Box 2
entry2 = Entry(root,width=30)
entry2.config(show='*')

# Creating Function For The Button
def Display():
    print('Name :',entry1.get())
    print('Gender :',gender.get())
    print('Birth-Day Month :',com.get())
    print('Password :',entry2.get())
    if check.get()==1:
        a='Yes'
    else:
        a='No'
    print('Remember :',a)

# Creating Button
button = ttk.Button(root,text='Login',command=Display)

# Declaring a Variable for CheckBox
check = IntVar()

# Initially setting the value of check button to 0 Which Means Unchecked
check.set(0)

# Creating CheckBox
check_button = Checkbutton(root,text='Remember',font='arial 10',variable=check)

# Declaring a variable for radio button
gender = StringVar()

# Creating Radio Button
male = ttk.Radiobutton(root,text='Male',value='Male',variable=gender)
female = ttk.Radiobutton(root,text='Female',value='Female',variable=gender)

# Declaring a variable for combo box
com=StringVar()

# Setting The Value Of The Combo Box
com.set('Jan')

# Creating a Combo Box
com_box=ttk.Combobox(root,textvariable=com,values=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
                     ,state='readonly')

# Using Grid Layout
label_title.grid(row=0,column=0,columnspan=2)
label1.grid(row=1,column=0,sticky=W)
entry1.grid(row=1,column=1)
label3.grid(row=2,column=0,sticky=W)
male.grid(row=2,column=1,sticky=W)
female.grid(row=2,column=2,sticky=W)
label4.grid(row=3,column=0,sticky=W)
com_box.grid(row=3,column=1,sticky=W)
label2.grid(row=4,column=0,sticky=W)
entry2.grid(row=4,column=1)
check_button.grid(row=5,column=1,sticky=W)
button.grid(row=6,column=1,sticky=W+E)

# Displaying The Window
root.mainloop()