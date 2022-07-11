
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
    sign_in_main_frame.forget()
    return 

def sign_up_form():
    sign_up_main_frame.pack(fill='both', expand=1)
    sign_in_main_frame.forget()
    return

sign_in_main_frame = LabelFrame(root,width=width,height=height)
sign_In_Frame = LabelFrame(sign_in_main_frame,width=(width/4), height=(height/4), borderwidth = 1, relief = "solid")
f3 = Frame(width = 200, height = 100)
border = Label(sign_In_Frame, text = "Sign in to Continue",)
border.place(in_ = sign_In_Frame, anchor = "c", relx = .5, rely = .1)

sign_in_main_frame.pack(fill='both', expand=1)
sign_In_Frame.place(in_ = sign_in_main_frame, anchor="c", relx=.5,rely=.5)
f3.place(in_ = sign_In_Frame, anchor = "c", relx = .5, rely =.6)

welcome = Label(sign_in_main_frame, text="Welcome to Toribio's POS", font=("Arial", 35))
welcome.place(in_ = sign_in_main_frame, anchor = "c", relx = .5, rely = .2)
#-------login in form-------
usernameLabel= Label(f3, text="User Name").grid(row=0, column=0, pady=(20,0), padx=20)
username = StringVar()
usernameEntry = Entry(f3, textvariable=username).grid(row=0, column=1, pady=(20,0), padx=20)
passwordLabel = Label(f3,text=" Password  ").grid(row=1, column=0, pady=(20,0), padx=20)  
password = StringVar()
passwordEntry = Entry(f3, textvariable=password, show='*').grid(row=1, column=1, pady=(20,0), padx=20) 

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(f3, text="Login", command=validateLogin).grid(row=4, column=0, pady=20, padx=20) 
sign_up_btn = Button(f3, text="New Here? Sign Up!", command=sign_up_form,borderwidth=0,fg="blue",cursor="hand2").grid(row=4, column=1, pady=20, padx=20) 
# sign up form
sign_up_main_frame = LabelFrame(root,width=width,height=height)
sign_up_frame = LabelFrame(sign_up_main_frame,width=(width/4), height=(height/4), borderwidth = 1, relief = "solid", pady=20, padx=20)
sign_up_frame.place(in_ = sign_up_main_frame, anchor="c", relx=.5,rely=.5)


root.mainloop()