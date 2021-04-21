from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from createsqltable import passwrd
db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to establish connection between python and books


import mysql.connector as con

        
cursor=db.cursor()
def root1():
    
    def clearitem():
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)                   #FUNCTION TO CLEAR THE ENTRIES
        entry5.delete(0, END)
        entry7.delete(0, END)
        entry8.delete(0, END)
        entry9.delete(0, END)
    #====================================================================================================================================================================================================================================================


    
    def additem():                              #FUNCTION TO ADD BOOK 
        
        bookid,aname,a1name,title,price,year,discription,numberC,cat=entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry7.get(),entry8.get(),entry9.get(),cat1.get()
        
        
        sql="INSERT INTO stocks(bookid,aname,a1name,title,price,year,discription,numberC,cat) VALUES ( '%s' ,'%s','%s','%s','%s' ,'%s','%s','%s','%s')"%(bookid,aname,a1name,title,price,year,discription,numberC,cat)
        
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo("-- complete --", "book successfully added!!..",icon="info")
        
        clearitem()

                    
    #====================================================================================================================================================================================================================================================
    root = Tk()
    root.title("Ebook store ")
    root.configure(width=1500,height=600,bg="light blue")
    root.geometry("1000x730") 

    var=-1

    
    label= Label(root,text="        ---- ADD BOOK TO THE STORE ---- ",bg="light blue",fg="dark blue",font=("rockwell", 30))
    
    label1=Label(root,text="enter book id:",bg="blue",relief="groove",fg="white",font=("rockwell", 15),width=45)
    entry1=Entry(root , font=("rockwell", 20),bd=3)
    
    label2=Label(root, text="enter author's name:",bd="3",relief="groove",height="1",bg="blue",fg="white", font=("rockwell", 15),width=45)
    entry2= Entry(root, font=("rockwell", 20),bd=3)
    
    label3=Label(root, text="enter author's surname:",bd="3",relief="groove",bg="blue",fg="white", font=("rockwell", 15),width=45)
    entry3= Entry(root, font=("rockwell", 20),bd=3)
    
    label4=Label(root, text="enter book title:",bd="3",relief="groove",bg="blue",fg="white", font=("rockwell", 15),width=45)
    entry4= Entry(root, font=("rockwell", 20),bd=3)
    
    label5=Label(root, text="eenter book price:",bg="blue",relief="groove",fg="white", font=("rockwell", 15),width=45)
    entry5= Entry(root, font=("rockwell", 20),bd=3)
    
    label7=Label(root, text="enter date of publication(yyyy-mm-dd) :",bd="3",relief="groove",height="1",bg="blue",fg="white", font=("rockwell", 15),width=45)
    entry7= Entry(root, font=("rockwell", 20),bd=3)
    
    label8=Label(root, text="enter description about the book:",bd="3",relief="groove",bg="blue",fg="white", font=("rockwell", 15),width=45)
    entry8= Entry(root, font=("rockwell", 20),bd=3)
    
    label9=Label(root, text="eneter no of copies :",bd="3",relief="groove",bg="blue",fg="white", font=("rockwell", 15),width=45)
    entry9= Entry(root, font=("rockwell", 20),bd=3)
    
    label10=Label(root, text="enter the catogory :",bd="3",relief="groove",bg="blue",fg="white", font=("rockwell", 15),width=45)
    button1= Button(root, text="add book", bg="blue", fg="white", width=20, font=("rockwell", 15),command=additem)
    

    label.grid(row=1,columnspan=6, padx=10, pady=40)
    label1.grid(row=3,column=0, sticky=W, padx=10, pady=10)
    label2.grid(row=4,column=0, sticky=W, padx=10, pady=10)
    label3.grid(row=5,column=0, sticky=W, padx=10, pady=10)
    label4.grid(row=6,column=0, sticky=W, padx=10, pady=10)
    label5.grid(row=7,column=0, sticky=W, padx=10, pady=10)
    label7.grid(row=10,column=0, sticky=W, padx=10, pady=10)
    label8.grid(row=11,column=0, sticky=W, padx=10, pady=10)
    label9.grid(row=12,column=0, sticky=W, padx=10, pady=10)
    label10.grid(row=13,column=0, sticky=W, padx=10, pady=10)

    
    entry1.grid(row=3,column=1, padx=40, pady=10)
    entry2.grid(row=4,column=1, padx=10, pady=10)
    entry3.grid(row=5,column=1, padx=10, pady=10)
    entry4.grid(row=6,column=1, padx=10, pady=10)
    entry5.grid(row=7,column=1, padx=10, pady=10)
    entry7.grid(row=10,column=1, padx=10, pady=10)
    entry8.grid(row=11,column=1, padx=10, pady=10)
    entry9.grid(row=12,column=1, padx=10, pady=10)

    
    
    l=["Fantasy","Science","fiction","Western","Romance","Thriller","Mystery","Detective story","Dystopia","Memoir","AutoBiography","Play","Musical","Satire","Haiku","HorrorDIY","Dictionary","Children's literature"]
    cat1=ttk.Combobox(root,values=l,width=30,font='bold')
    cat1.current(0)
    cat1.grid(row=13,column=1,pady=13)                                      #ALL THe CATOGORIES AVAILABLE
    button1.grid(row=15,column=1, padx=40, pady=40)
    
    #====================================================================================================================================================================================================================================================

    
    def back():
        root.destroy()                                  #FUNCTION TO GO BACK 
        import admnchoice
        
    button5= Button(root, text="back", bg="blue", fg="white", width=10, font=("rockwell", 15),command=back)
    button5.grid(row=15,column=0, padx=40, pady=40)

    #====================================================================================================================================================================================================================================================

    root.mainloop()

#====================================================================================================================================================================================================================================================
