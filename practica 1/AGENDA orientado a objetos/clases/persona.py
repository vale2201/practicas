class Persona: 

    def __init__(self, nombre, apellidos, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono

    def crear(self,mydb,mycursor):
        sql = "INSERT INTO persona (nombre,apellidos,telefono) VALUES ('" + self.nombre + "', '"+self.apellidos+"','"+self.telefono+"')"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    def leer(mycursor):
        personaprint(mycursor)

    def actualizar (self,mydb,mycursor,ed,campo, valor):
        personaprint(mycursor)
        if (ed=='nombre'):
            sql = "UPDATE persona SET nombre = %s WHERE id = %s"
            val = (campo, valor)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
        elif (ed=='apellidos'):
            sql = "UPDATE persona SET apellidos = %s WHERE id = %s"
            val = (campo, valor)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
        elif (ed=='telefono'):
            sql = "UPDATE persona SET telefono = %s WHERE id = %s"
            val = (campo, valor)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected") 
    
    def borrar (self,mydb,mycursor,ed,idb):
        if (ed == '1'):             
            sql = "DELETE FROM persona WHERE id = "+ idb
            val = (int(idb))
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted")
    def buscar (self,mydb,mycursor,b,n):
        
        if (b=='1'):
            mostp = mycursor.execute("SELECT id,nombre FROM persona WHERE nombre LIKE '%" + n +"%'" )
            myresult = mycursor.fetchall()
            for t in myresult:
                print (t)
        elif (b=='2'):
            mostp = mycursor.execute("SELECT id,telefono FROM persona WHERE telefono LIKE '%" + n +"%'" )
            myresult = mycursor.fetchall()
            for t in myresult:
                print (t)

def personaprint(mycursor):
    mostp = mycursor.execute("SELECT * FROM persona ")
    myresult = mycursor.fetchall()
    for t in myresult:
      print (t)