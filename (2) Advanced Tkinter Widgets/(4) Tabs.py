from tkinter import *
from tkinter import ttk, PhotoImage

# Creating Object For The Window
root = Tk()

# Declaring The Title for the Window
root.title('Tabs')

# Fixing The Size Of The Window
root.geometry('500x500')

# Storing Image In a Variable
Icon = PhotoImage('download.png')

# Creating Object For tab
tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH,expand=True)

# Creating Frames
frame1 = ttk.Frame(tabs)
frame2 = ttk.Frame(tabs)
frame2.pack(fill=BOTH,expand=True)

# Adding frames to the tabs
tab1 = tabs.add(frame1,text='First Tab')
tab2 = tabs.add(frame2,text='Second Tab')

# Creating Labels and Buttons for Frame1 and Frame2

# Frame 1
label1 = ttk.Label(frame1,text='Frame 1')
label1.pack(padx=20,pady=20)
button1 = ttk.Button(frame1,text='Click Me..!')
button1.pack(padx=20,pady=20)

# Frame 2
label2 = ttk.Label(frame2,text='Frame 2')
label2.pack(padx=20,pady=20)
button2 = ttk.Button(frame2,text='Click Me..!')
button2.pack(padx=20,pady=20)

# Selecting Particular Tab
tabs.select('1') # This Opens The Second Tab On Startup atb index starts from '0'

# Displaying The Window
root.mainloop()