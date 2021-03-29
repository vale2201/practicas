import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="agenda"
)

mycursor = mydb.cursor()

# aqui van las vars
nom=input("ingresa el nombre: ")
ape=input("ingresa el apellido: ")
tel=input("ingresa el telefono: ")

sql = "INSERT INTO persona (nombre, apellidos,telefono) VALUES (%s, %s, %s)"
val = (nom, ape,int(tel))
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")