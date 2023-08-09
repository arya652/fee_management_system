# creating database
CREATE DATABASE IF NOT EXISTS xyz;
use feemanagementsystem;

# creating tables
create table if not exists student (
id int auto_increment primary key, 
name varchar(20), 
rollnumber integer unsigned unique, 
cource enum('BCA','BBA','MCA','MBA'), 
total_fee decimal(10,2), 
remaining_fee decimal(10,2) default (total_fee)
);

create table if not exists fee_table (
student_id int, 
fee_amnt decimal(10,2), 
fee_date date, 
foreign key (student_id) references student(id)
);

create table if not exists users(
id int primary key auto_increment, 
username varchar(20),
password varchar(20),
s_id int,
isadmin boolean,
foreign key (s_id) references student(id) on delete cascade
);

# inserting data in student
insert into student (name,rollnumber,cource,total_fee) values 
('Alice', 1001, 'BCA', 75000.00),
('Bob', 1002, 'BBA', 62000.00),
('Charlie', 1003, 'MCA', 89000.00),
('David', 1004, 'MBA', 98000.00),
('Eva', 1005, 'BCA', 70000.00),
('Frank', 1006, 'BBA', 60000.00),
('Grace', 1007, 'MCA', 85000.00),
('Hank', 1008, 'MBA', 95000.00),
('Ivy', 1009, 'BCA', 72000.00),
('Jack', 1010, 'BBA', 63000.00),
('Kate', 1011, 'MCA', 88000.00),
('Luke', 1012, 'MBA', 97000.00),
('Mary', 1013, 'BCA', 76000.00),
('Nick', 1014, 'BBA', 61000.00),
('Olivia', 1015, 'MCA', 87000.00),
('Peter', 1016, 'MBA', 96000.00),
('Queen', 1017, 'BCA', 74000.00),
('Ryan', 1018, 'BBA', 64000.00),
('Sophia', 1019, 'MCA', 86000.00),
('Tom', 1020, 'MBA', 93000.00);


select * from student;
select * from users;
select * from fee_table;
delete from student where rollnumber=1574 or rollnumber=1544;


