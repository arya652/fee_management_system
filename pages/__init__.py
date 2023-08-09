import tkinter as tk
from tkinter import ttk


# login frame
class loginFrame(tk.Frame):
    """create object with given parent name as master and pack the object"""
    def __init__(self, master: tk.Tk):
        super().__init__(master=master, bd=2, borderwidth=2,bg="black")
        master.title('Login Page')
        master.minsize(width=500, height=350)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_rowconfigure(2, weight=4)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=4)
        self.grid_columnconfigure(3, weight=1)

        # heading text
        self.heading = ttk.Label(self, text='Login', font='"Bell MT" 26')
        self.heading.grid(row=0, column=0, columnspan=4, ipady=20)
        # username section
        self.username = tk.StringVar(self)
        self.username_lable = ttk.Label(self, text='Username: ', font='"Bell MT" 26')
        self.username_lable.grid(row=1, column=1, ipady=20)
        self.username_entry = ttk.Entry(self, textvariable=self.username, font='"Bell MT" 26')
        self.username_entry.grid(row=1, column=2, pady=20)

        # password section
        self.password = tk.StringVar(self)
        self.password_lable = ttk.Label(self, text='Password: ', font='"Bell MT" 26')
        self.password_lable.grid(row=2, column=1, ipady=20)
        self.password_entry = ttk.Entry(self, textvariable=self.password, font='"Bell MT" 26')
        self.password_entry.grid(row=2, column=2, pady=20)

        # login button
        self.submit_button = ttk.Button(self, text='SUBMIT', command=self.submit_function)
        self.submit_button.grid(row=3, column=0, columnspan=4, pady=20, ipadx=30, ipady=10)

    def submit_function(self):
        print(f'username: {self.username.get()} password: {self.password.get()}')
