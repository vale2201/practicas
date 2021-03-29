 #borradores
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="agenda"
)

mycursor = mydb.cursor()

print("Que tabla te gustaria ver?(persona o todo) ")
f=input()
if (f=='persona'):
    mycursor.execute("SELECT * FROM persona ")
    myresult = mycursor.fetchall()
    for t in myresult:
        print (t)
