from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import mysql.connector as con
from createsqltable import passwrd
db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to establish connection between python and books
def root1():
    root = Tk()
    root.title("Ebook store ")
    root.configure(width=1500,height=600,bg="light blue")
    var=-1
    root.geometry("1000x500") 
            
    cursor=db.cursor()
    
    label= Label(root,text="      ---- DELETE BOOK FROM BOOK STORE ---- ",bg="light blue",fg="dark blue",font=("rockwell", 30))
    label.grid(columnspan=6, padx=10, pady=40)

   
    #====================================================================================================================================================================================================================================================    
    def deleteitem():
        
        temp=int(bookid1.get())
        
        
        try:
            sql = "delete from stocks where bookid='%d'" % (temp)
            
            
            cursor.execute(sql)
            db.commit()
            print("Book deleted")
            
            messagebox.showinfo("-- complete --", "succesfully deleted the book",icon="info")
            root.destroy()
            root1()
        except Exception as e:
            print (e)
            db.close()
          
    label1=Label(root,text="enter book id :",bg="blue",relief="groove",fg="white",font=("rockwell", 18),width=33)
   
    
    l1=[]
    sql="select distinct bookid from stocks"
    cursor.execute(sql)
    l=cursor.fetchall()
    for j in l:
        for i in j:
            l1+=[i]
        
    try:
        
        
        bookid1=ttk.Combobox(root,values=l1,width=27,font='bold')
        bookid1.current(0)
        bookid1.grid(row=7,column=1)
        
    except:
        messagebox.showinfo("-- incomplete --", "No books in the shelf..!!",icon="warning")


    


    button2= Button(root, text="delete book", bg="blue", fg="white", width =20, font=("rockwell", 18),command=deleteitem)
    label1.grid(row=7,column=0, sticky=W, padx=50, pady=40)
    button2.grid(row=9,column=1, padx=40, pady=40)

    #====================================================================================================================================================================================================================================================
    def back():
        root.destroy()
        import admnchoice
        
    button5= Button(root, text="back ", bg="blue", fg="white", width=10, font=("rockwell", 18),command=back)
    button5.grid(row=9,column=0, padx=40, pady=40)
    root.mainloop()
        
#====================================================================================================================================================================================================================================================
