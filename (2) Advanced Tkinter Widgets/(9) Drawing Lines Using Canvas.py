from tkinter import *

# Creating Object for The Window
root = Tk()

# Declaring Title For The Window
root.title('Drawing Lines Using Canvas')

# Fixing The Size Of The window
root.geometry('500x500')

# Creating Canvas Object
canvas = Canvas(root,width=500,height=500)
canvas.pack()

# Drawing Line
line = canvas.create_line(100,250,360,25) #(x1,y1,x2,y2)
canvas.itemconfigure(line,fill='red',width=5)

# Drawing two lines
line2 = canvas.create_line(2,400,10,300,200,450,fill='green',width=10)
# (x1,y1,x2,y2) Only for the first line two are required
# from the second line onwards one point is enough (x3,y3) this points automatically joins to the previous line

# Creating Text Using Canvas
text = canvas.create_text(50,10,text='AJ Industries',font='timesnewroman 10 bold')

# Creating A rectangle Using Canvas
rectangle = canvas.create_rectangle(30,30,100,150,fill='red',width=5)

# Displaying The Window
root.mainloop()