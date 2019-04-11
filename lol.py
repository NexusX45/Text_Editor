from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox

#Initialization

top = Tk()
top.title('A Simple Text Editor')
txt = scrolledtext.ScrolledText(top, width = 100, height = 80)

#Functions

def savefile():
    file = filedialog.asksaveasfile(mode='w', filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))
    data = txt.get('1.0', END+'-1c')
    file.write(data)
    file.close()

def openfile():
    file = filedialog.askopenfile(mode='rb')
    contents = file.read()
    txt.insert('1.0', contents)
    file.close()

def newfile():
    txt.delete('1.0', END)

def exitfile():
    if messagebox.askyesno("Quit", 'Are you sure you want to exit'):
        top.destroy()

def about():
    messagebox.askokcancel('About', 'This editor was made by NexusX45-Sama !!!')

#Menu

menubar= Menu(top)
filemenu = Menu(menubar)
filemenu.add_command(label = "New", command = newfile)
filemenu.add_command(label = "Open", command = openfile)
filemenu.add_command(label = "Save", command = savefile)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = exitfile)
menubar.add_cascade(label="File", menu = filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label = "About", command = about)
menubar.add_cascade(label = "Help", menu = editmenu)

top.config(menu = menubar)
txt.pack()
top.mainloop()