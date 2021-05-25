from tkinter import *
from tkinter import ttk

# Creating Object for the window
root = Tk()

# Creating title for the window
root.title('List Box')

# Fixing the size of the window
root.geometry('300x300')

# Creating object for extracting items
def display():
    selected_items = listbox.curselection()
    for item in selected_items:
        print(listbox.get(item))

# Creating object for deleting items
def delete():
    delete_items = listbox.curselection()
    for item in delete_items:
        listbox.delete(item)

# Creating The List box object
listbox = Listbox(root,width=40,height=10,
                  selectmode=MULTIPLE) # By Changing the selectmode to multiple we can select multiple items
listbox.pack()

# Inserting Items on the list box
listbox.insert(0,'Python')
listbox.insert(1,'C++')
listbox.insert(2,'C')
listbox.insert(3,'Java')
listbox.insert(4,'PHP')

# Creating button for extracting the selected items
button1 = ttk.Button(root,text='Print',command=display).place(x=65,y=200)
button2 = ttk.Button(root,text='Delete',command=delete).place(x=160,y=200)

# Displaying The Window
root.mainloop()