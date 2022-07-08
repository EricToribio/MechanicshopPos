import tkinter as tk
from tkinter import *
from functools import partial
def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    return


root = tk.Tk()
# set window title
root.title("Shop POS")
# set window width and height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# f1= root.geometry("%dx%d" % (width, height))
# f1.configure(bg='gray')
f1 = tk.Frame(root.geometry("%dx%d" % (width, height)))
f4 = tk.Frame(width=(width/4), height=(height/4), borderwidth = 1, relief = "solid", pady=20, padx=20)
f3 = tk.Frame(width = 200, height = 50)

f1.pack(fill="both", expand=True, padx=20, pady=20)
f4.place(in_=f1, anchor = "c", relx = .5, rely = .5)
f3.place(in_ = f4, anchor = "c", relx = .5, rely =.6)

border = Label(f4, text = "Sign in to Continue", pady =20, padx=20)
border.place(in_ = f4, anchor = "c", relx = .5, rely = .1)

welcome = Label(f1, text="Welcome to Toribio's POS", font=("Arial", 35))
welcome.place(in_ = f1, anchor = "c", relx = .5, rely = .2)

usernameLabel= Label(f3, text="User Name").grid(row=0, column=0, pady=(20,0), padx=20)
username = StringVar()
usernameEntry = Entry(f3, textvariable=username).grid(row=0, column=1, pady=(20,0), padx=20)
passwordLabel = Label(f3,text=" Password  ").grid(row=1, column=0, pady=(20,0), padx=20)  
password = StringVar()
passwordEntry = Entry(f3, textvariable=password, show='*').grid(row=1, column=1, pady=(20,0), padx=20)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(f3, text="Login", command=validateLogin).grid(row=4, column=0, pady=20, padx=20) 

root.mainloop()