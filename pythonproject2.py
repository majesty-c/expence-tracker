from tkinter import *
from tkcalendar import DateEntry
import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
def create_project(conn, project):
    sql = ''' INSERT INTO project(amount,note,begin_date,account,method,committing)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid
database = r"db7.db"
conn = create_connection(database)
def main():
   
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS project(
                                        id integer PRIMARY KEY,
                                        amount integer NOT NULL,
                                        note text,
                                        begin_date text,
                                        account text,
                                        method text,
                                        committing text
                                    ); """
    
    if conn is not None:
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")
    create_table(conn, sql_create_projects_table)
    with conn:
        project = submit();
        project_id = create_project(conn, project);
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
cal = DateEntry(f1,textvariable=date, width=12, year=2020, month=11, day=1, 
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
    m=amount.get()
    n=note.get()
    o=date.get()
    p=variable2.get()
    q=variable.get()
    r=CheckVar1.get()
    my_data=(m,n,o,p,q,r)    
    return my_data
MyButton1 = Button(f1, text="save entry", width=10,bg="skyblue",fg="black",command=lambda:[submit(),main()])
MyButton1.grid(row=2, column=5,padx=(0, 70))
rows=3
columns=6
for i in range(rows):
    f1.grid_rowconfigure(i,  weight =1)
for i in range(columns):
    f1.grid_columnconfigure(i,  weight =1)
    
f3 = Frame(root,bg="#f2ddbd", borderwidth=2,relief="groove")
f5 = Frame(root,bg="#e4f5e8", borderwidth=2,relief="groove")
f4=Frame(root,bg="#f2ddbd", borderwidth=2,relief="groove")
f3.pack(fill=Y,side = LEFT)
f4.pack(fill=Y,side = RIGHT)
f5.pack(fill=Y,side=LEFT)


Label( f3 , text="  Start Date  ",bg="#f2ddbd").grid(row=1,column=0 ,padx=(61, 31),pady=(60, 0))
Label( f4 , text="ANALYSIS",bg="#f2ddbd",font='Helvetica 17').grid(row=0,column=0,padx=(48, 45))


cal = DateEntry(f3,textvariable1=date, width=12, year=2020, month=11, day=1, 
background='#e4f5e8', foreground='black', borderwidth=2)
cal.grid(row = 2,column = 0, padx=(10,10),pady=(30, 11),ipady=7)
Label( f3 , text="  End Date  ",bg="#f2ddbd").grid(row=3,column=0 ,padx=(61, 31),pady=(61, 11))
Label( f3 , text="  Filters  ",bg="#f2ddbd",borderwidth=2,relief="groove",font='Helvetica 20').grid(row=0,column=0 ,padx=(0, 0),pady=(0, 0),ipady=10,ipadx=36)
cal = DateEntry(f3,textvariable2=date, width=12, year=2020, month=12, day=1, 
background='#e4f5e8', foreground='black', borderwidth=2)
cal.grid(row = 4,column = 0, padx=(10,10),pady=(20, 11),ipady=7)
MyButton1 = Button(f3, text="filter", width=10,bg="skyblue",fg="black")
MyButton1.grid(row=5, column=0,padx=(40, 40),pady=(40, 40))
Label( f4 , text="  TOTAL MONEY  ",bg="#f2ddbd").grid(row=1,column=0 ,padx=(61, 31),pady=(61, 11))

Label( f4 , text="  MONTHLY MONEY  ",bg="#f2ddbd").grid(row=4,column=0 ,padx=(61, 31),pady=(61, 11))


r_set=conn.execute('''SELECT * from project''');
r1_set=conn.execute('''SELECT * from project LIMIT 32,50''');
sum1=0
diff=0
sum2=0
diff2=0

i=0 # row value inside the loop 
for student in r_set:  

    if student[6]=="1":
            sum1=sum1+student[1]
       
    elif student[6]=="0":
            diff=diff+student[1]
            
            
            
    for j in range(len(student)):
        
        e = Entry(f5, width=10, fg='black',font='Helvetica 18',relief="groove",bg="#e4f5e8") 
        e.grid(row=i, column=j,ipadx=12,ipady=7) 
        e.insert(END, student[j])
     
               
                
    i=i+1

for stuent in r1_set:  

    if stuent[6]=="1":
            sum2=sum2+stuent[1]
       
    elif stuent[6]=="0":
            diff2=diff2+stuent[1]
    i=i+1
print(sum1)
print (diff)
print(sum2)
print (diff2)
Label(f4,text=sum1,bg="#a1fc03",borderwidth=2,relief="groove",font='Helvetica 15').grid(row=2,column=0 ,padx=(0, 0),pady=(21, 0),ipady=17,ipadx=29)
Label(f4,text=diff,bg="red",borderwidth=2,relief="groove",font='Helvetica 15').grid(row=3,column=0 ,padx=(0, 0),pady=(0, 11),ipady=17,ipadx=29)
Label(f4,text=sum2,bg="#a1fc03",borderwidth=2,relief="groove",font='Helvetica 15').grid(row=5,column=0 ,padx=(0, 0),pady=(21, 0),ipady=17,ipadx=29)
Label(f4,text=diff2,bg="red",borderwidth=2,relief="groove",font='Helvetica 15').grid(row=6,column=0 ,padx=(0, 0),pady=(0, 11),ipady=17,ipadx=29)
root.mainloop()





