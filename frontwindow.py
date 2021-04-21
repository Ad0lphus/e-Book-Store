from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from createsqltable import *
          
#importing strftime function to retrieve system's Date & Time 
from time import strftime
def main():
    root=Tk()
    app=Window1(root)


class Window1:                  #MAIN WINDOW OF THE PROJECT
    
    def __init__(self,m):
        self.m=m
        self.m.title("--BOOK BUYING SYSTEM--")
        self.m.geometry('1200x700')
        self.m.configure(bg='sky blue')
        self.frame=Frame(self.m, bg='sky blue')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        self.lblTitle=Label(self.frame, text='---- ONLINE BOOK BUYING SYSTEM ----', font=('rockwell',30,),bg='sky blue',fg='dark blue')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)


        self.LoginFrame1=LabelFrame(self.frame, width=1350, height=600, font=('rockwell',20),relief='ridge', bg='sky blue',bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2=LabelFrame(self.frame, width=1000, height=600, font=('rockwell',20,),relief='ridge', bg='sky blue',bd=20)
        self.LoginFrame2.grid(row=2, column=0)


        self.lblUsername=Label(self.LoginFrame1, text= 'welcome to Ebook store', font=('rockwell',28), bd=22,bg='sky blue' , fg='dark blue')
        self.lblUsername.grid( row=0, column=0)
            

        self.lblPassword=Label(self.LoginFrame1, text= '“The Bookshop has a thousand books,\nAll colors, hues, and tinges,\nAnd every cover is a door \nThat turns on magic hinges.”', font=('rockwell',20,),bd=22,bg='sky blue' , fg='dark blue')
        self.lblPassword.grid( row=3, column=0)
            
                                         
        self.btnLogin=Button(self.LoginFrame2, text='ADMIN!',width=17,font=('rockwell',20),command=self.entry)
        self.btnLogin.grid(row=3,column=0,pady=20,padx=50)
        self.btncLogin1=Button(self.LoginFrame2, text='CUSTOMER!',width=17,font=('rockwell',20),command=self.entry1)
        self.btncLogin1.grid(row=3,column=1,pady=20,padx=50,sticky=E)

        #====================================================================================================================================================================================================================================================


        def time(): 
            string = strftime('%d/%m/%Y\t\t%H:%M:%S')                               
            
            self.lblTitle1.config(text = string)                                    #TIME AND DATE
            self.lblTitle1.after(1000, time)
                                                                                            
       
        self.lblTitle1 = Label(self.frame, font = ('calibri', 40, 'bold'), 
                    background = 'sky blue', 
                    foreground = 'dark blue')
        self.lblTitle1.grid(row=4,column=0,columnspan=2,pady=40)
        
        time() 
            

        self.btnExit=Button(self.LoginFrame2, text='EXIT!',width=17,font=('rockwell',20), command=self.iExit)
        self.btnExit.grid(row=3,column=2,pady=20,padx=50)

        #====================================================================================================================================================================================================================================================

    def entry(self):
        self.m.destroy()                                    #FUNCTION FOR ADMIN LOGIN             
        import login
        login.root1()
    #====================================================================================================================================================================================================================================================        

    def entry1(self):
        
        self.m.destroy()
                                                            #FUNCTION FOR CUSTOMER 
        import customer1
        
        customer1.cus1()

        import frontwindow
        frontwindow.main()
        
    #====================================================================================================================================================================================================================================================    

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("login Systems", "confirm if you want to exit")
        if self.iExit > 0:
            print("THANK YOU")
            self.m.destroy()                                #FUNCTION TO EXIT THE APPLICATION
        else:
            
            return   
           
#====================================================================================================================================================================================================================================================
        
if __name__=="__main__":
    main()
       

    

