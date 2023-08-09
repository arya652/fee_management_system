import tkinter as tk
from tkinter import ttk

class login_page(tk.Frame):
    def __init__(self,master):
        super().__init__(master, bg="#00b2ca",borderwidth=20,relief="ridge")
        #variables
        self.bg="#00b2ca"

        #Definig ]grid

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_rowconfigure(2, weight=4)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=4)
        self.grid_columnconfigure(3, weight=1)

        #heading text
        self.heading = tk.Label(self, text='Login', font='"Bell MT" 26',bg= self.bg,fg="black")
        self.heading.grid(row=0, column=0, columnspan=4, ipady=20)

        #username section
        self.username = tk.StringVar(self)
        self.username_lable = tk.Label(self, text='Username: ', font='"Bell MT" 26',bg=self.bg,fg="black")
        self.username_lable.grid(row=1, column=1, ipady=20)
        self.username_entry = tk.Entry(self, textvariable=self.username, font='"Bell MT" 26')
        self.username_entry.grid(row=1, column=2, pady=20)

        # password section
        self.password = tk.StringVar(self)
        self.password_lable = tk.Label(self, text='Password: ', font='"Bell MT" 26',fg="black",bg=self.bg)
        self.password_lable.grid(row=2, column=1, ipady=20)
        self.password_entry = tk.Entry(self, textvariable=self.password, font='"Bell MT" 26')
        self.password_entry.grid(row=2, column=2, pady=20)

        # login button
        self.submit_button = ttk.Button(self, text='SUBMIT')
        self.submit_button.grid(row=3, column=0, columnspan=4, pady=20, ipadx=30, ipady=10)

class student_page(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.sub_font= ("Arial",20,"bold")
        self.bg= '#416788'
        self.student_name = tk.StringVar(value='Shruti Kuttiya')
        self.student_roll_no = tk.IntVar(value=34567)
        self.student_course = tk.StringVar(value='Shruti Kuttiya')
        self.student_semester = tk.StringVar(value='Shruti Kuttiya')
        self.student_total_fee = tk.IntVar(value=22500)


        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        #heading
        self.heading=tk.Label(self,text="Student Information",font='"Bell MT" 26',bg=self.bg,fg="black")
        self.heading.grid(row=0,column=1,padx=20,pady=20)

        self.info_frame = tk.Frame(self)
        self.info_frame.grid(row=1,column=1)
        self.info_frame.grid_rowconfigure(0,weight=1)
        self.info_frame.grid_rowconfigure(1,weight=1)
        self.info_frame.grid_rowconfigure(2,weight=1)
        self.info_frame.grid_rowconfigure(3,weight=1)
        self.info_frame.grid_rowconfigure(4,weight=1)
        self.info_frame.grid_rowconfigure(5,weight=1)
        self.info_frame.grid_rowconfigure(6,weight=1)
        self.info_frame.grid_rowconfigure(7,weight=1)
        self.info_frame.grid_rowconfigure(8,weight=1)

        self.info_frame.grid_columnconfigure(0,weight=1)
        self.info_frame.grid_columnconfigure(1,weight=1)
        self.info_frame.grid_columnconfigure(2,weight=1)
        self.info_frame.grid_columnconfigure(3,weight=1)
        self.info_frame.grid_columnconfigure(4,weight=1)
        self.info_frame.grid_columnconfigure(5,weight=1)

        self.student_name_label=tk.Label(self.info_frame,text="Student Name:", font=self.sub_font)
        self.student_name_label.grid(row=0, column=1 , sticky='w', pady=10, padx=20)
        self.student_name_value=tk.Label(self.info_frame,textvariable=self.student_name, font=self.sub_font)
        self.student_name_value.grid(row= 0, column=2 , sticky='w', pady=10, padx=20)
        self.student_roll_label=tk.Label(self.info_frame,text="Roll- No:", font=self.sub_font)
        self.student_roll_label.grid(row= 1, column=1 , sticky='w', pady=10, padx=20)
        self.student_roll_value=tk.Label(self.info_frame,textvariable=self.student_roll_no, font=self.sub_font)
        self.student_roll_value.grid(row= 1, column=2 , sticky='w', pady=10, padx=20)
        self.student_course_label=tk.Label(self.info_frame,text="Course:", font=self.sub_font)
        self.student_course_label.grid(row= 2, column=1, sticky='w', pady=10, padx=20)
        self.student_course_value=tk.Label(self.info_frame,textvariable=self.student_course, font=self.sub_font)
        self.student_course_value.grid(row=2, column=2, sticky='w', pady=10, padx=20)
        self.student_semester_label=tk.Label(self.info_frame,text="Semester:", font=self.sub_font)
        self.student_semester_label.grid(row=3, column=1, sticky='w', pady=10, padx=20)
        self.student_semester_value=tk.Label(self.info_frame,textvariable=self.student_semester, font=self.sub_font)
        self.student_semester_value.grid(row=3, column=2, sticky='w', pady=10, padx=20)
        self.seperator = tk.Frame(self.info_frame,height=2, bg='black').grid(row=3,column=0, columnspan=6, sticky='sew')
        #Fees section
        self.fee_section_label=tk.Label(self.info_frame,text="Fees Section:-",bg=self.bg,fg="black",font=self.sub_font)
        self.fee_section_label.grid(row=4,column=1)

        self.total_fees_label=tk.Label(self.info_frame,text="Total Fees:-",bg=self.bg,font=self.sub_font)
        self.total_fees_label.grid(row=5,column=1)

        self.total_fees_value=tk.Label(self.info_frame,textvariable=self.student_total_fee,bg=self.bg,font=self.sub_font)
        self.total_fees_value.grid(row=5,column=2)

        self.fees_remain_label=tk.Label(self.info_frame,text="Remaining Fees:-",bg=self.bg,font=self.sub_font)


root = tk.Tk()
root.config( bg="lightblue")
a=student_page(root)
a.pack(expand=True,ipadx= 20,ipady= 20)
root.mainloop()




