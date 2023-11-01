import tkinter as tk
from sqlite3 import dbapi2 as sqlite
from PIL import ImageTk, Image

login = sqlite.connect("grocery.sqlite")
l = login.cursor()
WinStat = ''


def stock():
    application.destroy()
    login.close()
    import stockdetails
    a = stockdetails.stock()
    open_win()


def dailyincome():
    application.destroy()
    login.close()
    import billingdetails
    a = billingdetails.dailyincome()
    open_win()


def billingitems():
    application.destroy()
    login.close()
    import billingdetails
    a = billingdetails.billingitems()
    open_win()


def delstock():
    application.destroy()
    login.close()
    import stockdetails
    a = stockdetails.deletestock()
    open_win()


def updatestock():
    application.destroy()
    login.close()
    import stockdetails
    a = stockdetails.updatestock()
    open_win()


def expirycheck():
    application.destroy()
    login.close()
    import expirycheck
    a = expirycheck.expiry()
    open_win()

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

def again():
    global un, pwd, WinStat, root, application
    if WinStat == 'application':
        application.destroy()
    root = tk.Tk()
    root.title('INDIAN GROCERY STORE')

    # Calculate the center position for the login window
    window_width = 1050  # Adjust the desired width
    window_height = 689  # Adjust the desired height
    center_window(root, window_width, window_height)

    # Load and display the background image
    background_image = Image.open('billing/background_image.png')
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    img = ImageTk.PhotoImage(Image.open('billing/indian.gif'))
    panel = tk.Label(root, image=img)
    panel.pack()

    label1 = tk.Label(root, text='INDIAN SUPERMARKET', font='arial')
    label1.pack()

    label2 = tk.Label(root, text="Purasaiwalkam High Road, Chennai, Tamilnadu, India", font='arial')
    label2.pack()

    label3 = tk.Label(root, text='--------------------------------------------------------------')
    label3.pack()

    label4 = tk.Label(root, text='Username', font='arial')
    label4.pack()

    un = tk.Entry(root, width=20, font='arial')
    un.pack()

    label5 = tk.Label(root, text='Password', font='arial')
    label5.pack()

    pwd = tk.Entry(root, width=20, show="*", font='arial')
    pwd.pack()

    tk.Button(root, width=15, text='Enter', font='arial', command=check).pack()
    tk.Button(root, width=15, text='Close', font='arial', command=root.destroy).pack()

    root.mainloop()


def check():
    ''' Check Button for Login Window '''
    global un, pwd, root
    u = un.get()
    p = pwd.get()
    if 'admin' != u and 'admin' != p:
        top = tk.Tk()
        tk.Label(top, width=30, text='Wrong Username or Password').grid(row=0, column=0)
        top.destroy()
        top.mainloop()
    else:
        root.destroy()
        open_win()


def open_win():
    ''' Opens Main Window '''
    global application, WinStat
    WinStat = 'application'
    application = tk.Tk()

    application.title("INDIAN GROCERY STORE")
    application.geometry("1100x640")

    ''' Main Window Picture '''
    img = ImageTk.PhotoImage(Image.open('billing/collage.jpg'))
    panel = tk.Label(application, image=img)
    panel.grid(row=0, column=0, columnspan=5)

    menu_bar = tk.Menu(application)
    stock_menu = tk.Menu(menu_bar, tearoff=0)
    expiry_menu = tk.Menu(menu_bar, tearoff=0)
    billing_menu = tk.Menu(menu_bar, tearoff=0)
    '''Stock Maintenance'''
    stock_menu.add_command(label="Add Items", command=stock)
    stock_menu.add_command(label="Delete Items", command=delstock)
    stock_menu.add_command(label="Update Items", command=updatestock)
    '''Expiry Check'''
    expiry_menu.add_command(label="Check Expiry", command=expirycheck)
    '''Billing'''
    billing_menu.add_command(label="Billing", command=billingitems)
    billing_menu.add_command(label="Check Today's Income", command=dailyincome)

    menu_bar.add_cascade(label="Stock Maintenance", menu=stock_menu)
    menu_bar.add_cascade(label="Expiry", menu=expiry_menu)
    menu_bar.add_cascade(label="Billing", menu=billing_menu)
    menu_bar.add_cascade(label="Logout", command=again)
    application.config(menu=menu_bar)

    # Add buttons for Stock Maintenance, Expiry Check, Billing, and Logout
    stock_button = tk.Button(application, text="Add Stock", command=stock, font="arial")
    stock_button.grid(row=1, column=0, padx=10, pady=10)

    stock_button = tk.Button(application, text="Delete Stock", command=delstock, font="arial")
    stock_button.grid(row=2, column=0, padx=10, pady=10)

    stock_button = tk.Button(application, text="Update Stock", command=updatestock, font="arial")
    stock_button.grid(row=3, column=0, padx=10, pady=10)

    expiry_button = tk.Button(application, text="Expiry Check", command=expirycheck, font="arial")
    expiry_button.grid(row=1, column=1, padx=10, pady=10)

    billing_button = tk.Button(application, text="Billing", command=billingitems, font="arial")
    billing_button.grid(row=2, column=1, padx=10, pady=10)
    
    billing_button = tk.Button(application, text="Check Today's Income", command=dailyincome, font="arial")
    billing_button.grid(row=3, column=1, padx=10, pady=10)

    logout_button = tk.Button(application, text="Logout", command=again, font="arial")
    logout_button.grid(row=1, column=2, padx=10, pady=10)

    application.mainloop()


again()
