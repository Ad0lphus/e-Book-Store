from tkinter import *
from tkinter import messagebox
import mysql.connector
from createsqltable import passwrd
import mysql.connector as con
db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to establish connection between python and books
def root1():
    global root
    root = Tk()
    root.title("Ebook store ")
    root.geometry("1000x500") 

    root.configure(width=1500,height=600,bg='light blue')
    var=-1
    i=''
    cursor=db.cursor()
    
    #==========================================================================================================================================
        
    def searchitem():                       #FUNCTION TO SEARCH ITEM
        
        cursor = db.cursor()
        bname=title1.get()
        
        sql = "SELECT * FROM stocks where title='%s'" %(bname)
        cursor.execute(sql)
        results = cursor.fetchall()
        
        for c in results:
            bookid=c[0]
            aname=c[1]
            a1name=c[2]
            title=c[3]
            price=c[4]
            year=c[5]
            discription=c[6]
            
            numberC=c[7]
            
            global i
            i=''
            i=i+(" bookid='%s',\n aname='%s',\na1name='%s',\ntitle='%s',\nprice='%d',\nyear='%s',\ndiscription='%s',\n numberC='%d'   " % (bookid,aname,a1name,title,price,year,discription,numberC))
            
            messagebox.showinfo('book details'," bookid='%s',\n\n aname='%s',\n\na1name='%s',\n\ntitle='%s',\n\nprice='%d',\n\nyear='%s',\n\ndiscription='%s',\n\n numberC='%d'   " % (bookid,aname,a1name,title,price,year,discription,numberC))

    #====================================================================================================================================================================================================================================================        

    label3= Label(root,text="",bg="light blue",fg="light blue",font=("rockwell", 30))
    label3.grid(columnspan=6, padx=10, pady=5)
    label= Label(root,text="        ---- SEARCH BOOK FROM STORE ---- ",bg="light blue",fg="dark blue",font=("rockwell", 37))
    label.grid(columnspan=6, padx=10, pady=5)
    label5= Label(root,text="",bg="light blue",fg="light blue",font=("rockwell", 30))
    label5.grid(columnspan=6, padx=10, pady=5)
    label4=Label(root, text="enter book's title:",bd="2",relief="groove",bg="blue",fg="white", font=("rockwell", 18),width=38)
    sql = "select distinct title from stocks" 
    cursor.execute(sql)
    l1=[]
    l = cursor.fetchall()
    for j in l:
        for i in j:
            l1+=[i]
        
    global title1
    try:
        
        title1=ttk.Combobox(root,values=l1,width=30,font='bold')
        title1.current(0)                                           #COMBOBOX FOR TITLE'S
        title1.grid(row=5,column=1)
        
    except:
        
        messagebox.showinfo("-- incomplete --", "no books in the shelf..!!",icon="warning")


    
    #====================================================================================================================================================================================================================================================

    label4.grid(row=5,column=0, sticky=W, padx=10, pady=40)
    button4= Button(root, text="search book" , bg="blue", fg="white", width =15, font=("rockwell", 18), command=searchitem)
    button4.grid(row=7,column=1, padx=40, pady=10)
    
    def back():
        root.destroy()                          #FUNCTION TO GO BACK
        import admnchoice

    #====================================================================================================================================================================================================================================================
        
    button5= Button(root, text="back ", bg="blue", fg="white", width=10, font=("rockwell", 18),command=back)
    button5.grid(row=7,column=0, padx=40, pady=40)
    root.mainloop()

#====================================================================================================================================================================================================================================================
