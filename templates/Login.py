from tkinter import *
from functools import partial
def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    return


window = Tk()
# set window title
window.title("Shop POS")
# set window width and height
window.configure(width=500, height=300)
# set window background color
window.configure(bg='lightgray')

usernameLabel= Label(window, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(window, textvariable=username).grid(row=0, column=1)
passwordLabel = Label(window,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(window, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(window, text="Login", command=validateLogin).grid(row=4, column=0) 

window.mainloop()