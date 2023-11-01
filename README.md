#Supermarket Billing System
Supermarket Billing System is a simple application that allows users to manage the inventory and sales of a supermarket. It is written in Python using the Tkinter GUI toolkit. It has two modes: admin and cashier. The admin mode allows users to add, update, delete, and view products and categories in the database. The cashier mode allows users to scan products, generate bills, and print receipts. It has a simple and user-friendly interface that resembles a real supermarket billing system.

Installation
To run Supermarket Billing System, you need to have Python 3 installed on your system. You can download Python 3 from [here]. You also need to have Tkinter installed, which is usually included with Python 3. If not, you can install it using pip:

pip install tkinter

You also need to have SQLite installed, which is a lightweight database engine that stores data in a single file. You can download SQLite from [here].

To download Supermarket Billing System, you can either clone this repository using git:

git clone https://github.com/username/supermarket-billing-system.git

Or you can download the zip file from [here] and extract it to your preferred location.

Usage
To launch Supermarket Billing System, you can either double-click on the supermarket.py file or run it from the command line:

python supermarket.py

You will see a window like this:

![Supermarket Billing System screenshot]

You can choose either admin or cashier mode by clicking on the buttons. You will be asked to enter a password for each mode. The default passwords are:


Mode	Password
Admin	admin
Cashier	cashier
You can change the passwords later in the settings menu.

In the admin mode, you can use the menu bar to access various commands and options. You can also use keyboard shortcuts for some common actions. Here is a list of keyboard shortcuts:


Action	Shortcut
Add product	Ctrl+A
Update product	Ctrl+U
Delete product	Ctrl+D
View product	Ctrl+V
Add category	Ctrl+Shift+A
Update category	Ctrl+Shift+U
Delete category	Ctrl+Shift+D
View category	Ctrl+Shift+V
Exit	Alt+F4
In the cashier mode, you can use the buttons and entries to scan products, generate bills, and print receipts. You can also use keyboard shortcuts for some common actions. Here is a list of keyboard shortcuts:


Action	Shortcut
Scan product	Enter
Generate bill	F1
Print receipt	F2
Clear all	F3
Exit	Alt+F4
License
Supermarket Billing System is licensed under the MIT License. See [LICENSE] for more details.
