import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="agenda"
)

mycursor = mydb.cursor()

sql = "UPDATE persona SET nombre = 'valeria' WHERE nombre = 'vale'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")