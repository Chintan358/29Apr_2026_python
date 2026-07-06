import mysql.connector as sql

con = sql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password="root",
    database = "pythonapp"
)
# print("db connected")
cursor = con.cursor()

# cursor.execute("create database pythonapp")

#create table
# q = "create table student(id int primary key,name varchar(20),email varchar(50))"
# cursor.execute(q)

#add data
# q = "insert into student values(1,'saed','saed@gmail.com')"
# cursor.execute(q)
# con.commit()

# q = "insert into student values(%s,%s,%s)"
# v = (3,"Priya","priya@gmail.com")
# cursor.execute(q,v)
# con.commit()

#update data
# q = "update student set email='priya@yahoo.com' where id=3"
# cursor.execute(q)
# con.commit()

# q = "update student set email=%s where id=%s"
# v = ("saedgajiwala@gmial.com",1)
# cursor.execute(q,v)
# con.commit()

#delete data
# q = "delete from student where id=1"
# cursor.execute(q)
# con.commit()

#view emp
# cursor.execute("select * from student")
# data = cursor.fetchall()
# print(data)