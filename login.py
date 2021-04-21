from tkinter import *
from tkinter import messagebox
import mysql.connector
from createsqltable import passwrd
db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to establish connection between python and books

        
cursor=db.cursor()


def root1():
   global root
   root = Tk()
   root.title("Ebook store ")
   root.configure(width=3500,height=2600,bg="light blue")
   root.geometry("1150x600") 
   var=-1
   
   label= Label(root,text="---- LOGIN SYSTEM ----",bd=15,bg="light blue",fg="dark blue",font=("rockwell", 30))
   label.grid( padx=10, pady=40)
   
   #====================================================================================================================================================================================================================================================
   
   label1=Label(root,text="Enter login id:",bg="blue",bd=3,relief="groove",fg="white",font=("rockwell", 18),width=45)
   entry1=Entry(root , font=("rockwell", 18),bd=3)
   label2=Label(root, text="Enter password :",bd=3,relief="groove",height="1",bg="blue",fg="white", font=("rockwell", 18),width=45)
   entry2= Entry(root, font=("rockwell", 18),show='*',bd=3)

   label1.grid(row=4,column=0, sticky=W, padx=40, pady=40)
   label2.grid(row=6,column=0, sticky=W, padx=40, pady=40)
   entry1.grid(row=4,column=1, padx=40, pady=40)
   entry2.grid(row=6,column=1, padx=40, pady=40)

   

   up=0  
   def trylogin():
      sql = "SELECT * FROM pass" 
      cursor.execute(sql)              #GETS INFO FROM THE SAVED USERNAME AND PASSWORD
      results = cursor.fetchall()
      up=0
         
      for c in results:
         if c[0]==entry1.get() and c[1]==entry2.get():      #CHECKS WEATHER PASSWORD AND USERNAME IS CORECT OR NOT
            up=1
            
      
         
      if up==1:
               
         
         messagebox.showinfo("-- complete --", "you have now logged in..",icon="info")
         root.destroy()
         import admnchoice
         admnchoice.root1()
         
            
            

      else:
         
         messagebox.showinfo("-- error --", "Please enter valid infomation", icon="warning")
   #====================================================================================================================================================================================================================================================
   def newadmin():
      messagebox.showinfo("-- complete your profile --", "Give neccesary information",icon="info")
      root.destroy()
      import adminsignup
      adminsignup.root1()
   #====================================================================================================================================================================================================================================================

   def back():
        root.destroy()
        import frontwindow
        frontwindow.main()   
   #====================================================================================================================================================================================================================================================
     
   button1= Button(root, text="login admin",bd=3, bg="blue", fg="white", width=20, font=("rockwell", 18),command=trylogin)
   button1.grid(row=8,column=1, padx=40, pady=40)
   button2= Button(root, text="forgot password?",bd=3, bg="blue", fg="white", width=20, font=("rockwell", 18),command=newadmin)
   button2.grid(row=8,column=0, padx=40, pady=40)
   button5= Button(root, text="back",bd=3, bg="blue", fg="white", width=15, font=("rockwell", 18),command=back)
   button5.grid(row=0,column=1, padx=80, pady=40,sticky=E)
   root.mainloop()


#====================================================================================================================================================================================================================================================
