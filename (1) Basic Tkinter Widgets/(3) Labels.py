from tkinter import *

# Adjusting The Screen Resolution Graphics For Better View
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Creating The Object For The Window
root = Tk()

# Creating The Title For The Window
root.title('Labels')

# Fixing The Size Of The Window
root.geometry('250x250')

# Creating A Label
label = Label(root,text='Hello World',fg='white',bg='gray',wraplength=20,justify='right',font=('times 10'))

# Uncomment The Below Statements And See The Difference
'''
# Using The Configure Function To Modify The Label Value
label.config(text='Welcome To Python') # Changing The Text Content Of The Label
label.config(fg='red') # Changing The Text Color
label.config(bg='yellow') # Changinh The Backgroud Color
label.config(wraplength='60') # Changing The Length Of The Label
label.config(justify='left') # Changing The Aligment Of The Label
label.config(font=('timesnewroman 20 bold italic underline')) # Changing The Font and Size
label.config(padx=20,pady=20) # Creating Spcaes For The Label (padx - Creates Width left and right of The Label, pady - Creating Spaces top and bottom of The Label)'''

label.pack()

# Displaying The Window
root.mainloop()