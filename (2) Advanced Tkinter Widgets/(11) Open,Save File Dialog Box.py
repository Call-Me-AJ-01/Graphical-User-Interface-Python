from tkinter import *
from tkinter import ttk
from tkinter import filedialog

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Creating Object For The Window
root = Tk()

# Declaring The Title For The Window
root.title('Open and Save Dialog Box')

# Creating Function For Button
def open_file():
    filename = filedialog.askopenfilename(initialdir='/',title='Select File',
                                          filetypes=(('Text File','.txt'),('All Files','*.*')))

    # Read The Text File
    content = open(filename).read()

    # Writing The Content Of The Text File On The Text Box
    text.delete(0.0,END)
    text.insert(INSERT,content)

def save_file():
    save = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if save is None:
        return
    content = text.get(0.0,END)
    save.write(content)

# Creating TextField
text = Text(root,width=30,height=15,wrap=WORD)
text.pack(pady=50)
text.insert(INSERT,'Select A Text File To View That In This Text Box\n\n Note:- Select A Text File \n\n\t      OR\n\nNote:- Write Something On The Text Box And Press Save File To Save The Entered Text in a Text Format')

# Creating Button
button = ttk.Button(root,text='Open File',command=open_file)
button.pack(pady=5,padx=(100,10),side=LEFT)

button1 = ttk.Button(root,text='Save File',command=save_file)
button1.pack(pady=10,padx=(10,10),side=LEFT)

# Fixing The Size Of The Window
root.geometry('450x500')

# Displaying The Window
root.mainloop()