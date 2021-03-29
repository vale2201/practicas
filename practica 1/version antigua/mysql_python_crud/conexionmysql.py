import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="agenda"
)

mycursor = mydb.cursor()
print ("ingresa el nuevo nombre del grupo")
sql = "UPDATE grupo SET nombre = %s WHERE id = %s"
val = (input(), int(input()))

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
