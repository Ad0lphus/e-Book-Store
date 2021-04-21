from tkinter import *
from tkinter import messagebox

import mysql.connector
from createsqltable import passwrd
from tkinter import ttk
import mysql.connector as con

db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to establish connection between python and books
def root1():
    root = Tk()
    root.title("Ebook store ")
    root.configure(width=3500,height=2600,bg="light blue")
    root.geometry("1000x500") 
    var=-1
    cursor=db.cursor()
    
    #=====================================================================================================================================================    
        
    def updateitem():                   #FUNCTION TO UPDATE BOOK
        global uid
        uid=uid1.get()
        no1=int(no.get())
        tempst=uid
        sql = "Update stocks set numberC='%d' where bookid='%s'" % (no1,tempst)
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo("-- complete --", "succesfully updated the status of the book..",icon="info")
                
    #=====================================================================================================================================================    

    label= Label(root,text="       ---- UPDATE STATUS OF THE BOOK ---- ",bg="light blue",fg="dark blue",font=("rockwell", 30))
    label.grid(columnspan=6, padx=40, pady=40)
    label1=Label(root,text="enter book id:",bg="blue",relief="groove",fg="white",font=("rockwell", 18),width=37)
    #=====================================================================================================================================================
    sql = "select distinct bookid from stocks" 
    cursor.execute(sql)
    l1=[]
    l = cursor.fetchall()
    for j in l:
        for i in j:
            l1+=[i]
    
        
    l2=[]
    
    for k in range(0,101):
        l2+=[k]
    no=ttk.Combobox(root,values=l2,width=30,font='bold')
    no.current(0)
    no.grid(row=7,column=1)    
    
    try:
        
        
        uid1=ttk.Combobox(root,values=l1,width=30,font='bold')
        uid1.current(0)
        uid1.grid(row=6,column=1)
        
    except:
        messagebox.showinfo("-- incomplete --", "no books in the shelf..!!",icon="warning")

    
    label6=Label(root,text="no: of books available:",bg="blue",relief="groove",fg="white",font=("rockwell", 18),width=37)
    
    label1.grid(row=6,column=0, sticky=W, padx=10, pady=20)
    label6.grid(row=7,column=0, sticky=W, padx=10, pady=40)
    button3= Button(root, text="update status" , bg="blue", fg="white", width =20, font=("rockwell", 18),command=updateitem)
    button3.grid(row=14,column=1, padx=40, pady=40)
    #=====================================================================================================================================================
    def back():
        root.destroy()                  #FUNCTION TO GO BACK
        import admnchoice

    #=====================================================================================================================================================
        
    button5= Button(root, text="back ", bg="blue", fg="white", width=10, font=("rockwell", 18),command=back)
    button5.grid(row=14,column=0, padx=40, pady=40)
    root.mainloop()

#=====================================================================================================================================================

