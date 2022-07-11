
from tkinter import *
from functools import partial


root = Tk()
root.title("Toribio's POS")

# set window to fullscreen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

def validateLogin(name, password):
    global username 
    print("username entered :", name.get())
    print("password entered :", password.get())
    username = name.get()
    loggedIn = LabelFrame(root, text="Hello " + username + " you are loggedIn", font=("Arial", 35))
    loggedIn.pack(fill='both', expand=1)
    f4.forget()
    return 
f4 = LabelFrame(root,width=(width/4), height=(height/4), borderwidth = 1, relief = "solid", pady=20, padx=20)
f3 = Frame(width = 200, height = 50)

f4.pack(fill = 'both', expand = 1)
f3.place(in_ = f4, anchor = "c", relx = .5, rely =.6)

welcome = Label(root, text="Welcome to Toribio's POS", font=("Arial", 35))
welcome.place(in_ = root, anchor = "c", relx = .5, rely = .2)

border = Label(f4, text = "Sign in to Continue", pady =20, padx=20)
border.place(in_ = f4, anchor = "c", relx = .5, rely = .1)
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
