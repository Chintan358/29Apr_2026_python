import sqlite3

con = sqlite3.connect("data.db");

con.execute("create table emp(id int primary key, name varchar(20), phone varchar(15))")