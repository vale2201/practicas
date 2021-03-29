import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="agenda"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM persona")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)