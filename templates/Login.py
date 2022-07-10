
from tkinter import *
# from functools import partial
# import tkinter

# print(tkinter.__file__)
# import sys

# # 👇️ print all built-in module names
# print(sys.builtin_module_names)
# def validateLogin(username, password):
#     print("username entered :", username.get())
#     print("password entered :", password.get())
#     return

# # print(dir(tk))
root = Tk()

myLabel = Label(root, text = " Hello world")

root.mainloop()
# # set window title
# root.title("Shop POS")
# # set window width and height
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# # f1= root.geometry("%dx%d" % (width, height))
# # f1.configure(bg='gray')
# f1 = Frame(root.geometry("%dx%d" % (width, height)))
# f4 = Frame(width=(width/4), height=(height/4), borderwidth = 1, relief = "solid", pady=20, padx=20)
# f3 = Frame(width = 200, height = 50)

# f1.pack(fill="both", expand=True, padx=20, pady=20)
# f4.place(in_=f1, anchor = "c", relx = .5, rely = .5)
# f3.place(in_ = f4, anchor = "c", relx = .5, rely =.6)

# border = Label(f4, text = "Sign in to Continue", pady =20, padx=20)
# border.place(in_ = f4, anchor = "c", relx = .5, rely = .1)

# welcome = Label(f1, text="Welcome to Toribio's POS", font=("Arial", 35))
# welcome.place(in_ = f1, anchor = "c", relx = .5, rely = .2)

# usernameLabel= ttk.Label(f3, text="User Name").grid(row=0, column=0, pady=(20,0), padx=20)
# username = StringVar()
# usernameEntry = Entry(f3, textvariable=username).grid(row=0, column=1, pady=(20,0), padx=20)
# passwordLabel = Label(f3,text=" Password  ").grid(row=1, column=0, pady=(20,0), padx=20)  
# password = StringVar()
# passwordEntry = Entry(f3, textvariable=password, show='*').grid(row=1, column=1, pady=(20,0), padx=20)  

# validateLogin = partial(validateLogin, username, password)

# #login button
# loginButton = Button(f3, text="Login", command=validateLogin).grid(row=4, column=0, pady=20, padx=20) 

root.mainloop()