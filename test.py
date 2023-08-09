import tkinter as tk
from tkinter import ttk

'''


def func1():
    frame1.pack_forget()
    frame2.pack()


def func2():
    frame2.pack_forget()
    frame1.pack()


root = tk.Tk()
root.geometry('500x300')

frame3 = tk.Frame(master=frame1, width=500, height=300, bg='Black')
frame3.grid_propagate()
tk.Label(master=frame1, text="I am frame 1").grid(row=0, column=0)
frame2 = tk.Frame(master=root, width=500, height=300, bg='Blue')
tk.Label(master=frame2, text="I am frame 2").pack()
tk.Button(master=frame1, text='next', command=func1).grid(row=0, column=1)
tk.Button(master=frame2, text='previous', command=func2).pack()
ttk.Entry(master=frame1).grid(row=1, column=0)
tk.Entry(master=frame1).grid(row=1, column=0)
letters = ('A', 'B', 'C', 'D', 'E')
spin_var = tk.StringVar(value=letters[0])
spinnBox = ttk.Spinbox(master=frame2, textvariable=spin_var)
spinnBox.pack()
spinnBox.configure(values=letters)
cnv = tk.Canvas(master=frame2, bg='black')
cnv.pack()
frame1.place(x=0, y=0)

frame1.grid()
# frame1.grid_propagate(0)

btn = tk.Button(master=frame1, text='clickme')
btn.grid(row=0, column=0)
btn.grid_propagate(0)
frame1 = tk.Frame(master=root, width=500, height=300, bg='Black')

frame_1 = tk.Frame(root, bg='#c4ffd2', width=500, height=300)
frame_1.grid()
frame_1.grid_propagate(False)

label_1 = tk.Label(frame_1, text='Name')
label_1.grid(row=0, column=0)
submit = tk.Entry(frame_1)
submit.grid(row=0, column=1)
frame_1.grid()
frame_1.grid_rowconfigure(0, weight=1)
frame_1.grid_columnconfigure(0, weight=1)
'''

# pack Excercise

'''
root = tk.Tk()
root.geometry('300x500')
lable1 = tk.Label(master=root, text='Lable1', bg='red')
lable2 = tk.Label(master=root, text='Lable2', bg='blue')
lable3 = tk.Label(master=root, text='Lable3', bg='green')
lable4 = tk.Label(master=root, text='Lable4')

lable1.pack(fill='x')
lable2.pack(expand=True)
lable3.pack(expand=True, fill='both')
lable4.pack(fill='x')
root.mainloop()
'''

# layout exercise
import pages

root = tk.Tk()
frame1 = pages.loginFrame(root)
frame1.pack(expand=True)


root.mainloop()

# root = tk.Tk()
#
# login_frame = tk.Frame(master=root)
# tk.Radiobutton(master=login_frame, value='student', )
