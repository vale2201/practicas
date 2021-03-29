class Ep:

    def __init__(self,ID_Persona,ID_Empresa):
        self.id =id
        self.ID_Persona = ID_Persona
        self.ID_Empresa = ID_Empresa

    def crear(self,mydb,mycursor):
        sql = "INSERT INTO r_empresa_persona (ID_Persona,ID_Empresa) VALUES ('" + self.ID_Persona + "', '"+self.ID_Empresa+"')"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
  
    def leer(mycursor):
        epprint(mycursor)
        




def epprint(mycursor):
    mycursor.execute("SELECT EP.id,P.nombre,apellidos,nombre_empresa FROM persona AS P JOIN r_empresa_persona AS EP ON EP.ID_Persona= P.id JOIN empresa AS e on EP.ID_Empresa= e.id")
  #  mycursor.execute("SELECT * FROM r_empresa_persona ")
    myresult = mycursor.fetchall()
    for t in myresult:
        print (t)

