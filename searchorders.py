from tkinter import *
from tkinter import messagebox
import mysql.connector
from createsqltable import passwrd
from tkinter import ttk
import mysql.connector as con
db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to establish connection between python and books
def root1():
    global root
    root = Tk()
    root.title("Ebook store ")
    root.geometry("1150x600") 

    root.configure(width=1500,height=600,bg="light blue")
    var=-1
    i=''
    cursor=db.cursor()

    #=====================================================================================================================================================
    
    label3= Label(root,text="",bg="light blue",fg="light blue",font=("rockwell", 30))
    label3.grid(columnspan=6, padx=10, pady=5)
    label= Label(root,text="        ---- SEARCH ORDERS ----",bg="light blue",fg="dark blue",font=("rockwell", 38))
    label.grid(columnspan=6, padx=10, pady=40)
    label5= Label(root,text="",bg="light blue",fg="light blue",font=("rockwell", 30))
    label5.grid(columnspan=6, padx=10, pady=10)
    label4=Label(root, text="Enter order id : ",bd="3",relief="groove",bg="blue",fg="white", font=("rockwell", 18),width=26)
    sql = "select distinct orderid from orders" 
    cursor.execute(sql)
    l1=[]
    l = cursor.fetchall()
    for j in l:
        for i in j:
            l1+=[i]
        
    global orderid
    try:
        
        
        orderid1=ttk.Combobox(root,values=l1,width=30,font='bold')
        orderid1.current(0)
        orderid1.grid(row=3,column=1)
    except:
        messagebox.showinfo("-- incomplete --", "no orders yet..!!",icon="warning")

    #=====================================================================================================================================================        
    def searchuser():
        
        global oid
        oid=orderid1.get()
        
        sql = "SELECT * FROM orders where orderid='%s'" %(oid)
        cursor.execute(sql)
        results = cursor.fetchall()
        
        for c in results:
            orderid=c[0]
            uid=c[1]
            productid=c[2]
            address=c[3]
            Quantity=c[4]
            payment=c[5]
            
            
            global i
            i=''
            i=i+(" orderid='%d',\n\n uid='%d',\n\nproductid='%d',\n\naddress='%s',\n\nQuantity='%d',\n\npayment='%s' " % (orderid,uid,productid,address,Quantity,payment))
            
            messagebox.showinfo('User details',i)
    #=====================================================================================================================================================
            
    def deleteuser():
                                            #function to delete book
        temp=orderid1.get()
        
        
        try:
            sql = "delete from orders where orderid='%s'" % (temp)
            
            
            cursor.execute(sql)
            db.commit()
            messagebox.showinfo("-- complete --", "succesfully deleted the order",icon="info")
            print("Deleted the order")
            root.destroy()
            root1()
        except Exception as e:
            print (e)
            db.close()
    
    label4.grid(row=3,column=0, sticky=W, padx=10, pady=60)
    button4= Button(root, text="search orders" , bg="blue", fg="white", width =20, font=("rockwell", 18), command=searchuser)
    button4.grid(row=9,column=0, padx=40, pady=30)
    button8= Button(root, text="delete orders" , bg="blue", fg="white", width =20, font=("rockwell", 18), command=deleteuser)
    button8.grid(row=9,column=1, padx=40, pady=30)
    
    #=====================================================================================================================================================
    
    def back():
        root.destroy()
        import admnchoice
       
    button5= Button(root, text="back ", bg="blue", fg="white", width=20, font=("rockwell", 18),command=back)
    button5.grid(row=9,column=2, padx=40, pady=30)
    
    #=====================================================================================================================================================
    
    root.mainloop()


#=========================================================================================================================================================
    
