class Grupo:

    def __init__(self,nombre,descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def crear (self,mydb,mycursor):
        sql = "INSERT INTO grupo (nombre, descripcion) VALUES ('" + self.nombre + "',' "+self.descripcion+"')"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    
    def leer(mycursor):
        grupoprint(mycursor)

    def actualizar (self,mydb,mycursor,ed,campo, valor):
        
        if (ed=='nombre'):           
            sql = "UPDATE grupo SET nombre = %s WHERE id = %s"
            val = (campo, valor)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
        elif (ed=='descripcion'):
            sql = "UPDATE grupo SET descripcion = %s WHERE id = %s"
            val = (campo, valor)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            

    def borrar (self,mydb,mycursor,ed,idb):
        grupoprint(mycursor)

        # idb=input("cual es el ID del grupo que deseas eliminar?") 
        sql="SELECT * FROM r_grupo_persona WHERE ID_Grupo = "+idb
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        cregistros= len(myresult)

        if (cregistros != 0 ):
            #borrar relacion personas-empresa
                            
            sql = "DELETE FROM r_grupo_persona WHERE ID_Grupo ="+ idb
            mycursor.execute(sql)
            mydb.commit()

            sql = "DELETE FROM grupo WHERE id = " +idb
            val = (int(idb))
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted")
            
            
def grupoprint(mycursor):
    mycursor.execute("SELECT * FROM grupo ")
    myresult = mycursor.fetchall()
    for t in myresult:
        print (t)









    