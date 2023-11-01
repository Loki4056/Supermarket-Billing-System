import tkinter as tk
from sqlite3 import dbapi2 as sqlite
import time

columns = ('Item_No', 'Item_Name', 'Item_Type', 'Quantity_Remain', 'Item_Cost', 'Expiry_Date', 'Manufactured_By')

c = sqlite.connect("grocery.sqlite")
cur = c.cursor()

def create_table_if_not_exists():
    cur.execute('''CREATE TABLE IF NOT EXISTS grocerylist (
                    Item_No INTEGER PRIMARY KEY,
                    Item_Name TEXT NOT NULL,
                    Item_Type TEXT,
                    Quantity_Remain INTEGER,
                    Item_Cost REAL,
                    Expiry_Date DATE,
                    Manufactured_By TEXT
                )''')
    c.commit()

def expiry():
    ''' Expiry GUI '''
    global expirychk, expdate, c, cur, flag
    total = 0.0
    today = str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(time.localtime().tm_year)

    flag = 'expirychk'
    groitem = []
    cur.execute("select * from grocerylist")
    for i in cur:
        groitem.append(i[1])
    c.commit()
    expirychk = tk.Tk()
    expirychk.title('Check Expiry of the Items')
    tk.Label(expirychk, text='Today: ' + today).grid(row=0, column=0, columnspan=3)
    tk.Label(expirychk, text='Its Illegal to sell expired items').grid(row=1, column=0, columnspan=3)
    tk.Label(expirychk, text='-' * 80).grid(row=2, column=0, columnspan=3)
    expdate = tk.Spinbox(expirychk, values=groitem)
    expdate.grid(row=3, column=0)
    tk.Button(expirychk, text='Check Expiry date', command=chkexpiry).grid(row=3, column=1)
    tk.Label(expirychk, text='-' * 80).grid(row=4, column=0, columnspan=3)

    tk.Button(expirychk, text='Main Menu', command=mainmenu).grid(row=5, column=2)
    expirychk.mainloop()


def chkexpiry():
    ''' Check Expiry Date button will navigate here '''
    global c, cur, expdate, expirychk
    cur.execute("select * from grocerylist")
    for i in cur:
        if (i[1] == expdate.get()):
            tk.Label(expirychk, text=i[5]).grid(row=3, column=2)
    c.commit()


def mainmenu():
    if flag == 'expirychk':
        expirychk.destroy()


# expiry()
