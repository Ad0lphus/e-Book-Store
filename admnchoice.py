from tkinter import *
from tkinter import messagebox
from createsqltable import passwrd
import mysql.connector
import mysql.connector as cur
db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to establish connection between python and books
def root1():
    global root
    root = Tk()
    root.title("Ebook store ")
    root.configure(width=3500,height=2600,bg='light blue')
    root.geometry("1270x750") 
    var=-1

    def additem():
        root.destroy()
        import proj1
        proj1.root1()
        
        root1()
        
    #====================================================================================================================================================================================================================================================    
        
       
    def deleteitem():
        sql = "select distinct bookid from stocks" 
        cursor.execute(sql)
        l1=[]
        l = cursor.fetchall()
        for j in l:
            for i in j:
                l1+=[i]
        if l1==[]:
            
            messagebox.showinfo("-- incomplete --", "no books in the shelf..!!",icon="warning")
            
        else:
            root.destroy()
            import deleteitem
            deleteitem.root1()
            
            root1()

    #====================================================================================================================================================================================================================================================
    def updateitem():
        sql = "select distinct bookid from stocks" 
        cursor.execute(sql)
        l1=[]
        l = cursor.fetchall()
        for j in l:
            for i in j:
                l1+=[i]
        if l1==[]:
           
            messagebox.showinfo("-- incomplete --", "no book in the shelf to get updated..!!",icon="warning")
            
        else:
            root.destroy()
            
            import updateitem
            updateitem.root1()
        
        root1()

    #====================================================================================================================================================================================================================================================
    def searchitem():
        sql = "select distinct title from stocks" 
        cursor.execute(sql)
        l1=[]
        l = cursor.fetchall()
        for j in l:
            for i in j:
                l1+=[i]
        if l1==[]:
           
            messagebox.showinfo("-- incomplete --", "no books in the shelf..!!",icon="warning")
            
        else:
            root.destroy()
            import searchitem
            searchitem.root1()
        
            root1()

    #====================================================================================================================================================================================================================================================
    def searchuser():
        sql = "select distinct uname from users" 
        cursor.execute(sql)
        l1=[]
        l = cursor.fetchall()
        for j in l:
            for i in j:
                l1+=[i]
        if l1==[]:
            
            messagebox.showinfo("-- incomplete --", "no users registered..!!",icon="warning")
            
        else:
            root.destroy()
            import usersearch
            usersearch.root1()
            root1()

    #====================================================================================================================================================================================================================================================
        
    def back():
        root.destroy()
        import frontwindow
        frontwindow.main()
        
    #====================================================================================================================================================================================================================================================   
    def deleteuser1():
        
        temp=entry1.get()
        
        
        try:
            sql = "delete from users where uname='%s'" % (temp)
            
            
            cursor.execute(sql)
            db.commit()
            messagebox.showinfo("-- complete --", "succesfully deleted the book",icon="info")
        except Exception as e:
            print (e)
            db.close()

    #====================================================================================================================================================================================================================================================
    def find(data):                                     #buying page
        global master2

        
        
        master2=Tk()
        Label(master2,text="uid",bd=15).grid(row=0,column=0,pady=10,padx=10)
        Label(master2,text="uname",bd=15).grid(row=0,column=1,pady=10,padx=10)
        Label(master2,text="age",bd=15).grid(row=0,column=2,pady=10,padx=10)
        
        Label(master2,text="contact number",bd=15).grid(row=0,column=3,pady=10,padx=10)
        
        Label(master2,text="billing address",bd=15).grid(row=0,column=4,pady=10,padx=10)
        

        for i in range(len(data)):
            for j in range(len(data[i])-1):
            
                Label(master2,text=data[i][j]).grid(row=i+1,column=j,pady=10,padx=10)
            T=Text(master2,height=5,width=20)
            T.insert(END,data[i][j+1])
            T.grid(row=i+1,column=j+1,pady=10,padx=10)
            Button(master2,text="delete",command=deleteuser1,fg="white",bg="blue").grid(row=i+1,column=j+2,pady=10,padx=10)
            

    #====================================================================================================================================================================================================================================================
    def search():
        global entry1,master1
        master1=Tk()
        Label(master1,text="enter the name of the user : ",bd=15).grid(row=1,column=0,pady=20)
        entry1=Entry(master1,bd=15)
        entry1.grid(row=1,column=1,pady=20)
        
        name=entry1.get()
        sql="select uid,uname,age,contactno,billingadd from users where uname='"+name+"';"
        cursor.execute(sql)
        datan=cur.fetchall()
        
        Button(master1,text="search",bd=15,command=search1,bg="blue").grid(row=2,column=1)


    #====================================================================================================================================================================================================================================================
    def searchorders():
        sql = "select distinct orderid from orders" 
        cursor.execute(sql)
        l1=[]
        l = cursor.fetchall()
        for j in l:
            for i in j:
                l1+=[i]
        if l1==[]:
            #root.exit()
            messagebox.showinfo("-- incomplete --", "no orders registered..!!",icon="warning")
            
        else:
            root.destroy()
            import searchorders
            searchorders.root1()
            
            root1()
        
    #====================================================================================================================================================================================================================================================
    def search1():
        name=entry1.get()
        sql="select uid,uname,age,contactno,billingadd from users where uname='"+name+"';"
        cursor.execute(sql)
        datan=cur.fetchall()
        master1.destroy()
        find(datan)
    
    #====================================================================================================================================================================================================================================================
    cursor=db.cursor()
    label= Label(root,text="\t\t---- BOOK STORE ----\t\t",bd=3,bg="light blue",fg="dark blue",font=("rockwell",38))
    label.grid(columnspan=6, padx=10, pady=60)
    
    label2= Label(root,text="\t\tAdmin select the choice:\t\t\t",bd=3,bg="light blue",fg="dark blue",font=("rockwell",26))
    label2.grid(columnspan=6, padx=10, pady=60)
    
    button1= Button(root, text="add book ",bd=3, bg="blue", fg="white", width=20, font=("rockwell", 18),command=additem)
    button2= Button(root, text="delete book ",bd=3, bg="blue", fg="white", width =20, font=("rockwell", 18),command=deleteitem)
    button3= Button(root, text="update status ",bd=3 , bg="blue", fg="white", width =20, font=("rockwell", 18),command=updateitem)
    button4= Button(root, text="search book " ,bd=3, bg="blue", fg="white", width =20, font=("rockwell", 18), command=searchitem)
    button1.grid(row=8,column=2, padx=50, pady=40)
    button2.grid(row=9,column=1, padx=50, pady=40)
    button3.grid(row=8,column=3, padx=50, pady=40)
    button4.grid(row=8,column=1, padx=50, pady=40)
    button6= Button(root, text="user management " ,bd=3, bg="blue", fg="white", width =20, font=("rockwell", 18), command=searchuser)
    button6.grid(row=9,column=2, padx=40, pady=40)
    button7= Button(root, text="order management " ,bd=3, bg="blue", fg="white", width =20, font=("rockwell", 18), command=searchorders)
    button7.grid(row=9,column=3, padx=40, pady=40)
    button5= Button(root, text="signout",bd=3, bg="blue", fg="white", width=15, font=("rockwell", 18),command=back)
    button5.grid(row=0,column=3, padx=80, pady=40)



    root.mainloop()

#====================================================================================================================================================================================================================================================
