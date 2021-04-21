from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as con
from createsqltable import passwrd
import random



def ret():
    global paid
    
    if var1.get()==1 and len(combo.get())!=0:
        address=combo.get()                                                                                             
        sql="insert into orders values("+str(orderid)+","+str(uid)+","+str(bookid)+",'"+address+"',"+str(numberC)+",'COD');"              #saving orders to books database
        cur.execute(sql)
        mycon.commit()
        sql="update stocks set numberC=numberC-"+str(numberC)+" where bookid="+str(bookid)+";"
        cur.execute(sql)
        mycon.commit()
        print("Stock of item decreased..")
        mycon.close()
        bill()
        print("Order placed")
        messagebox.showinfo("message","Your order has been placed")
        master.destroy()
        paid=True

    
    elif len(combo.get())==0:
         messagebox.showinfo("Alert..","please enter an address")
        

    
   

    elif var1.get()==0:
        messagebox.showinfo("Alert:","please select the payment option")
    
        



#====================================================================================================================================================================================================================================================
    
        
    

def bill():
    f=open("bill.txt","w")                                                                                              #creating a text file as invoice of the purchase

                                                                                                                        #writing into the file the details regarding the purchase
    f.write('Order id:'+str(orderid)+'\n')
    f.write('customer id:'+str(uid)+'\n')
    f.write('Customer name:'+uname+'\n')
    f.write('Product name:'+data1[1]+'\n')
    f.write('Payment method:COD'+'\n')
    f.write('Price:'+str(int(data1[0])*numberC)+'\n')
    f.write('address:'+l[0]+'\n')
    f.write('\n\n')
    f.write('Thankyou for shopping with us...\nSee you again soon')
    f.close()
    print('bill printed and saved')

#====================================================================================================================================================================================================================================================    

def abort():
    master.destroy()
    print("transaction aborted")
    
    
    
#====================================================================================================================================================================================================================================================        
        

def pay():                                                                                                 #cid is the customer id, and productid is the id of the item bought
    global var1,master,combo,uname,l,data1
    
    sql="select billingadd,uname from users where uid="+str(uid)+";"
    cur.execute(sql)
    data=cur.fetchone()
    
    
    uname=data[1]
    l=[data[0]]

    sql1="select price,title from stocks where bookid="+str(bookid)+";"
    cur.execute(sql1)
    data1=cur.fetchone()
    

    print("payment process started...")
    master=Toplevel()                                                                                                         #creating master window
    master.title("Payment")
    
    master.configure(width=3500,height=2600,bg='light blue')
    Label(master,text="WELCOME TO THE PAYMENT PAGE"+"\n"*1,font="rockwell,10",fg="Blue",bg='light blue').grid(row=0,column=0,columnspan=2)
    Label(master,text="Item selected:",bg='light blue').grid(row=2,column=0)
    Label(master,text=data1[1],bg='light blue').grid(row=2,column=1)
    Label(master,text="Order Id:",bg='light blue').grid(row=3,column=0)
    Label(master,text=str(orderid),bg='light blue').grid(row=3,column=1)
    Label(master,text="Price:",bg='light blue').grid(row=4,column=0)
    Label(master,text=str(int(data1[0])*numberC),bg='light blue').grid(row=4,column=1)
    Label(master,text="Name:",bg='light blue').grid(row=5,column=0)
    Label(master,text=uname,bg='light blue').grid(row=5,column=1)
    Label(master,text="Enter address",bg='light blue').grid(row=6,column=0)
    combo=ttk.Combobox(master,values=l)
    combo.current(0)
    combo.grid(row=6,column=1,pady=2)


    Label(master,text="Payment method",bg='light blue').grid(row=8,column=0)

    var1=IntVar()
    Checkbutton(master,text="cash on delivery",variable=var1,bg='light blue').grid(row=8,column=1)
    Button(master,text="submit",command=ret,bg="blue",width=5).grid(row=10,column=1,sticky=E)
    Button(master,text="cancel",command=abort,bg="blue",width=5).grid(row=10,column=0,sticky=W)
    master.mainloop()

#====================================================================================================================================================================================================================================================    
    
def payment(uuid,ookid,o):
    global uid,bookid,numberC,orderid,cur,paid,mycon

    mycon=con.connect(host="localhost",user="root",password=passwrd,database="books")                                       #establishing connection with books database
    cur=mycon.cursor()    
                                                                                   
    paid=False                                                                                                              #creating a flag to check if the payment is successful

    orderid=random.randrange(10000,99999)                                                               #creating a random order id for the purchase
    uid=uuid
    bookid=ookid
    numberC=o
    pay()                                                                                                      #creating a flag to check if the payment is successful

#====================================================================================================================================================================================================================================================    
    













