from tkinter import *
from tkcalendar import DateEntry
import sqlite3
root=Tk()
root.geometry("800x900")
root.title("Expense tracker")
root.iconbitmap('et.ico')
#setting first and second frame
f1 = Frame(root,bg="#f2ddbd", borderwidth=2,relief="groove")
f2=Frame(root,bg="#e4f5e8", borderwidth=2,relief="groove")
f2.pack(fill=X)
f1.pack(fill=X)
#label for new entry
Label( f2 , text="New entry",bg="#e4f5e8").grid(row=0,column=0 ,padx=(31, 31))
#these are variavles to check wheather values are for deposit or withdraw
CheckVar1 = IntVar()      #variable for Depositing
CheckVar2 = IntVar()        #variable for withdraw
def cb():
    if CheckVar1.get()==1 and CheckVar2.get()==1:
        CheckVar1.set(0)
        CheckVar2.set(0)    
C1 = Checkbutton (f2, text = "Deposited",bg="#e4f5e8",selectcolor="#a1fc03",relief=GROOVE, variable = CheckVar1, \
                  onvalue = 1, offvalue = 0, height=2, \
                 width = 15,command=cb)
C2 = Checkbutton (f2, text = "withdrawn",bg="#e4f5e8",selectcolor="red",relief=GROOVE , variable = CheckVar2, \
                  onvalue = 1, offvalue = 0, height=2, \
                 width = 15,command=cb) 
#function for making frame reponsive
n_rows =1
n_columns =1
for i in range(n_rows):
    f2.grid_rowconfigure(i,  weight =1)
for i in range(n_columns):
    f2.grid_columnconfigure(i,  weight =1)    
C1.grid(row=0,column=1, padx=(91, 2))
C2.grid(row=0,column=2, padx=(0, 11),pady=(10, 11))
#second frame starts here 
amount = IntVar()
note = StringVar()
date =StringVar()

Label( f1 , text="Ammount   (In Rupees)  :",bg="#f2ddbd").grid(row = 1,column = 1)
a1 = Entry(f1,textvariable=amount ).grid(row = 1,column = 2, padx=(0, 0),pady=(5, 11),ipady=6,ipadx=17)
Label( f1 , text="Entry Name / Note   : ",bg="#f2ddbd").grid(row = 1,column = 3)
b1 = Entry(f1,textvariable=note).grid(row = 1,column = 4, padx=(0, 0),pady=(5, 11),ipady=7,ipadx=27)

cal = DateEntry(f1,textvariable=date, width=12, year=2019, month=6, day=22, 
background='#e4f5e8', foreground='black', borderwidth=2)
cal.grid(row = 1,column = 5, padx=(0,90),pady=(10, 11),ipady=7)

Label( f1 , text=" Select payment method   : ",bg="#f2ddbd").grid(row = 2,column = 1)
OPTIONS = ['Cash','Checks','Debit cards','Credit cards','UPI''none']
variable = StringVar(f1)
variable.set(OPTIONS[0]) 
w = OptionMenu(f1, variable, *OPTIONS)
w.grid(row=2, column=2,padx=(0, 0),pady=(5, 11),ipady=5,ipadx=27)
Label( f1 , text="  Select account  : ",bg="#f2ddbd").grid(row = 2,column = 3)
OPTIONS =  ['proffessional','personal']
variable2 = StringVar(f1)
variable2.set(OPTIONS[0])
w = OptionMenu(f1, variable2, *OPTIONS)
w.grid(row=2, column=4,padx=(0, 0),pady=(5, 11),ipady=5,ipadx=27)
def submit():
    
    print(amount.get())
    print(note.get())
    print(date.get())
    print(variable2.get())
    print(variable.get())
    if CheckVar1.get()==1 and CheckVar2.get()==0 :
        print("depostiting")
    elif CheckVar2.get()==1 and CheckVar1.get()==0 :
        print("withdrawing")
        

MyButton1 = Button(f1, text="save entry", width=10,bg="skyblue",fg="black",command=submit)
MyButton1.grid(row=2, column=5,padx=(0, 70))
rows=3
columns=6
for i in range(rows):
    f1.grid_rowconfigure(i,  weight =1)
for i in range(columns):
    f1.grid_columnconfigure(i,  weight =1)
    
root.mainloop()