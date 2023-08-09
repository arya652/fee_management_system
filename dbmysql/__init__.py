import datetime
import mysql.connector


class DataBase:
    def __init__(self, user='root', password='', host='localhost', port=3306):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )
        self.cursor = self.db.cursor()
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS feeManagementSystem;')
        self.cursor.execute('USE feemanagementsystem')
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), rollnumber INTEGER UNSIGNED UNIQUE, cource ENUM('BCA','BBA','MCA','MBA'), total_fee DECIMAL(10,2), remaining_fee DECIMAL(10,2) DEFAULT (total_fee));")
        self.cursor.execute(
            'create table if not exists fee_table (id int primary key auto_increment, student_id int, fee_amnt decimal(10,2), payment_date date, foreign key (student_id) references student(id));')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(20), password VARCHAR(20), s_id INT, isadmin BOOLEAN, FOREIGN KEY (s_id) REFERENCES student(id) ON DELETE CASCADE);')

    def addStudent(self, name: str | None, roll_number: int | None, course: str | None, total_fee: int | None):
        self.cursor.execute(f"INSERT INTO student (name,rollnumber,cource,total_fee) VALUES ('{name}',{roll_number},'{course}',{total_fee});")
        self.db.commit()

    def removeStudent(self, roll_number):
        self.cursor.execute(f"DELETE FROM student WHERE rollnumber={roll_number};")

    def showStudents(self, roll_number: int = None):
        if roll_number is None:
            self.cursor.execute('SELECT * FROM student;')
        else:
            self.cursor.execute(f'SELECT * FROM student WHERE rollnumber={roll_number};')
        return self.cursor.fetchall()

    def addUser(self, username: str | None, password: str | None, student_id: int | None):
        is_admin = (student_id is None) if True else False
        if student_id is None :
            student_id = 'null'
        self.cursor.execute(f"INSERT INTO users (username, password, isadmin, s_id) VALUES ('{username}','{password}', {is_admin}, {student_id});")
        self.db.commit()

    def showUsers(self):
        self.cursor.execute('SELECT * FROM users;')
        return self.cursor.fetchall()

    def show_fee_entries(self, student_id: int = None):
        if student_id is None:
            self.cursor.execute('SELECT * FROM fee_table;')
        else:
            self.cursor.execute(f'SELECT * FROM fee_table WHERE student_id={student_id};')
        return self.cursor.fetchall()

    def fee_entry(self, student_id: int, fee_amnt: int, payment_date: datetime=datetime.date.today()):
        self.cursor.execute(f"INSERT INTO fee_table (student_id, fee_amnt, payment_date) VALUES ({student_id},{fee_amnt},'{payment_date}');")
        self.cursor.reset(True)
        self.db.commit()


    def remove_entry(self, entery_id: int):
        self.cursor.execute(f"DELETE FROM fee_table WHERE id={entery_id};")

    def checkLoginInfo(self, username: str, password: str):
        self.cursor.execute(f'SELECT * FROM users WHERE username = "{username}";')
        res = self.cursor.fetchone()
        if res is not None:
            if res[2] == password:
                return {
                    'id': res[0],
                    'stu_id': res[-2],
                    'admin': res[-1]
                }
        return {
            'id': None,
            'stu_id': None,
            'admin': None
        }

    def __del__(self):
        self.cursor.close()
        self.db.close()
        print("Db is closed")
