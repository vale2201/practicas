class Empresa:

    def __init__(self,nombre_empresa,direccion,representante, telefono_empresa):
        
        self.nombre_empresa =nombre_empresa
        self.direccion =direccion
        self.representante =representante
        self.telefono_empresa =telefono_empresa


#crear
    def crear (self,mydb,mycursor):
        sql = "INSERT INTO empresa (nombre_empresa,representante,telefono_empresa,direccion) VALUES ('" + self.nombre_empresa + "', '"+self.representante+"','"+self.telefono_empresa+"', '"+self.direccion+"')"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
#leer
    def leer(mycursor):
        empresaprint(mycursor)
# actualizar
    def actualizar (self,mydb,mycursor,ed,campo, valor):
        if (ed=='nombre'):
            sql = "UPDATE empresa SET nombre_empresa = %s WHERE id = %s"
            val = (campo, valor)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
        elif (ed=='direccion'):
            sql = "UPDATE empresa SET direccion = %s WHERE id = %s"
            val = (campo, valor)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
        elif (ed=='representante'):
            sql = "UPDATE empresa SET representante = %s WHERE id = %s"
            val = (campo, valor)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
        elif (ed=='telefono'):
            sql = "UPDATE empresa SET telefono_empresa = %s WHERE id = %s"
            val = (campo, valor)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
#borrar
    def borrar (self,mydb,mycursor,ed,idb):
        empresaprint(mycursor)
        # idb=input("cual es el ID del grupo que deseas eliminar?") 
        sql="SELECT * FROM r_empresa_persona WHERE ID_Empresa = "+idb
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        cregistros= len(myresult)

        if (cregistros != 0 ):
                #borrar relacion personas-empresa
                                
                sql = "DELETE FROM r_empresa_persona WHERE ID_Empresa ="+ idb
                mycursor.execute(sql)
                mydb.commit()

                sql = "DELETE FROM empresa WHERE id = " +idb
                val = (int(idb))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) deleted")

#buscar
    def buscar (self,mydb,mycursor,b,n):
        if (b == '3'):              
            mostp = mycursor.execute("SELECT id,nombre_empresa FROM empresa WHERE nombre_empresa LIKE '%" + n +"%'" )
            myresult = mycursor.fetchall()
            for t in myresult:
                print (t)



def empresaprint(mycursor):
    mycursor.execute("SELECT * FROM empresa ")
    myresult = mycursor.fetchall()
    for t in myresult:
        print (t)