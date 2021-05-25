from tkinter import *
from tkinter import ttk

# Creating Object For The Window
root = Tk()

# Declaring Title For The Window
root.title('Search bar')

# Fixing The Size Of The Window
root.geometry('500x150')

# Creating Object For The Search Bar
search = LabelFrame(root,text='Search Bar Title',padx=20,pady=20) # You can also give the background color 'bg'
search.pack(padx=20,pady=20)

# Creating Label For The Search Bar
label = Label(search,text='Enter Your Name :',font='bold')
label.pack(side=LEFT,padx=10)

# Creating Entry Field For The Search Bar
entry = Entry(search,width=30)
entry.pack(side=LEFT,padx=10)

# Creating Button For The Search Bar
button = ttk.Button(search,text='Click Me..!')
button.pack()

# Displaying The Window
root.mainloop()