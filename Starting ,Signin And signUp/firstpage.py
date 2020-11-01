from tkinter import *
from PIL import ImageTk,Image

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
root = Tk()
#for next page Transversing
def call_Next_Page():
    root.destroy()
    import loginpy
#background image and tittle for full window
root.title("Welcome")
image2 =Image.open('E:/New folder (3)/new.jpg')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
root.geometry('%dx%d+0+0' % (w,h))
label1 = Label(root, image=image1)
Label(root,text='ARE   YOU WORRIED . . ?  TRACK  YOUR  DAYS  CALCULATION  ?' ,font=("Impact",20,'roman',),height='2',width='70',fg='#2F4F4F').place(x=400,y=50)
Label(root,text='JuSt CliCk BeLoW' ,font=("Impact",20,'roman'),height='2',width='100',fg='#2F4F4F').place(x=500,y=200,width=500)
Button(root,text='GO...',bg='pink',font=("Impact",14,'roman'),fg='#2F4F4F',width='50',command=call_Next_Page).place(x=800,y=350,width=120)
label1.pack()
#creating manu and its components
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
