#shopping page

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as con
from functools import partial
import payment
from createsqltable import passwrd

def shop():
    global master
    
                                                                                                        #main page    
    master=Tk()
    master.title("Home")
    master.configure(width=3500,height=2600,bg='light blue')
    Label(master,text="Hello "+uname+",\nWishing you a happy shopping",bg='light blue',font=("Helvetica",15)).grid(row=1,column=0,columnspan=2,pady=20)
    Button(master,text="Log out",bg="red",command=logout).grid(row=2,column=2,columnspan=1,rowspan=2,pady=20,sticky=NE)
    Button(master,text="View my cart",bg="blue",fg='white',command=viewcartitems).grid(row=2,column=0,columnspan=1,rowspan=2,pady=20,sticky=W)
    Button(master,text="My orders",bg="grey",fg='white',command=myorders).grid(row=2,column=1,columnspan=1,rowspan=2,pady=20,sticky=W)
    Button(master,text="Browse by author",command=bba,bg="light green").grid(row=4,column=1,pady=30,sticky=W)
    
    Button(master,text="Browse by category",command=bbc,bg="grey",fg='white').grid(row=5,column=1,pady=30,sticky=W)
    Button(master,text="Search a book",command=search).grid(row=6,column=1,pady=30,sticky=W)
    Button(master,text="Browse all books",command=all,bg="yellow").grid(row=7,column=1,pady=10,sticky=W)
    master.mainloop()
#====================================================================================================================================================================================================================================================
def bba():                                                          #browse by author
    global l,a,master1,author
    sql="select distinct aname from stocks;"
    cur.execute(sql)
    data=cur.fetchall()
    l=[]
    for i in data:
        l+=i
    master1=Tk()
    master1.title("Search by author")
    master1.configure(width=3500,height=2600,bg='light blue')
    author=ttk.Combobox(master1,values=l)
    author.current(0)
    author.grid(row=1,column=1)
    
        
    Button(master1,text="search",command=bba1,bg="blue").grid(row=2,column=1)
    
#====================================================================================================================================================================================================================================================        
def bba1():
    author1=author.get()
    sql="select bookid,title,aname,price,cat,discription from stocks where aname='"+author1+"';"                       
    cur.execute(sql)
    dataan=cur.fetchall()
    master1.destroy()
    find(dataan)
    
#====================================================================================================================================================================================================================================================        
def all():
    sql="select bookid,title,aname,price,cat,discription from stocks"                                   #browse all books
    cur.execute(sql)
    dataall=cur.fetchall()
    find(dataall)

#====================================================================================================================================================================================================================================================
def bbc():
    global l,a,master1,cat
    sql="select distinct cat from stocks;"
    cur.execute(sql)
    data=cur.fetchall()
    l=[]
    for i in data:
        l+=i
    master1=Tk()
    master1.title("Category search")
    master1.configure(width=3500,height=2600,bg='light blue')
    cat=ttk.Combobox(master1,values=l)
    cat.current(0)
    cat.grid(row=1,column=1)
    
    
    Button(master1,text="search",command=bbc1,bg="blue").grid(row=2,column=2)
#====================================================================================================================================================================================================================================================
def bbc1():
    cat1=cat.get()
    
    sql="select bookid,title,aname,price,cat,discription from stocks where cat='"+cat1+"';"
    cur.execute(sql)
    datacat=cur.fetchall()
    master1.destroy()
    find(datacat)

#====================================================================================================================================================================================================================================================
def search():
    global entry1,master1,bname
    sql="select distinct title from stocks"
    cur.execute(sql)
    data=cur.fetchall()
    l=[]
    for i in data:
        l+=i
    master1=Tk()
    master1.title("Search books")
    master1.configure(width=3500,height=2600,bg='light blue')
    Label(master1,text="enter the book you want to search",bg='light blue').grid(row=1,column=0,pady=20)
    bname=ttk.Combobox(master1,values=l)
    bname.grid(row=1,column=1,pady=20)
    bname.current(0)

    
    Button(master1,text="search",command=search1,bg="blue").grid(row=2,column=1)
    
#====================================================================================================================================================================================================================================================
def search1():
    name=bname.get()
    sql="select bookid,title,aname,price,cat,discription from stocks where title='"+name+"';"
    cur.execute(sql)
    datan=cur.fetchall()
    master1.destroy()
    find(datan)


#====================================================================================================================================================================================================================================================
def find(data):                                     #buying page
    global master2

    
    
    master2=Tk()
    master2.title("Catalogue")
    master2.configure(width=3500,height=2600,bg='light blue')
    Label(master2,text="bookid",bg='light blue').grid(row=0,column=0,pady=10,padx=10)
    Label(master2,text="title",bg='light blue').grid(row=0,column=1,pady=10,padx=10)
    Label(master2,text="author's name",bg='light blue').grid(row=0,column=2,pady=10,padx=10)
    
    Label(master2,text="price",bg='light blue').grid(row=0,column=3,pady=10,padx=10)
    
    Label(master2,text="catagory",bg='light blue').grid(row=0,column=4,pady=10,padx=10)
    Label(master2,text="description",bg='light blue').grid(row=0,column=5,pady=10,padx=10)

    for i in range(len(data)):
        for j in range(len(data[i])-1):
        
            Label(master2,text=data[i][j],bg='light blue').grid(row=i+1,column=j,pady=10,padx=10)
        T=Text(master2,height=10,width=30)
        T.insert(END,data[i][j+1])
        T.grid(row=i+1,column=j+1,pady=10,padx=10)
        Button(master2,text="buy",command=partial(buy,data[i][0]),fg="white",bg="blue").grid(row=i+1,column=j+2,pady=10,padx=10)
        Button(master2,text="add to cart",command=partial(cart,data[i][0]),fg="white",bg="blue").grid(row=i+1,column=j+3,pady=10,padx=10)
    
        
#====================================================================================================================================================================================================================================================            
def viewcartitems():                                    #viewing the items in the cart
    
    global master2
    
    
    
    master2=Tk()
    master2.title("My Cart")
    master2.configure(width=3500,height=2600,bg='light blue')

    if cartitems==[]:
        Label(master2,text="Your cart is empty",bg='light blue').grid(column=0,row=0)
    else:
        Label(master2,text="bookid",bg='light blue').grid(row=0,column=0,pady=10,padx=10)
        Label(master2,text="title",bg='light blue').grid(row=0,column=1,pady=10,padx=10)
        Label(master2,text="author's name",bg='light blue').grid(row=0,column=2,pady=10,padx=10)
        
        Label(master2,text="price",bg='light blue').grid(row=0,column=3,pady=10,padx=10)
        
        Label(master2,text="catagory",bg='light blue').grid(row=0,column=4,pady=10,padx=10)
        Label(master2,text="Description",bg='light blue').grid(row=0,column=5,pady=10,padx=10)

        for i in range(len(cartitems)):
            for j in range(len(cartitems[i])-1):
            
                Label(master2,text=cartitems[i][j],bg='light blue').grid(row=i+1,column=j,pady=10,padx=10)
            T=Text(master2,height=10,width=30)
            T.insert(END,cartitems[i][j+1])
            T.grid(row=i+1,column=j+1,pady=10,padx=10)
            Button(master2,text="buy",command=partial(buy,cartitems[i][0]),fg="white",bg="blue").grid(row=i+1,column=j+2,pady=10,padx=10)
            Button(master2,text="delete",command=partial(remove,cartitems[i][0]),fg="white",bg="blue").grid(row=i+1,column=j+3,pady=10,padx=10)

#====================================================================================================================================================================================================================================================
def getno(bookid):
    noo=int(no.get())
    bookno.destroy()
    cont(noo,bookid)

#====================================================================================================================================================================================================================================================
def buy(bookid):
    global bookno,no
    if uid!=0:                                      #if user is signed in
        
        sql="select numberC from stocks where bookid="+str(bookid)+";"
        cur.execute(sql)
        ava=cur.fetchone()
        
        if int(ava[0])>0:                   #if book is available
            
            bookno=Toplevel()
            bookno.title("Quantity")
            bookno.configure(width=3500,height=2600,bg='light blue')
            Label(bookno,text="No of books available:"+str(ava[0]),bg='light blue').grid(pady=5)
            Label(bookno,text="Select no of books you want:",bg='light blue').grid(row=1,column=0)
            no=Spinbox(bookno,from_ =1 ,to=int(ava[0]))
            no.grid(row=1,column=1)
            Button(bookno,text="submit",command=partial(getno,bookid=bookid),bg="blue",fg="white").grid(row=2,column=1,sticky=E)
            
        else:
            messagebox.showinfo("message","this book is currently unavailable.. sorry for the inconvenience")
        
            
        
    else:
        messagebox.showinfo("message","you have to be logged in before buying.\nplease click logout or close the window and then sign in..")
        
#====================================================================================================================================================================================================================================================        
def cont(no,bookid):            #no-no of books selected,bookid-id of book selected
    
    master2.destroy()
    remove1(bookid)
    payment.payment(uid,bookid,no)

#====================================================================================================================================================================================================================================================
def logout():


    user=None                       #deleting the current user data
    master.destroy()
    
    
#====================================================================================================================================================================================================================================================
def remove(i):                                      #removing items from cart
    master2.destroy()
    sql="delete from cart where bookid="+str(i)+" and uid="+str(uid)+";"
    cur.execute(sql)
    mycon.commit()
    cartitem()
    viewcartitems()
#====================================================================================================================================================================================================================================================
def remove1(i):
    
    sql="delete from cart where bookid="+str(i)+" and uid="+str(uid)+";"
    cur.execute(sql)
    mycon.commit()
    cartitem()
    
#====================================================================================================================================================================================================================================================    
    
def cart(bookid):                                   #inserting book with id=bookid into the cart 
    sql="insert into cart values("+str(uid)+","+str(bookid)+");"
    cur.execute(sql)
    mycon.commit()
    cartitem()
    messagebox.showinfo("message","item added to cart")
    
#====================================================================================================================================================================================================================================================    
def myorders():                                                                     #show orders
    master1=Tk()
    master1.configure(width=3500,height=2600,bg='light blue')
    mycon.commit()
    sql="select bookid,title,quantity from orders,stocks where productid=bookid and uid="+str(uid)+";"
    cur.execute(sql)
    myord=cur.fetchall()
    if myord==[]:
        Label(master1,text="No orders yet..",bg='light blue').grid()
    else:
        Label(master1,text="book id",bg='light blue').grid(row=0,column=0,padx=5,pady=5)
        Label(master1,text="title",bg='light blue').grid(row=0,column=1,padx=5,pady=5)
        Label(master1,text="quantity",bg='light blue').grid(row=0,column=2,padx=5,pady=5)
        Label(master1,text="mode of payment",bg='light blue').grid(row=0,column=3,padx=5,pady=5)
        
        for i in range(len(myord)):
            for j in range(len(myord[i])):
                Label(master1,text=myord[i][j],bg="light blue").grid(row=i+1,column=j)
            Label(master1,text="COD",bg='light blue').grid(row=i+1,column=j+1)


mycon=con.connect(host="localhost",user="root",password=passwrd,database="books")
cur=mycon.cursor()

#====================================================================================================================================================================================================================================================

def cartitem():                                         #retrieving the cart items of the current user
    global cartitems
    mycon.commit()
    cur.execute("select b.bookid,title,aname,price,cat,discription from stocks as b,cart as c where c.bookid=b.bookid and uid="+str(uid)+";")
    cartitems=cur.fetchall()
#====================================================================================================================================================================================================================================================
def initialize(user):
    
    global uid
    global uname
    
   
    uid=user[0]
    uname=user[1]
    cartitem()
    shop()

#====================================================================================================================================================================================================================================================


