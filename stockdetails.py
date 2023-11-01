import tkinter as tk
from sqlite3 import dbapi2 as sqlite

columns = ('Item_No', 'Item_Name', 'Item_Type', 'Quantity_Remain', 'Item_Cost', 'Expiry_Date', 'Manufactured_By')

c = sqlite.connect("grocery.sqlite")
cur = c.cursor()

def autoincre():
    ''' To auto-generate item No '''
    cur.execute("select max(Item_No) from grocerylist")
    incval = cur.fetchone()
    if incval and incval[0] is not None:
        incval = incval[0] + 1
    else:
        incval = 1
    return incval

def stock():
    ''' Stock User GUI here '''
    global cur, c, columns, value, flag, sto, application
    
    flag = 'sto'
    value = [''] * len(columns)
    sto = tk.Tk()
    sto.title('Add Stock')
    tk.Label(sto, text='Enter a New Item to the Grocery Stock').grid(row=0, column=0, columnspan=2)
    tk.Label(sto, text='-' * 50).grid(row=1, column=0, columnspan=2)

    tk.Label(sto, width=15, text=str(columns[0]) + ':', justify='left').grid(row=3, column=0, sticky='w')
    autovalue = autoincre()
    value[0] = tk.Entry(sto)
    value[0].grid(row=3, column=1)
    value[0].insert(0, str(autovalue))

    tk.Label(sto, width=15, text=str(columns[1]) + ':', justify='left').grid(row=4, column=0, sticky='w')
    value[1] = tk.Entry(sto)
    value[1].grid(row=4, column=1)
    
    tk.Label(sto, width=15, text=str(columns[2]) + ':', justify='left').grid(row=5, column=0, sticky='w')
    value[2] = tk.Entry(sto)
    value[2].grid(row=5, column=1)
    
    tk.Label(sto, width=15, text=str(columns[3]) + ':', justify='left').grid(row=6, column=0, sticky='w')
    value[3] = tk.Entry(sto)
    value[3].grid(row=6, column=1)
    
    tk.Label(sto, width=15, text=str(columns[4]) + ':', justify='left').grid(row=7, column=0, sticky='w')
    value[4] = tk.Entry(sto)
    value[4].grid(row=7, column=1)
    
    tk.Label(sto, width=15, text=str(columns[5]) + ':', justify='left').grid(row=8, column=0, sticky='w')
    value[5] = tk.Entry(sto)
    value[5].grid(row=8, column=1)
    
    tk.Label(sto, width=15, text=str(columns[6]) + ':', justify='left').grid(row=9, column=0, sticky='w')
    value[6] = tk.Entry(sto)
    value[6].grid(row=9, column=1)
    
    ref()
    
    tk.Button(sto, width=15, text='Submit', command=chk).grid(row=12, column=1)
    tk.Label(sto, text='-' * 165).grid(row=13, column=0, columnspan=7)
    tk.Button(sto, width=15, text='Refresh stock', command=ref).grid(row=12, column=4)
    
    for i in range(1, 7):
        tk.Label(sto, text=columns[i]).grid(row=14, column=i-1)
    
    tk.Button(sto, width=10, text='Main Menu', command=mainmenu).grid(row=12, column=5)
    
    sto.mainloop()

def updatestock():
    ''' Which item to Update GUI '''
    global cur, c, flag, lb1, updatesto, valueupx
    
    valueupx = ''
    flag = 'updatesto'
    updatesto = tk.Tk()
    updatesto.title("Update grocery item from Stock")
    tk.Label(updatesto, text='Enter the Item No to Update').grid(row=1, column=0)
    valueupx = tk.Entry(updatesto)
    valueupx.grid(row=1, column=1)
    tk.Label(updatesto, text='Item').grid(row=2, column=0)
    tk.Label(updatesto, text='Qty Remain').grid(row=2, column=1)
    tk.Label(updatesto, text='Cost').grid(row=2, column=2)
    tk.Label(updatesto, text='Expiry Date').grid(row=2, column=3)

    displayupdate()
    tk.Button(updatesto, width=20, text='Update', command=updatestockbutton).grid(row=1, column=3)
    tk.Button(updatesto, width=20, text='Main Menu', command=mainmenu).grid(row=5, column=3) 
    updatesto.mainloop()

def updatestockbutton():
    ''' Update Stock Button GUI '''
    global valueupx, cur, valueupxy, updateitemno, flag, updatestobut

    index = 0
    updateitemno = valueupx.get()
    print(updateitemno)
    updatesto.destroy()

    flag = 'updatestobut'
    updatestobut = tk.Tk()
    updatestobut.title("Update grocery item from Stock")
    tk.Label(updatestobut, text='Enter the Item to update to the Grocery Stock').grid(row=0, column=0, columnspan=2)
    col = ('ItemNo', 'ItemName', 'QtyRem', 'Cost', 'Expiry', 'ItemType', 'ManufacturedBy')
    valueupxy = [''] * len(col)

    # Add a label and an entry field for "Item No"
    tk.Label(updatestobut, text='Item_No').grid(row=2, column=0)
    valueupxy[0] = tk.Entry(updatestobut)
    valueupxy[0].grid(row=2, column=1)

    tk.Label(updatestobut, text='Item_Name').grid(row=4, column=0)
    valueupxy[1] = tk.Entry(updatestobut)
    valueupxy[1].grid(row=4, column=1)

    tk.Label(updatestobut, text='Quantity_Remain').grid(row=6, column=0)
    valueupxy[2] = tk.Entry(updatestobut)
    valueupxy[2].grid(row=6, column=1)

    tk.Label(updatestobut, text='Cost').grid(row=8, column=0)
    valueupxy[3] = tk.Entry(updatestobut)
    valueupxy[3].grid(row=8, column=1)

    tk.Label(updatestobut, text='Expiry_Date').grid(row=10, column=0)
    valueupxy[4] = tk.Entry(updatestobut)
    valueupxy[4].grid(row=10, column=1)

    # Add labels and entry fields for "Item Type" and "Manufactured By"
    tk.Label(updatestobut, text='Item_Type').grid(row=12, column=0)
    valueupxy[5] = tk.Entry(updatestobut)
    valueupxy[5].grid(row=12, column=1)

    tk.Label(updatestobut, text='Manufactured_By').grid(row=14, column=0)
    valueupxy[6] = tk.Entry(updatestobut)
    valueupxy[6].grid(row=14, column=1)

    cur.execute('select * from grocerylist where Item_No=?', updateitemno)
    for i in cur:
        index += 1
        valueupxy[0].insert(index, i[0])  # Insert "Item No"
        valueupxy[1].insert(index, i[1])
        valueupxy[2].insert(index, i[3])
        valueupxy[3].insert(index, i[4])
        valueupxy[4].insert(index, i[5])
        valueupxy[5].insert(index, i[2])  # Insert "Item Type"
        valueupxy[6].insert(index, i[6])  # Insert "Manufactured By"
    c.commit()

    tk.Button(updatestobut, width=20, text='Update', command=updatesql).grid(row=16, column=0)
    tk.Button(updatestobut, width=20, text='Main Menu', command=mainmenu).grid(row=16, column=1)
    updatestobut.mainloop()

def create_grocerylist_table_if_not_exists(cur):
    # Check if the "grocerylist" table exists, and create it if it doesn't
    cur.execute('''
        CREATE TABLE IF NOT EXISTS grocerylist (
            Item_No INTEGER PRIMARY KEY,
            Item_Name TEXT,
            Quantity_Remain INTEGER,
            Item_Cost REAL,
            Expiry_Date TEXT
        )
    ''')

def updatesql():
    ''' Update in the database '''
    global updatestobut, valueupxy, updateitemno, cur, c
    
    itemno = updateitemno
    upitemname = valueupxy[0].get()
    upqtyremai = valueupxy[1].get()
    upcost = valueupxy[2].get()
    upexpiry = valueupxy[3].get()
    
    print(itemno)
    print(upitemname)
    print(upqtyremai)
    print(upcost)
    print(upexpiry)

    # Create the "grocerylist" table if it doesn't exist
    create_grocerylist_table_if_not_exists(cur)
    
    cur.execute('''
        UPDATE grocerylist 
        SET Item_Name=?, Quantity_Remain=?, Item_Cost=?, Expiry_Date=? 
        WHERE Item_No=?
    ''', (upitemname, upqtyremai, upcost, upexpiry, itemno))
    
    top = tk.Tk()
    tk.Label(top, width=20, text='Modified!').pack()
    c.commit()
    top.mainloop()

def displayupdate():
    ''' Display data from database for Update '''
    global lb1, updatesto, cur, c
    
    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)
    
    index = 0
    vsb = tk.Scrollbar(orient='vertical', command=onvsb)
    lb1 = tk.Listbox(updatesto, width=25, yscrollcommand=vsb.set)
    lb2 = tk.Listbox(updatesto, width=7, yscrollcommand=vsb.set)
    lb3 = tk.Listbox(updatesto, width=7, yscrollcommand=vsb.set)
    lb4 = tk.Listbox(updatesto, width=13, yscrollcommand=vsb.set)
    
    vsb.grid(row=3, column=2, sticky='ns')
    lb1.grid(row=3, column=0)
    lb2.grid(row=3, column=1)
    lb3.grid(row=3, column=2)
    lb4.grid(row=3, column=3)
    
    cur.execute("select * from grocerylist")
    for i in cur:
        index += 1
        lb1.insert(index, str(i[0]) + ')  ' + i[1])
        lb2.insert(index, i[3])
        lb3.insert(index, i[4])
        lb4.insert(index, i[5])
    c.commit()

def chk():
    ''' Add new Stock Item '''
    global value, c, cur, columns, sto

    # Calculate the new Item_No (y) by finding the maximum and adding 1
    cur.execute("SELECT MAX(Item_No) FROM grocerylist")
    result = cur.fetchone()
    if result[0] is not None:
        y = result[0] + 1
    else:
        y = 1

    x = [''] * 10
    
    for i in range(1, 7):
        x[i] = value[i].get()
    
    sql = "INSERT INTO grocerylist VALUES (?, ?, ?, ?, ?, ?, ?)"
    values = (y, x[1], x[2], x[3], x[4], x[5], x[6])
    cur.execute(sql, values)
    c.commit()
    
    top = tk.Tk()
    tk.Label(top, width=20, text='Success!').pack()
    top.mainloop()

def deletestock():
    ''' Delete Stock GUI '''
    global cur, c, flag, lb1, delsto, valuex
    
    valuex = ''
    flag = 'delsto'
    delsto = tk.Tk()
    delsto.title("Delete grocery item from Stock")
    tk.Label(delsto, text='Enter the Item No to Delete').grid(row=1, column=0)
    valuex = tk.Entry(delsto)
    valuex.grid(row=1, column=1)
    tk.Label(delsto, text='Item').grid(row=2, column=0)
    tk.Label(delsto, text='Qty Remain').grid(row=2, column=1)
    tk.Label(delsto, text='Cost').grid(row=2, column=2)
    tk.Label(delsto, text='Expiry Date').grid(row=2, column=3)
    
    displayren()
    
    tk.Button(delsto, width=20, text='Delete', command=deletestockbutton).grid(row=1, column=3)
    tk.Button(delsto, width=20, text='Main Menu', command=mainmenu).grid(row=5, column=3) 
    delsto.mainloop()

def deletestockbutton():
    ''' Deleting from the table '''
    global p, c, cur, delsto, valuex
    
    item_no = valuex.get()  # Assuming valuex contains the Item_No you want to delete
    cur.execute("DELETE FROM grocerylist WHERE Item_No=?", (item_no,))
    c.commit()
    displayren()

def displayren():
    global lb1, delsto, cur, c
    
    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)
    
    index = 0
    vsb = tk.Scrollbar(orient='vertical', command=onvsb)
    lb1 = tk.Listbox(delsto, width=25, yscrollcommand=vsb.set)
    lb2 = tk.Listbox(delsto, width=7, yscrollcommand=vsb.set)
    lb3 = tk.Listbox(delsto, width=7, yscrollcommand=vsb.set)
    lb4 = tk.Listbox(delsto, width=13, yscrollcommand=vsb.set)
    
    vsb.grid(row=3, column=2, sticky='ns')
    lb1.grid(row=3, column=0)
    lb2.grid(row=3, column=1)
    lb3.grid(row=3, column=2)
    lb4.grid(row=3, column=3)
    
    cur.execute("select * from grocerylist")
    for i in cur:
        index += 1
        lb1.insert(index, str(i[0]) + ')  ' + str(i[1]))
        lb2.insert(index, i[3])
        lb3.insert(index, i[4])
        lb4.insert(index, i[5])
    c.commit()

def ref(): 
    ''' Multilistbox to show all the data in the database '''
    global sto, cur, c
    
    def scrollbarv(*args):
        lb1.yview(*args)
        lb2.yview(*args)
        lb3.yview(*args)
        lb4.yview(*args)
        lb5.yview(*args)
        lb6.yview(*args)
    
    index = 0
    sc_bar = tk.Scrollbar(orient='vertical', command=scrollbarv)
    lb1 = tk.Listbox(sto, yscrollcommand=sc_bar.set)
    lb2 = tk.Listbox(sto, yscrollcommand=sc_bar.set)
    lb3 = tk.Listbox(sto, yscrollcommand=sc_bar.set, width=7)
    lb4 = tk.Listbox(sto, yscrollcommand=sc_bar.set, width=7)
    lb5 = tk.Listbox(sto, yscrollcommand=sc_bar.set, width=20)
    lb6 = tk.Listbox(sto, yscrollcommand=sc_bar.set, width=20)
    
    sc_bar.grid(row=15, column=6, sticky='ns')
    lb1.grid(row=15, column=0)
    lb2.grid(row=15, column=1)
    lb3.grid(row=15, column=2)
    lb4.grid(row=15, column=3)
    lb5.grid(row=15, column=4)
    lb6.grid(row=15, column=5)
    
    cur.execute("select * from grocerylist")
    for i in cur:
        index += 1
        lb1.insert(index, str(i[0]) + '. ' + str(i[1]))
        lb2.insert(index, i[2])
        lb3.insert(index, i[3])
        lb4.insert(index, i[4])
        lb5.insert(index, i[5])
        lb6.insert(index, i[6])
    c.commit()   

def mainmenu():
    ''' Main Menu Button '''
    if flag == 'sto':
        sto.destroy()
    elif flag == 'delsto':
        delsto.destroy()  
    elif flag == 'updatestobut':
        updatestobut.destroy()
    elif flag == 'updatesto':
        updatesto.destroy()

if __name__ == "__main__":
    stock()
