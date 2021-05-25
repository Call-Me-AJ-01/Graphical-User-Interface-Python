from tkinter import *

# Note:-
# --> jpg format is not supported <--

# Creating Object For The Window
root = Tk()

# Declaring The Title For The Window
root.title('Using Inages')

# Fixing The Size Of The Window
root.geometry('550x450')

# Creating Label
label1 = Label(root,text='I am Using Images',font='timesnewroman 16 bold',fg='red')
label1.pack()

# Loading The Image to a Variable
img = PhotoImage(file='G:\\Python\\Tkinter1\\images\\Simpsons_viewable.gif') # Has To Give Full Path Of The File

# Displaying Image on Label
label2 = Label(root,image=img)
label2.pack()

# Displaying The Window
root.mainloop()