import mysql.connector
passwrd=''

def create():
    f=open("sqlpassword.txt","w")
    f.close()


try:
    f=open("sqlpassword.txt","r+")
    f.close()
except:
    create()
try:
    db=mysql.connector.connect(host='localhost',user='root', password=passwrd) #to get the password
    cur=db.cursor()

except:
    
    f=open("sqlpassword.txt","r+")
    data=f.read()
    
    if data=='':
        passwrdnew=input("Enter the password of your mysql database:")
        f.write(passwrdnew)
        passwrd=passwrdnew
        f.close()
    else:
        
        passwrd=data
        
        

try:
    db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database="books")

except:
    db=mysql.connector.connect(host='localhost',user='root', password=passwrd) #to create database
    cur=db.cursor()
    sql="create database books"
    cur.execute(sql)
    
try:
    db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to create table stocks
    cur=db.cursor()
    sql="select * from stocks"
    cur.execute(sql)
except:
    db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') 
    cur=db.cursor()
    sql="create table stocks(bookid varchar(55),aname varchar(55),a1name varchar(55),title varchar(55),price integer,year date,discription varchar(10000),numberC integer,cat varchar(55));"   
    cur.execute(sql)
    a=input("Do you want to insert sample books..(y/n)")
    if a in "yY":
        sql="insert into stocks values(100,'Jeffrey Archer',Null,'False Impression',1000,'2002-09-18','When an aristocratic old lady is brutally murdered in her country home the night before 9/11, it takes all the resources of the FBI and Interpol to work out the connection between her and the possible motive for her death – a priceless Van Gogh painting. Anna Petrescu is missing, presumed dead, after 9/11 and she uses her new status to escape from America, only to be pursued across the world...',30,'Novel thriller');"
        cur.execute(sql)
        sql="insert into stocks values(101,'Mahatma Gandhi',null,'The Story of My Experiments with Truth',2000,'2002-05-15','This autobiography The Story of My Experiments with Truth, is an aperture to the workings of Mahatma Gandhis mind – an aperture to the emotions of his heart – an aperture to understanding what drove this seemingly ordinary man to the heights of being the father of a nation – India....',30,'Autobiography');"
        cur.execute(sql)
        sql="insert into stocks values(102,'William Shakespeare',null,'Macbeth',3000,'1623-05-15','When three witches make a prophecy that Macbeth will be crowned King of Scotland, he is sceptical. He quickly begins to rise up the ranks however, and starts to wonder if there is any truth in the prediction. His wife is convinced that he should be in power, and persuades him to kill the current king.... ',50,'Drama');"
        cur.execute(sql)
        sql="insert into stocks values(103,'Ashwin Sanghi',null,'The Krishna Key',4000,'2012-07-11','Five thousand years ago, there came to earth a magical being called Krishna, who brought about innumerable miracles for the good of mankind. In modern times, a poor little rich boy grows up believing that he is that final avatar.Only, he is a serial killer. .',80,'‎Novel‎ Thriller');"
        cur.execute(sql)
        sql="insert into stocks values(104,'J.K Rowling',null,'The Complete Harry Potter Series (7 books)',200,'2016-07-30','J. K. Rowling presents the story of a young boy wizard who must face one day face his greatest adversary, a Dark Lord who lost his power in an attempt to kill the boy when he was merely a year old. The Complete Collection presents all seven volumes of the Harry Potter series that took the literary world by storm....',30,'Juvenile Fiction');"
        cur.execute(sql)
        
        db.commit()


try:
    db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to create table pass
    cur=db.cursor()
    sql="select * from pass"
    cur.execute(sql)
except:
    db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') 
    cur=db.cursor()
    sql="create table pass(ussername varchar(55),password varchar(55));"   
    cur.execute(sql)
    print("Admin registration")
    print("*********************")
    uname=input("Enter uname:")
    password=input("Enter password:")
    sql="insert into pass values('"+uname+"','"+password+"');"
    cur.execute(sql)
    print("Administrator successfully registered")
    db.commit()






try:
    db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to create table cart
    cur=db.cursor()
    sql="select * from cart"
    cur.execute(sql)
except:
    sql="create table cart(uid integer,bookid integer);"   
    cur.execute(sql)


try:
    db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to create table orders
    cur=db.cursor()
    sql="select * from orders"
    cur.execute(sql)
except:
    sql="create table orders(orderid integer,uid integer,productid integer,address varchar(100),Quantity integer, payment varchar (55));"   
    cur.execute(sql)




try:
    db=mysql.connector.connect(host='localhost',user='root', password=passwrd,database='books') #to create table users
    cur=db.cursor()
    sql="select * from users"
    cur.execute(sql)
except:
    sql="create table users(uid integer,uname varchar(55),password varchar(55),age integer,contact integer,billingadd varchar(100));"   
    cur.execute(sql)





db.close()

