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
    root.geometry("1100x550") 

    root.configure(width=1500,height=600,bg="light blue")
    var=-1
    i=''
    cursor=db.cursor()
    #====================================================================================================================================================================================================================================================
            
    def searchuser():                   #FUNCTION TO SEARCH USER

        
        db = mysql.connector.connect(user='root', password='', host='localhost',database='books')
        cursor = db.cursor()
        bname=name.get()
        
        sql = "SELECT * FROM users where uname='%s'" %(bname)
        cursor.execute(sql)
        results = cursor.fetchall()
        
        for c in results:
            uid=c[0]
            uname=c[1]
            age=c[3]
            contact=c[4]
            billingadd=c[5]
            
            
            global i
            i=''
            i=i+(" uid='%s',\n\n uname='%s',\n\nage='%d',\n\ncontact='%d',\n\nbillingadd='%s' " % (uid,uname,age,contact,billingadd))
            
            messagebox.showinfo('User details',i)
    #=====================================================================================================================================================

            
    def deleteuser():
        
        temp=name.get()
        
        
        try:
            sql = "delete from users where uname='%s'" % (temp)
            
            
            cursor.execute(sql)
            db.commit()
                  
            messagebox.showinfo("-- complete --", "succesfully deleted the user",icon="info")
            root.destroy()
            root1()
            
            
        except Exception as e:
            print (e)
            db.close()
    #=====================================================================================================================================================

    
    
    label3= Label(root,text="",bg="light blue",fg="light blue",font=("rockwell", 30))
    label3.grid(columnspan=6, padx=10, pady=10)
    label= Label(root,text="    ---- SEARCH USERS ----",bg="light blue",fg="dark blue",font=("rockwell", 36))
    label.grid(columnspan=6, padx=10, pady=20)
    label5= Label(root,text="",bg="light blue",fg="light blue",font=("rockwell", 30))
    label5.grid(columnspan=6, padx=10, pady=10)
    label4=Label(root, text="Enter username:",bd="2",relief="groove",bg="blue",fg="white", font=("rockwell", 18),width=30)

    #=====================================================================================================================================================


    sql = "select distinct uname from users" 
    cursor.execute(sql)
    l1=[]
    l = cursor.fetchall()
    for j in l:
        for i in j:
            l1+=[i]
        
    global title1
    try:
        
        
        name=ttk.Combobox(root,values=l1,width=30,font='bold')
        name.current(0)
        name.grid(row=4,column=1)
        
    except:
        
        messagebox.showinfo("-- incomplete --", "no users registered..!!",icon="warning")

    
    #=====================================================================================================================================================


    label4.grid(row=4,column=0, sticky=W, padx=10, pady=40)
    button4= Button(root, text="search user" , bg="blue", fg="white", width =18, font=("rockwell", 18), command=searchuser)
    button4.grid(row=6,column=0, padx=40, pady=40)
    button8= Button(root, text="delete user" , bg="blue", fg="white", width =18, font=("rockwell", 18), command=deleteuser)
    button8.grid(row=6,column=1, padx=40, pady=40)

    #=====================================================================================================================================================
    def back():
        root.destroy()
        import admnchoice
        
    #=====================================================================================================================================================    

    button5= Button(root, text="back", bg="blue", fg="white", width=13, font=("rockwell", 18),command=back)
    button5.grid(row=6,column=2, padx=40, pady=40)


    
    root.mainloop()
#==========================================================================================================================================================
    
