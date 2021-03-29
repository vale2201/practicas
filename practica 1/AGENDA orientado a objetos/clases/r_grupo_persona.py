class Gp:

    def __init__(self,ID_Persona,ID_Grupo):
        self.id =id
        self.ID_Persona = ID_Persona
        self.ID_Grupo = ID_Grupo

    def crear(self,mydb,mycursor):
        sql = "INSERT INTO r_grupo_persona (ID_Persona,ID_Grupo) VALUES ('" + self.ID_Persona + "', '"+self.ID_Grupo+"')"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")


    def leer(mycursor):
        gpprint(mycursor)
        #print("si entroo")

    #def actualizar(mycursor):     
      #  gpprint(mycursor)
      #  ed= input("deseas cambiar el contacto o el grupo ?")
      #  if (ed=='contacto'):
            # print ("ingresa el nuevo id del contacto al que se relacionara el grupo.\nIngresa el nombre y despues el id del cual modificaras la informacion.  ")
      #      sql = "UPDATE r_grupo_persona SET ID_Persona = %s WHERE id = %s"
  #          val = (campo, valor)
  #          mycursor.execute(sql,val)
  #          mydb.commit()
  #          print(mycursor.rowcount, "record(s) affected")
  #      elif (ed=='grupo'):
  #          # print ("ingresa el id del nuevo nombre del grupo para el contacto. \nIngresa el grupo y despues el id del cual modificaras la informacion.  ")
  #          sql = "UPDATE r_grupo_persona SET ID_Grupo = %s WHERE id = %s"
  #          val = (campo, valor)
  #          mycursor.execute(sql,val)
  #          mydb.commit()
  #          print(mycursor.rowcount, "record(s) affected")



def gpprint(mycursor):
    mycursor.execute("SELECT GP.id,P.nombre,apellidos,g.nombre,descripcion FROM persona AS P JOIN r_grupo_persona AS GP ON GP.ID_Persona= P.id JOIN grupo AS g on GP.ID_Grupo= g.id")      

    myresult = mycursor.fetchall()
    for t in myresult:
        print (t)

