from tkinter import *
from tkinter import ttk

# creating Object for the Window
root = Tk()

# Declaring The Size Of The Window
root.title('Paned Window')

# Creating Paned Window
pan_win = ttk.Panedwindow(root,orient=HORIZONTAL)
pan_win.pack(fill=BOTH,expand=True)

# Creating Frames To Paned Window
frame1 = ttk.Frame(pan_win,width=300,height=200,relief=SUNKEN)
frame2 = ttk.Frame(pan_win,width=200,height=200,relief=SUNKEN)
frame3 = ttk.Frame(pan_win,width=100,height=200,relief=SUNKEN)

# Adding Frames To Paned Window Using 'add' function
pan_win.add(frame1,weight=1)
pan_win.add(frame2,weight=3)

# Adding Frames To Paned Window Using 'insert' function
pan_win.insert(1,frame3) # (Column no , frame name)

# Note:-
#When Using The 'insert' function on padding we can manually change the frame size by dragging

# Fixing The Size Of The Window
root.geometry('500x500')

# Adding Labels And Button

# Frame 1
lab_tit1 = Label(frame1,text='Frame 1').grid(row=0,column=0,padx=10,pady=10)
lab1 = Label(frame1,text='Hello World').grid(row=1,column=0,padx=10,pady=10)
button1 = ttk.Button(frame1,text='Click Me').grid(row=2,column=0,padx=10,pady=10)

# Frame 2
lab_tit2 = Label(frame2,text='Frame 2').grid(row=0,column=0,padx=10,pady=10)
lab2 = Label(frame2,text='Hello World').grid(row=1,column=0,padx=10,pady=10)
button2 = ttk.Button(frame2,text='Click Me').grid(row=2,column=0,padx=10,pady=10)

# Frame 3
lab_tit3 = Label(frame3,text='Frame 3').grid(row=0,column=0,padx=10,pady=10)
lab3 = Label(frame3,text='Hello World').grid(row=1,column=0,padx=10,pady=10)
button3 = ttk.Button(frame3,text='Click Me').grid(row=2,column=0,padx=10,pady=10)

# Displaying The Window
root.mainloop()