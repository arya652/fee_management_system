# import tkinter as tk
# from tkinter import ttk
#
# def login():
#     root.destroy()
#     page = tk.Tk()
#     page.geometry('500x500')
#     tk.Label(master=page, text= "Login").pack()
#     page.mainloop()
#
# root = tk.Tk()
# root.geometry('500x500')
# tk.Button(master=root, text="Login", command=login).pack()
#
# root.mainloop()


import dbmysql

db = dbmysql.DataBase()
# for x in db.showStudents():
#     print(x)
#
# db.removeStudent(1544)
# db.addStudent('Shivam', 1544, 'BCA', 22500)
fee_data = [(1, 500.00, '2023-07-01'),
            (2, 600.00, '2023-07-02'),
            (3, 550.00, '2023-07-03'),
            (4, 750.00, '2023-07-04'),
            (5, 600.00, '2023-07-05'),
            (6, 500.00, '2023-07-06'),
            (7, 700.00, '2023-07-07'),
            (8, 650.00, '2023-07-08'),
            (9, 600.00, '2023-07-09'),
            (10, 700.00, '2023-07-10'),
            (1, 450.00, '2023-07-11'),
            (2, 550.00, '2023-07-12'),
            (3, 500.00, '2023-07-13'),
            (4, 700.00, '2023-07-14'),
            (5, 550.00, '2023-07-15'),
            (6, 450.00, '2023-07-16'),
            (7, 650.00, '2023-07-17'),
            (8, 600.00, '2023-07-18'),
            (9, 550.00, '2023-07-19'),
            (10, 650.00, '2023-07-20')]

user_data = [('user1', 'password1',False, 1),
    ('user2', 'password2', False, 2),
    ('user3', 'password3', False, 3),
    ('user4', 'password4', True, 4),
    ('user5', 'password5', False, 5),
    ('user6', 'password6', False, 6),
    ('user7', 'password7', True, 7),
    ('user8', 'password8', False, 8),
    ('user9', 'password9', False, 9),
    ('user10', 'password10', False, 10),
    ('user11', 'password11', True, 11),
    ('user12', 'password12', False, 12),
    ('user13', 'password13', False, 13),
    ('user14', 'password14', True, 14),
    ('user15', 'password15', False, 15),
    ('user16', 'password16', False, 16),
    ('user17', 'password17', True, 17),
    ('user18', 'password18', False, 18),
    ('user19', 'password19', False, 19),
    ('user20', 'password20', True, 20)]
# db.addUser('Shiva', 'dsjdklaj', 30)
# for x in db.show_fee_entries():
#     print(x)
# db.show_fee_entries()
print(db.checkLoginInfo('user1', 'password1'))
print(db.showStudents(1006))

# for data in user_data:
#     db.addUser(data[0], data[1], data[-1])

# for x in db.showUsers():
#     print(x)

class student:
    def __init__(self, a: tuple):
        self.id = a[0]
        self.name = a[1]
        self.roll_number = a[2]
        self.course = a[3]
        self.t_fee = int(a[4])
        self.r_fee = int(a[5])

    def show_info(self):
        print('student_id',self.id)
        print('student_name',self.name)
        print('student_roll_number',self.roll_number)


stu = student(db.showStudents(1006)[0])

stu.show_info()
#

# import dbmysql
# import pages











