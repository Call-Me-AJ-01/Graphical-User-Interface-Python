from tkinter import *
from tkinter import ttk

# Creating Object for The Window
root = Tk()

# Declaring Title For The Window
root.title('Progress Bar')

# Fixing the Size Of The Window
root.geometry('300x300')

# Creating Progress Bar 1
prog1 = ttk.Progressbar(root,orient=HORIZONTAL,length=200,mode='indeterminate')
prog1.pack(padx=20,pady=20)
prog1.start()
# To Stop the progress bar
# prog1.stop()

# Creating Progress Bar 2
prog2 = ttk.Progressbar(root,orient=HORIZONTAL,
                        length=200,
                        mode='determinate',
                        maximum=100.0,value=10.0) # 'value' determines the starting value of the progress bar and can also be changed
prog2.pack(padx=20,pady=20)
prog2.start()
# To Stop the progress bar
# prog2.stop()

# Displaying The Window
root.mainloop()