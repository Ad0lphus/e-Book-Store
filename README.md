# e-BOOK STORE


---

## SYNOPSIS 

The Book store is a simple e-commerce application where users can  select books, view the bookstore catalogue, and purchase books. 
Two roles are defined for the system: customer and administrator. A  customer would only be able to buy books or search for them. An  administrator can add books to the inventory, query all the orders  placed in the website and manage users. 
Books are organized into various categories. All these categories are  displayed in a user-friendly manner. 
A guest can query for any book. To buy a book, the user must be  logged-in. There is a ‘Buy book’ button under each book. This takes  the user to the ‘Buy book’ page. If the number of copies available for  the selected book is zero, appropriate message is displayed, otherwise,  the customer information would be auto-populated in the Buy-Book page. The user can select the number of copies required. The total  price is displayed to the user. By clicking on ‘Buy’, it displays  success message. 
A log of all the books sold including the details of the users who  bought them are maintained. The admin would be able to query all the  orders placed in the website. 
Python 3.7.4 has been used in the project. Tkinter module is used in  the project for creating GUI (Graphical User Interface), which makes  it easy to access and provides the click and view style. MySQL is  used as backend database.


---

### Book Store Home Page 
The website opens to home page where two major options are  displayed. Upon clicking on the options, the users are directed to  corresponding pages. The options available are as below  

1) Admin 
The admin user is authenticated with login ID and password.  Operations (displayed once the Admin user successfully logs-n)  which can be performed by Admin user are as below  
• Add book: Admin user can add a book to the online store. The  details entered in the webpage are updated in the MySQL  database in background 
• Delete book: Admin user can delete a book in the store with this  option. The corresponding details are updated in the MySQL  database in background 
• Search book: Admin user can search and view details of a book.  The query is generated based on the input entered in the  webpage and executed in the MySQL database. The result is  displayed on the webpage 
• User management: Admin user can add or delete users and  modify access for users for the Book Store. The changes made  are updated in the MySQL database, 
• Order management: Admin user can query and view all orders  placed in the Book Details of books sold, which users who  bought them would be visible to the Admin 
• Update book: The details of a book can be updated with this  option. Details of book such as number, description etc entered  are updated in the MySQL database 
• Sign out: Admin users can sign-out from the Book Store with  this option

2) Customer 
Customers visiting the Online Book Store can use this option. The  customer option redirects the user to a new page with following  options for log-in 
• Existing User: User must enter the login details (username,  password) which is verified from the MySQL database. After  successful login, customer can perform the following operations  
o Search and view details of a book: The details entered by  customer are converted to query using logic implemented  in python and executed in the MySQL database. The result  is displayed in the webpage 
o Purchase: purchase books: Customer can purchase desired  number of books from the online store. The number and  details of books are updated in database 
• New Customer: New customers can create user accounts with  this option. Name, age, contact number, shipping and billing  address will be collected from the user while registering. 
• Enter without logging: This option is for users to view and  search details of books. Through this option, the customer  would not be able to purchase books 
• Exit option: The user is directed back to Main menu

### SYSTEM DIAGRAM
![](https://i.imgur.com/uUGdg9N.png)

[Run frontwindow.py]
---

### OUTPUT:

#### database configuration 
![](https://i.imgur.com/Cw82IBd.png)

#### Home!
![](https://i.imgur.com/e85SVVg.png)

#### Admin Login
![](https://i.imgur.com/OzjyaXe.png)

#### Admin Control
![](https://i.imgur.com/3cPLRxF.png)

#### Costomer Page
![](https://i.imgur.com/sqbMUUC.png)

#### New User Registration
![](https://i.imgur.com/1IXIfZx.png)

#### User Login
![](https://i.imgur.com/wi2LVFY.png)

#### Buying Page
![](https://i.imgur.com/TT7r43o.png)

#### MySQL Database Tables
![](https://i.imgur.com/Dixr6e3.png)

#### Auto-Bill Generation
![](https://i.imgur.com/ofJgQyL.png)
