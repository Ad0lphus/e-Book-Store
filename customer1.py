#customer first page

from tkinter import *
import mysql.connector as con
from tkinter import messagebox
import random
import shopping
from createsqltable import *

def cus1():                                                                                                                      #user sign in page
    
    global master
    master=Tk()
    master.title("Users page")
    master.configure(width=3500,height=2600,bg='light blue')
    Label(master,text="Hi..",bg='light blue',fg="dark blue",width=55,font=("rockwell",27)).grid(row=0,column=2,columnspan=1,rowspan=2,padx=10)
    Button(master,text="sign in as an already existing customer",command=signin,font=("rockwell",18),bg="blue",fg="white",width=50).grid(row=2,column=1,columnspan=3,rowspan=2,padx=5,pady=10)
    Button(master,text="register as a new user",font=("rockwell",18),command=new,bg="blue",fg="white",width=50).grid(row=4,column=1,columnspan=3,rowspan=2,padx=5,pady=10)
    Button(master,text="continue without sign in",command=nsign,bg="blue",fg="white",font=("rockwell",18),width=50).grid(row=6,column=1,columnspan=3,rowspan=2,padx=5,pady=10)
    master.mainloop()
#====================================================================================================================================================================================================================================================
def new1():
    global user
    
    if len(entry1.get())==0:
        messagebox.showinfo("Alert..","Please enter user name..")

    elif len(entry2.get())==0:
        messagebox.showinfo("Alert..","Please enter password..")
        
                                                                                                #if any entry is missing 
     
    elif len(entry3.get())==0:
        messagebox.showinfo("Alert..","Please Re-enter password..")

    elif entry2.get()!=entry3.get():
        messagebox.showinfo("Alert..","Passwords doesn't match...")
    elif len(entry4.get())==0 or len(entry5.get())==0 or len(entry6.get())==0:
        
        messagebox.showinfo("Alert..","Please fill in all the columns..")

    else:
        entry2.get()==entry3.get()                                                             #comparing both passwords
        print("User successfully registered")
        uname=entry1.get()
        password=entry2.get()
        age=entry4.get()
        contactno=entry5.get()
        billingadd=entry6.get()
        
        uid=random.randint(10000,99999)
        sql="insert into users values("+str(uid)+",'"+uname+"','"+password+"',"+str(age)+","+str(contactno)+",'"+billingadd+"');"
        
        cur.execute(sql)
        
        mycon.commit()
        mycon.close()
        master1.destroy()
        user=(uid,uname)                                                                                # Flag to identify if the user is signed in or not and also to uniquely identify the user
        print("User successfully signed in..")
        enter()


#====================================================================================================================================================================================================================================================
def clear1():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')                                      #Clearing the entries
    entry4.delete(0,'end')
    entry5.delete(0,'end')
    entry6.delete(0,'end')


#====================================================================================================================================================================================================================================================    
def clear2():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
#====================================================================================================================================================================================================================================================
def back1():
    master1.destroy()
    cus1()                                                  #Going back to the homepage
#====================================================================================================================================================================================================================================================
def back2():
    master2.destroy()
    cus1()
#====================================================================================================================================================================================================================================================    
def signin():                                                           #user sign in page
    
    global entry1,entry2,master2
    master.destroy()
    master2=Tk()
    master2.configure(width=3500,height=2600,bg='light blue')
    master2.title("sign in")
    Label(master2,text="user sign in",bg='light blue',font=("rockwell",30)).grid(row=0,column=0,columnspan=2)
    Label(master2,text="enter username:",bg='blue',fg="white",font=("rockwell",18)).grid(row=3,column=0,pady=40)
    entry1=Entry(master2)
    entry1.grid(row=3,column=2,pady=40)
    Label(master2,text="enter password:",bg='blue',fg="white",font=("rockwell",18)).grid(row=5,column=0,pady=40)
    entry2=Entry(master2,show="*")
    entry2.grid(row=5,column=2,pady=40)
    Button(master2,text="submit",bg="blue",fg="white",command=ver).grid(row=6,column=2,sticky=SE)
    Button(master2,text="clear records",bg="blue",command=clear2).grid(row=6,column=1,sticky=W)
    Button(master2,text="go back",bg="blue",fg="white",command=back2).grid(row=6,column=0,sticky=SW)
#====================================================================================================================================================================================================================================================
def ver():
    
    global user
    uname=entry1.get()
    password=entry2.get()
    sql="select uid from users where uname='"+uname+"' and password='"+password+"';"
    cur.execute(sql)
    data=cur.fetchall()                                                                                 #No such record exists
    if len(data)==0:
        messagebox.showinfo("Alert....","username or password is invalid")
    else:
        master2.destroy()
        print("signed in successfully")
        user=(data[0][0],uname)
        enter()
#====================================================================================================================================================================================================================================================
def nsign():
    global user
    print("user entered without signing in..")
    master.destroy()
    user=[0,"user"]                                                                             #flag to identify that user has entered without signing in
    enter()
    
        
        
    
    
#====================================================================================================================================================================================================================================================


def new():                                                                                                          #New registration
    global entry1,entry2,entry3,entry4,entry5,entry6,master1
    master.destroy()
    master1=Tk()
    master1.title("New user")
    master1.configure(width=3500,height=2600,bg='light blue')
    Label(master1,text=" new User registration",bg='light blue',font=("rockwell",20)).grid(row=0,column=0,columnspan=1,rowspan=1,pady=20)
    Label(master1,text="enter username:",bg='light blue',font=("rockwell",15)).grid(row=1,column=0,pady=20)
    entry1=Entry(master1)
    entry1.grid(row=1,column=1,pady=20)
    Label(master1,text="enter password:",bg='light blue',font=("rockwell",15)).grid(row=2,column=0,pady=10)
    entry2=Entry(master1,show="*")
    entry2.grid(row=2,column=1,pady=10)
    Label(master1,text="confirm password:",bg='light blue',font=("rockwell",15)).grid(row=3,column=0,pady=10)
    entry3=Entry(master1,show="*")
    entry3.grid(row=3,column=1,pady=10)
    Label(master1,text="enter age:",bg='light blue',font=("rockwell",15)).grid(row=4,column=0,pady=10)
    entry4=Entry(master1)
    entry4.grid(row=4,column=1,pady=10)
    Label(master1,text="enter contact no:",bg='light blue',font=("rockwell",15)).grid(row=5,column=0,pady=10)
    entry5=Entry(master1)
    entry5.grid(row=5,column=1,pady=10)
    Label(master1,text="enter billing address:",bg='light blue',font=("rockwell",15)).grid(row=6,column=0,pady=10)
    entry6=Entry(master1)
    entry6.grid(row=6,column=1,pady=10)
    Button(master1,text="submit",bg="blue",fg="white",command=new1).grid(row=7,column=2,pady=20,sticky=SE)
    Button(master1,text="clear records",bg="blue",command=clear1).grid(row=7,column=1,pady=20,sticky=S)
    Button(master1,text="go back",bg="blue",fg="white",command=back1).grid(row=7,column=0,pady=20,sticky=SW)

#====================================================================================================================================================================================================================================================

def enter():
    shopping.initialize(user)
    print("user successfully logged out")
    cus1()

#====================================================================================================================================================================================================================================================
mycon=con.connect(host="localhost",user="root",password=passwrd,database="books")

cur=mycon.cursor()
user=None

