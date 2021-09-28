import mysql.connector
my_db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1qaz2wsx",
    auth_plugin = 'mysql_native_password',
    database="pythontest"
)
my_cursor=my_db.cursor()
#to create database
#my_cursor.execute("create database pythontest")
#to show all the databases
"""
my_cursor.execute("show databases")
for x in my_cursor:
    print(x)
"""
#to create a table
#my_cursor.execute("create table user_table(username varchar(25),password varchar(30))")
#to show tables
users = open("users.txt", "r")
#for i in users:
 #   a,b = i.split()
my_cursor.execute("insert into user_table(username,password) values ('naveensanapala@broad.com','Qwertty@1')")

#for x in my_cursor:
 #   print(x)

#to shoe all rows of table

my_cursor.execute("select * from user_table")
my_result=my_cursor.fetchall()
for i in my_result:
    print(i)

#to fetch one row only
"""my_cursor.execute("select * from actor")
my_result=my_cursor.fetchone()
print(my_result)"""

#cursor.execute("""INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
 #  VALUES ('Mac', 'Mohan', 20, 'M', 2000)""")