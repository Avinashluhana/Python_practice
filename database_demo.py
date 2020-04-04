import mysql.connector

mycon = mysql.connector.connect(host="localhost",user="root",passwd="root",database="python_prac")
mycursor = mycon.cursor()
mycursor.execute("select * from student")
result = mycursor.fetchall()

for i in result:
    print(i)


