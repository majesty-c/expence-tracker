from tkinter import*
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image

mydb=mysql.connector.connect(host='localhost',user='root',password='1437869292',database='expence_c')
#print(mydb.connection_id)
cur=mydb.cursor()
def insert():
  if (Password.get()=="") or (RegistrationNo.get()=="")or(PhoneNumber.get()=="")or(ConfirmPassword.get()==""):
        messagebox.showinfo('Error','Many fields are Empty')
  elif(Password.get()==ConfirmPassword.get()and PhoneNumber.get().isdigit()):
    s="create table IF NOT EXISTS customers(Ename varchar(20),Lname varchar(30),RegistrationNo integer(20),PhoneNumber varchar(20),Password varchar(20),ConfirmPassword varchar(20))"
    cur.execute(s)
    s2="insert into customers(Ename,Lname,RegistrationNo,PhoneNumber,Password,ConfirmPassword) values(%s,%s,%s,%s,%s,%s)"
    b=(Fname.get(),Lname.get(),RegistrationNo.get(),PhoneNumber.get(),Password.get(),ConfirmPassword.get())
    cur.execute(s2,b)
    messagebox.showinfo('WELCOME','Register Successfully')
    mydb.commit()
  else:
    messagebox.showinfo('Error','please enter same password for both field')
    
#cREATING GUI
master=Tk()
#background image and tittle for full window
master.title("Welcome")
image2 =Image.open('E:/New folder (3)/new.jpg')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
master.geometry('%dx%d+0+0' % (w,h)) 
label1 = Label(master, image=image1)
label1.pack()
#background image for small window
Frame_login1=Frame(master,bg='lightblue')
Frame_login1.place(x=100,y=150,height=400,width=400)
image3=Image.open('E:/New folder (3)/login-icon-3036.png')
image4 = ImageTk.PhotoImage(image3)
label= Label(Frame_login1, image=image4)
label.pack()

#create variables for accesing Entry Boxes and Tables:
Fname=StringVar()
Lname=StringVar()
RegistrationNo=StringVar()
PhoneNumber=StringVar()
Password=StringVar()
ConfirmPassword=StringVar()
status=StringVar()
#Creating label for instructing the user:
#function for nextpage call
def call():
    master.destroy()
    import login
#frame for register
Frame_login=Frame(master,bg='lightgray')
Frame_login.place(x=600,y=150,height=400,width=700)
Label(Frame_login,text='SIGN UP HERE:',bg='lightgray',font=("Impact",20,'roman',),fg='red').place(x=220,y=35)
Label(Frame_login,text='first Name:',bg='lightgray',font=("Impact",12,'roman'),fg='#2F4F4F').place(x=70,y=80)
Label(Frame_login,text='Last Name:',bg='lightgray',font=("Impact",12,'roman'),fg='#2F4F4F').place(x=360,y=80)
Label(Frame_login,text='RegistrationNo:',bg='lightgray',font=("Impact",12,'roman'),fg='#2F4F4F').place(x=70,y=150)
Label(Frame_login,text='Phone Number:',bg='lightgray',font=("Impact",12,'roman'),fg='#2F4F4F').place(x=360,y=150)
Label(Frame_login,text='Password:',bg='lightgray',font=("Impact",12,'roman'),fg='#2F4F4F').place(x=70,y=230)
Label(Frame_login,text='Confirm Password:',bg='lightgray',font=("Impact",12,'roman'),fg='#2F4F4F').place(x=360,y=230)
Label(Frame_login,text=status,textvariable=status).place(x=70,y=400)
#create boxes for taking input
a=Entry(Frame_login,bg='lightgray',font=("times new roman",17,'roman'), textvariable=Fname).place(x=70,y=110)
Entry(Frame_login,bg='lightgray',font=("times new roman",17,'roman'), textvariable=Lname).place(x=360,y=110)
Em=Entry(Frame_login,bg='gray',font=("times new roman",16,'roman'), textvariable=RegistrationNo).place(x=70,y=190)
Entry(Frame_login,bg='gray',font=("times new roman",16,'roman'), textvariable=PhoneNumber).place(x=360,y=190)
pas=Entry(Frame_login,bg='pink',show='*',font=("times new roman",16,'roman'), textvariable=Password).place(x=70,y=260)
Entry(Frame_login,bg='pink',show='*',font=("times new roman",16,'roman'), textvariable=ConfirmPassword).place(x=360,y=260)
#Adding Button for Submitting Data:
#columnspane decide how much column space is to be Given
#ccc
Button(Frame_login1,text='LOgin',bg='#2F4F4F',font=("Impact",10,'italic'),fg='#FF1493',command=call).place(x=200,y=330,width=110)
but=Button(Frame_login,text='Submit',bg='#2F4F4F',font=("Impact",10,'italic'),fg='#FF1493',command=insert).place(x=250,y=330,width=110)
mainloop()
messagebox.showinfo(status)

