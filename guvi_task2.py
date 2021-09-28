student_name=input("enter student name:")
sub1,sub2,sub3,sub4,sub5=map(int,input("enter marks of subjects : ").split(" "))
print(student_name,sub1,sub2,sub3,sub4,sub5,sep="\n")
total=sub1+sub2+sub3+sub4+sub5
avg=total/5
student_details = open("student_details.txt", "a+")
student_details.write(student_name+","+str(sub1)+","+str(sub2)+","+str(sub3)+","+str(sub4)+","+str(sub5)+","+str(total)+","+str(avg)+"\n")
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1qaz2wsx",
    auth_plugin='mysql_native_password',
    database="guvi_task_26_sep"
)
my_cursor = my_db.cursor()
# to create database
# my_cursor.execute("create database guvi_task_26_sep")


# to create a table of student name, marks ,sum,avg.
my_cursor.execute("create table guvi_assignments(student_name varchar(30),sub1 int,sub2 int,sub3 int,sub4 int,sub5 int,total int,average decimal)")
#sql query
query="""insert into guvi_assignments(student_name,sub1,sub2,sub3,sub4,sub5,total,average) values(%s,%s,%s,%s,%s,%s,%s,%s)"""
data=(student_name,sub1,sub2,sub3,sub4,sub5,total,avg)
my_cursor.execute(query,data)
my_db.commit()
my_cursor.execute("select * from guvi_assignments")

my_result=my_cursor.fetchall()
for i in my_result:
    print(i)
