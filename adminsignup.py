from tkinter import *
from tkinter import messagebox
from createsqltable import passwrd

import mysql.connector
db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to establish connection between python and books

        
cursor=db.cursor()
def root1():
    root = Tk()
    root.title("Ebook store ")
    root.configure(width=3500,height=2600,bg='light blue')
    root.geometry("1050x600")
    var=-1
    label= Label(root,text="---- CUSTOMER LOGIN SYSTEM ----",bg="light blue",fg="dark blue",font=("rockwell", 29,))
    label.grid(columnspan=6, padx=200, pady=80)

    label1=Label(root,text="login ID :",bd=3,bg="blue",relief="groove",fg="WHITE",font=("rockwell", 18),width=40)
    entry1=Entry(root , font=("rockwell", 15),bd=3)
    label2=Label(root, text="create a password :",bd=3,relief="groove",height="1",bg="blue",fg="white", font=("rockwell", 18),width=40)
    entry2= Entry(root, font=("rockwell", 15),bd=3,show='*')
    label3=Label(root, text="company code:",bd=3,relief="groove",height="1",bg="blue",fg="white", font=("rockwell", 18),width=40)
    entry3= Entry(root, font=("rockwell", 15),bd=3)
    #====================================================================================================================================================================================================================================================
    def password():
        
        
        if entry3.get()=='1234':            #CHECKS THE PASSCODE
        
            a=entry1.get()
                                   #GETS THE USERNAME AND PASSWORD (WHICH TO BE MODIFIED)
            b=entry2.get()
            
            sql=' update pass set password="%s" where ussername="%s"' % (b,a)
            cursor.execute(sql)
            db.commit()
            messagebox.showinfo("-- complete--", "Password Successfully Changed .",icon="info")
        else:
            messagebox.showinfo("-- error --", "Please enter valid code!", icon="warning")

    #====================================================================================================================================================================================================================================================
    def login():
        root.destroy()                      #LOG IN SYSYTEM 
        import login
        login.root1()

    #====================================================================================================================================================================================================================================================
    label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
    label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
    label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
    entry1.grid(row=1,column=1, padx=40, pady=10)
    entry2.grid(row=2,column=1, padx=10, pady=10)
    entry3.grid(row=3,column=1, padx=10, pady=10)
    button1= Button(root, text="change password!",bd=3, bg="blue", fg="white", width=20, font=("rockwell", 18),command=password)
    button1.grid(row=4,column=1, padx=40, pady=80)
    button2= Button(root, text="login admin!",bd=3, bg="blue", fg="white", width=20, font=("rockwell", 18),command=login)
    button2.grid(row=4,column=0, padx=40, pady=80)

        
    root.mainloop()


#====================================================================================================================================================================================================================================================
