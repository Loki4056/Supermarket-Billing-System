import tkinter as tk
import sqlite3
import win32api
import win32print
import random
import time
import subprocess

columns = ('Item_No', 'Item_Name', 'Item_Type', 'Quantity_Remain', 'Item_Cost', 'Expiry_Date', 'Manufactured_By')

c = sqlite3.connect("grocery.sqlite")
cur = c.cursor()

sto = None  # Define sto as a global variable

def billingitems():
    ''' Billing GUI '''
    global c, cur, flag, t, name, name1, add, billingsto, names, qty, sl, qtys, n, namee, lb1
    t = 0
    
    names = []
    qty = []
    sl = []
    n = []
    qtys = [''] * 10
    cur.execute("CREATE TABLE IF NOT EXISTS grocerylist (Item_No INTEGER PRIMARY KEY, Item_Name TEXT, Item_Type TEXT, Quantity_Remain INTEGER, Item_Cost REAL, Expiry_Date TEXT, Manufactured_By TEXT)")
    cur.execute("SELECT * FROM grocerylist")
    for i in cur:
        n.append(i[1])
    c.commit()

    flag = 'billingsto'
    billingsto = tk.Tk()
    billingsto.title('BILLING')
    tk.Label(billingsto, text='-' * 48 + 'Billing' + '-' * 49).grid(row=0, column=0, columnspan=7, sticky='W')
    tk.Label(billingsto, text='Enter Name: ').grid(row=1, column=0)
    name1 = tk.Entry(billingsto)
    name1.grid(row=1, column=1)
    tk.Label(billingsto, text='Enter Address: ').grid(row=2, column=0)
    add = tk.Entry(billingsto)
    add.grid(row=2, column=1)

    tk.Label(billingsto, text='-' * 115).grid(row=6, column=0, columnspan=7, sticky='W')
    tk.Label(billingsto, text='Select Item', relief='ridge', width=15).grid(row=7, column=0)
    tk.Label(billingsto, text='Qty_Remain', relief='ridge', width=10).grid(row=7, column=1)
    tk.Label(billingsto, text='Cost', relief='ridge', width=4).grid(row=7, column=2)
    tk.Label(billingsto, text='Expiry Date', width=10, relief='ridge').grid(row=7, column=3)

    tk.Button(billingsto, text='Add to bill', width=15, command=addtothebill).grid(row=8, column=6)
    tk.Label(billingsto, text='QUANTITY', width=20, relief='ridge').grid(row=7, column=5)
    qtys = tk.Entry(billingsto)
    qtys.grid(row=8, column=5)
    refresh()
    tk.Button(billingsto, width=15, text='Main Menu', command=mainmenu).grid(row=1, column=6)
    tk.Button(billingsto, width=15, text='Refresh Stock', command=refresh).grid(row=3, column=6)
    tk.Button(billingsto, width=15, text='Reset Bill', command=resetbill).grid(row=4, column=6)
    tk.Button(billingsto, width=15, text='Print Bill', command=printbill).grid(row=5, column=6)
    tk.Button(billingsto, width=15, text='Save Bill', command=savebill).grid(row=7, column=6)

    billingsto.mainloop()


def refresh():
    ''' Displays all the data from the database '''
    global cur, c, billingsto, lb1, lb2, vsb

    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)
        lb3.yview(*args)
        lb4.yview(*args)

    def onmousewheel(event):
        lb1.yview('scroll', event.delta, 'units')
        lb2.yview('scroll', event.delta, 'units')
        lb3.yview('scroll', event.delta, 'units')
        lb4.yview('scroll', event.delta, 'units')
        return 'break'

    index = 0
    vsb = tk.Scrollbar(orient='vertical', command=onvsb)
    lb1 = tk.Listbox(billingsto, width=25, yscrollcommand=vsb.set)
    lb2 = tk.Listbox(billingsto, width=7, yscrollcommand=vsb.set)
    lb3 = tk.Listbox(billingsto, yscrollcommand=vsb.set, width=7)
    lb4 = tk.Listbox(billingsto, yscrollcommand=vsb.set, width=20)

    vsb.grid(row=8, column=2, sticky='N' + 'S')
    lb1.grid(row=8, column=0)
    lb2.grid(row=8, column=1)
    lb3.grid(row=8, column=2)
    lb4.grid(row=8, column=3)

    lb1.bind('<MouseWheel>', onmousewheel)
    lb2.bind('<MouseWheel>', onmousewheel)
    lb3.bind('<MouseWheel>', onmousewheel)
    lb4.bind('<MouseWheel>', onmousewheel)
    cur.execute("SELECT * FROM grocerylist")
    for i in cur:
        index += 1
        lb1.insert(index, str(i[0]) + ' ' + i[1])
        lb2.insert(index, i[3])
        lb3.insert(index, i[4])
        lb4.insert(index, i[5])

    c.commit()
    lb1.bind('<<ListboxSelect>>', select_mn)


def select_mn(e):
    ''' It will store the selected item from the listbox '''
    global billingsto, lb1, n, p, sl1, nm
    p = lb1.curselection()

    # Check if p is empty before accessing its elements
    if p:
        x = 0
        sl1 = ''
        cur.execute("SELECT * FROM grocerylist")
        for i in cur:
            if x == int(p[0]):
                sl1 = int(i[0])
                break
            x += 1
        c.commit()
        print(sl1)
        nm = n[x]
        print(nm)
    else:
        # Handle the case when no item is selected
        print("No item selected")



def addtothebill():
    ''' Add to bill button which allows appending the data in the bill'''
    global sl, names, nm, qty, sl1
    sl.append(sl1)
    names.append(nm)
    qty.append(qtys.get())
    print(qty)
    print(sl[len(sl) - 1], names[len(names) - 1], qty[len(qty) - 1])


def printbill():
    ''' Print the text file in pdf '''
    file_to_print = 'bill.txt'
    printer_name = win32print.GetDefaultPrinter()
    
    try:
        subprocess.run(["notepad.exe", "/p", file_to_print], shell=True)
    except Exception as e:
        print(f"Error printing the file: {e}")


def resetbill():
    ''' Clears all the textboxes in the bill '''
    global sl, names, qty
    sl = []
    names = []
    qty = []

def create_customer_table_if_not_exists():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            name TEXT,
            address TEXT
        )
    ''')
    c.commit()

def savebill():
    ''' Create Text File of Bill Format'''
    global t, c, cur, names, qty, sl, named, addd, name1, add, details

    create_bill_table_if_not_exists()
    create_customer_table_if_not_exists()  # Create the customer table if it doesn't exist

    price = [0.0] * len(sl)  # Use the correct length based on the number of items in the bill
    details = ['', '', '', '', '', '', '', '']
    details[2] = ', '.join(map(str, sl))  # Convert sl to a comma-separated string

    # Calculate the prices for each item in the bill
    for k in range(len(sl)):
        if qty[k]:  # Check if qty[k] is not an empty string
            cur.execute("SELECT * FROM grocerylist WHERE Item_No=?", (sl[k],))
            for i in cur:
                price[k] = int(qty[k]) * float(i[4])
                cur.execute("UPDATE grocerylist SET Quantity_Remain=? WHERE Item_No=?", (int(i[3]) - int(qty[k]), sl[k]))
    c.commit()

    details[5] = str(random.randint(100, 999))
    total = sum(price)
    
    # Create the bill text
    lineadd = '\n\n\n'
    lineadd += "===============================================\n"
    lineadd += "                                  No :%s\n\n" % details[5]
    lineadd += "          INDIAN SUPERMARKET\n"
    lineadd += "  Purasaiwalkam High Road, Chennai, Tamilnadu, India\n\n"
    lineadd += "-----------------------------------------------\n"
    
    if t == 1:
        lineadd += "Name: %s\n" % named
        lineadd += "Address: %s\n" % addd
        details[0] = named.lower()
        details[1] = addd.lower()
        cur.execute('SELECT * FROM customer WHERE name=?', (named,))
        for i in cur:
            details[7] = i[1]
    else:
        lineadd += "Name: %s\n" % name1.get()
        lineadd += "Address: %s\n" % add.get()
        details[0] = name1.get()
        details[1] = add.get()
        cur.execute('INSERT INTO customer VALUES (?, ?)', (details[0].lower(), details[1].lower()))
    
    lineadd += "-----------------------------------------------\n"
    lineadd += "Product                      Qty.       Price\n"
    lineadd += "-----------------------------------------------\n"
    
    for i in range(len(sl)):
        if names[i] != 'nil':
            s1 = ' '
            s1 = (names[i]) + (s1 * (27 - len(names[i]))) + s1 * (3 - len(qty[i])) + qty[i] + s1 * (
                    15 - len(str(price[i]))) + str(price[i]) + '\n'
            lineadd += s1
    
    lineadd += "\n-----------------------------------------------\n"
    lineadd += 'Total' + (' ' * 25) + (' ' * (12 - len(str(total)))) + '₹ ' + str(total) + '\n'
    details[3] = str(total)
    
    lineadd += "-----------------------------------------------\n\n"
    lineadd += "Dealer 's signature:___________________________\n"
    lineadd += "===============================================\n"
    
    p = time.localtime()
    details[4] = f"{p[2]}/{p[1]}/{p[0]}"
    details[6] = lineadd
    
    # Save the bill as a text file with UTF-8 encoding
    bill_filename = 'bill.txt'
    with open(bill_filename, 'w', encoding='utf-8') as bill_file:
        bill_file.write(lineadd)
    
    # Insert bill details into the database
    cur.execute('INSERT INTO bill (cname, cadd, items, total, date, bill) VALUES (?, ?, ?, ?, ?, ?)',
                (details[0], details[1], details[2], details[3], details[4], details[6]))
    c.commit()
    
    print("Bill saved successfully!")

def create_bill_table_if_not_exists():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS bill (
            cname TEXT,
            cadd TEXT,
            items TEXT,
            total REAL,
            date TEXT,
            billno INTEGER PRIMARY KEY,
            bill TEXT
        )
    ''')
    c.commit()

def dailyincome():
    ''' This function will allow us to show today's total income '''
    global c, cur, flag, rev, dailyinco

    # Create the "bill" table if it doesn't exist
    create_bill_table_if_not_exists()

    billtable = ('cname', 'cadd', 'items', 'total', 'date', 'billno', 'bill')
    flag = 'dailyinco'
    dailyinco = tk.Tk()
    total = 0.0
    today = str(time.localtime()[2]) + '/' + str(time.localtime()[1]) + '/' + str(time.localtime()[0])
    tk.Label(dailyinco, text='Today: ' + today).grid(row=0, column=0)
    cur.execute('SELECT * FROM bill')
    for i in cur:
        if i[4] == today:
            total += float(i[3])

    tk.Label(dailyinco, width=22, text="Today's Total Income: $ " + str(total), bg='black', fg='white').grid(row=1,
                                                                                                            column=0)
    index = 0
    vsb = tk.Scrollbar(orient='vertical')
    lb1 = tk.Listbox(dailyinco, width=25, yscrollcommand=vsb.set)
    vsb.grid(row=2, column=1, sticky='N' + 'S')
    lb1.grid(row=2, column=0)
    vsb.config(command=lb1.yview)
    cur.execute("SELECT * FROM bill")
    for i in cur:
        if i[4] == today:
            index += 1
            lb1.insert(index, 'Bill No.: ' + str(i[5]) + '    : $ ' + str(i[3]))
    c.commit()
    tk.Button(dailyinco, text='Main Menu', command=mainmenu).grid(row=15, column=0)
    dailyinco.mainloop()

def mainmenu():
    if flag == 'sto':
        sto.destroy()
    elif flag == 'billingsto':
        billingsto.destroy()
    elif flag == 'dailyinco':
        dailyinco.destroy()

# billingitems()
