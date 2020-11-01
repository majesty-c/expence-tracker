from tkinter import*
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image
mydb=mysql.connector.connect(host='localhost',user='root',password='1437869292',database='expence_c')
cur=mydb.cursor()
#function for validating the user after login
def view():
  cur.execute("select * from customers where RegistrationNo=%s and Password=%s",(RegistrationNo.get(),Password.get()))
  row=cur.fetchone()
  #print(row)
  if row==None:
      messagebox.showerror('error','please enter right username and password')
  else:
      messagebox.showinfo('Welcome','Login successfully ')
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
#frame and background image for it
Frame_login1=Frame(master,bg='lightblue')
Frame_login1.place(x=100,y=150,height=400,width=400)
image3=Image.open('E:/New folder (3)/login-icon-3036.png')
image4 = ImageTk.PhotoImage(image3)
label= Label(Frame_login1, image=image4)
label.pack()
#for travelling to next page
def call_Next_Page():
    master.destroy()
    import signup
#Backpage transversing
def call_Back_Page():
    master.destroy()
    import firstPage
#create variables for accesing Entry Boxes and Tables:
RegistrationNo=StringVar()
Password=StringVar()
status=StringVar()
#Creating label for instructing the user:
Frame_login=Frame(master,bg='lightgray')
Frame_login.place(x=600,y=150,height=400,width=500)
Label(Frame_login,text='LOGIN HERE',bg='lightgray',font=("Impact",20,'roman'),fg='red').place(x=150,y=25)
Label(Frame_login,text='Registration Number',bg='lightgray',font=("Impact",13,'roman'),fg='#2F4F4F').place(x=70,y=90)
Label(Frame_login,text='Password:',bg='lightgray',font=("Impact",13,'roman'),fg='#2F4F4F').place(x=70,y=170)
Label(Frame_login,text='',textvariable=status).grid(row=3,column=8)
#Creating Entry Boxes for Taking Input:
Entry(Frame_login,bg='lightgray',font=("serif",17,'bold'), textvariable=RegistrationNo).place(x=70,y=120)
Entry(Frame_login,show='*',bg='gray',font=("serif",17,'roman'), textvariable=Password).place(x=70,y=200)
#Adding Button for Submitting Data:
#columnspane decide how much column space is to be Given
Label(Frame_login,text='New  User ?',bg='lightgray',font=("Impact",13,'underline',),height='2',fg='#2F4F4F').place(x=70,y=270)
Button(Frame_login,text='Sign Up',bg='pink',font=("Impact",12,'roman'),command=call_Next_Page,fg='#2F4F4F').place(x=160,y=270,width=110)
Button(Frame_login1,text='HoMe',bg='#2F4F4F',font=("Impact",10,'italic'),fg='red',command=call_Back_Page).place(x=200,y=330,width=110)
Button(Frame_login,text='lOG IN',bg='pink',font=("Impact",10,'roman'),height='1',command=view,fg='#2F4F4F').place(x=100,y=340,width=110)
mainloop()
messagebox.showinfo(status)

