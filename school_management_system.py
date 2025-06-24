import customtkinter
from customtkinter import *
from customtkinter import CTkEntry
# from school import base

root = CTk()
root.geometry("300x200")
root.title("School App")
set_appearance_mode("dark")

u = []
p = []
m = []
e = []
b = []
r = []
y = []

def home():
    pass

def submit_scores():
    m.append(mathsentry.get())
    e.append(englishentry.get())
    b.append(bstentry.get())
    r.append(rnventry.get())
    y.append(yorubaentry.get())
    a.destroy()

def score_entry():
    global a, mathsentry, englishentry, bstentry, rnventry, yorubaentry
    a = CTk()
    maths = CTkLabel(master=a, text="Mathematics", fg_color="transparent")
    mathsentry = CTkEntry(master=a)

    english = CTkLabel(master=a, text="English", fg_color="transparent")
    englishentry = CTkEntry(master=a)

    bst = CTkLabel(master=a, text="BST", fg_color="transparent")
    bstentry = CTkEntry(master=a)

    rnv = CTkLabel(master=a, text="RNV", fg_color="transparent")
    rnventry = CTkEntry(master=a)

    yoruba = CTkLabel(master=a, text="Yoruba", fg_color="transparent")
    yorubaentry = CTkEntry(master=a)

    maths.place(relx=0.1, rely=0.1)
    mathsentry.place(relx=0.3, rely=0.1)

    english.place(relx=0.1, rely=0.25)
    englishentry.place(relx=0.3, rely=0.25)

    bst.place(relx=0.1, rely=0.4)
    bstentry.place(relx=0.3, rely=0.4)

    rnv.place(relx=0.1, rely=0.55)
    rnventry.place(relx=0.3, rely=0.55)

    yoruba.place(relx=0.1, rely=0.7)
    yorubaentry.place(relx=0.3, rely=0.7)

    submit = CTkButton(master=a, text="Submit", command=submit_scores)
    submit.place(relx=0.1, rely=0.85)

    a.mainloop()

def create():
    root.destroy()
    app = CTk()
    app.geometry("300x200")

    username = CTkLabel(master=app, text="Username", fg_color="transparent")
    userentry = CTkEntry(master=app)

    password = CTkLabel(master=app, text="Password", fg_color="transparent")
    passentry = CTkEntry(master=app)

    conpass = CTkLabel(master=app, text="Confirm \n Password", fg_color="transparent")
    conentry = CTkEntry(master=app)

    register = CTkButton(master=app, text="Register", command=score_entry)

    username.place(relx=0.1, rely=0.1)
    userentry.place(relx=0.3, rely=0.1)

    password.place(relx=0.1, rely=0.3)
    passentry.place(relx=0.3, rely=0.3)

    conpass.place(relx=0.1, rely=0.5)
    conentry.place(relx=0.3, rely=0.5)

    register.place(relx=0.3, rely=0.7)
    app.mainloop()

    u.append(userentry.get())
    p.append(passentry.get())

def login():
    root.destroy()
    app = CTk()
    app.geometry("300x200")

    username = CTkLabel(master=app, text="Username", fg_color="transparent")
    userentry = CTkEntry(master=app)

    password = CTkLabel(master=app, text="Password", fg_color="transparent")
    passentry = CTkEntry(master=app)

    username.place(relx=0.1, rely=0.1)
    userentry.place(relx=0.3, rely=0.1)

    password.place(relx=0.1, rely=0.3)
    passentry.place(relx=0.3, rely=0.3)

    login_button = CTkButton(master=app, text="Login", command=lambda: print("Login button clicked"))
    login_button.place(relx=0.3, rely=0.7)
    app.mainloop()

    u.append(userentry.get())
    p.append(passentry.get())

create_button = CTkButton(master=root, text="Create \n Account", corner_radius=32, fg_color="transparent", command=create)
create_button.place(relx=0.5, rely=0.3, anchor="center")

login_button = CTkButton(master=root, text="Login", corner_radius=32, fg_color="transparent", command=login)
login_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()