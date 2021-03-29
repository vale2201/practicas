#agenda completa prueba 1
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="agenda"
)
mycursor = mydb.cursor()
def personaprint():
    mostp = mycursor.execute("SELECT * FROM persona ")
    myresult = mycursor.fetchall()
    for t in myresult:
      print (t)
def grupoprint():
      mycursor.execute("SELECT * FROM grupo ")
      myresult = mycursor.fetchall()
      for t in myresult:
          print (t)
def empresaprint():         
      mycursor.execute("SELECT * FROM empresa ")
      myresult = mycursor.fetchall()
      for t in myresult:
          print (t)
def gpprint():
      mycursor.execute("SELECT * FROM r_grupo_persona ")
      myresult = mycursor.fetchall()
      for t in myresult:
          print (t)
def epprint():
      mycursor.execute("SELECT * FROM r_empresa_persona ")
      myresult = mycursor.fetchall()
      for t in myresult:
          print (t)
while True:
    print("""
    ***  MENU   ***
-------------------------
    ¿Que desea hacer?

       *- Crear 
       *- Leer
       *- Actualizar
       *- Borrar   
       *- Salir """)
    r = input()

    if (r =='crear'):
        tabla= input("a que tabla desea agregar el contacto?(persona, grupo, empresa).")
        if (tabla == 'persona'):           
            nom=input("ingresa el nombre: ")
            ape=input("ingresa el apellido: ")
            tel=input("ingresa el telefono: ")

            sql = "INSERT INTO persona (nombre, apellidos,telefono) VALUES (%s, %s, %s)"
            val = (nom, ape,int(tel))
            mycursor.execute(sql, val)

            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
 
        elif (tabla == 'grupo'):
       
            gru=input("ingresa a que grupo pertenece: (amigos, familia, trabajo)")
            des=input("ingresa una descripcion: ")
            
            sql = "INSERT INTO grupo (nombre, descripcion) VALUES (%s, %s)"
            val = (gru, des)
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
        elif (tabla == 'empresa'):
        
            nomem=input("ingresa el nombre de la empresa: ")
            direc=input("ingresa la direccion: ")
            rep=input("ingresa el nombre del representante: ")
            telem=input("ingresa el numero de telefono de la empresa: ")
            
            sql = "INSERT INTO empresa (nombre_empresa, direccion, representante, telefono_empresa) VALUES (%s, %s,%s, %s)"
            val = (nomem, direc,rep,telem)
            mycursor.execute(sql, val)
            mydb.commit()

            print(mycursor.rowcount, "record inserted.")

    elif (r== 'leer'):
        f=input("Que tabla te gustaria ver?(persona, grupo, empresa, contacto grupo o contacto empresa) ")
        if (f=='persona'):
          personaprint()            
        elif (f=='grupo'):
          grupoprint()
        elif (f=='empresa'):
          empresaprint()
        elif (f=='contacto grupo'):
          gpprint()
        elif (f=='contacto empresa'):
          epprint()

    elif (r =='actualizar'):
        print ("En que tabla desea realizar cambios?(persona, grupo, empresa, contacto grupo o contacto empresa)")
        e=input()
        #actualizar la persona atraves de ID            
        if (e=='persona'):
            personaprint()
            ed= input("deseas cambiar el nombre, apellidos o telefono   ")
            if (ed=='nombre'):
                print ("ingresa el nuevo nombre de la persona. \nIngresa el nombre y despues el id en el cual modificaras la informacion")
                sql = "UPDATE persona SET nombre = %s WHERE id = %s"
                val = (input(), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
            elif (ed=='apellidos'):
                print ("ingresa los nuevos apellidos de la persona. \nIngresa el apellido y despues el id en el cual modificaras la informacion")
                sql = "UPDATE persona SET apellidos = %s WHERE id = %s"
                val = (input(), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
            elif (ed=='telefono'):
                print ("ingresa el nuevo numero de telefono de la persona. \nIngresa el telefono y despues el id en el cual modificaras la informacion")
                sql = "UPDATE persona SET telefono = %s WHERE id = %s"
                val = (input(), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected") 
        #actualizar grupo atraves de ID
        elif (e=='grupo'):
            grupoprint()
            ed= input("deseas cambiar el nombre o la descripcion del grupo?")
            if (ed=='nombre'):
                print ("ingresa el nuevo nombre del grupo")
                sql = "UPDATE grupo SET nombre = %s WHERE id = %s"
                val = (input(), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
            elif (ed=='descripcion'):
                print ("ingresa la nueva descripcion del grupo. \nIngresa la informacion y despues el id en el cual modificaras la descripcion.")
                sql = "UPDATE grupo SET descripcion = %s WHERE id = %s"
                val = (input(), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
        #actualizar la empresa atraves de ID
        elif (e=='empresa'):
            empresaprint()
            ed= input("deseas cambiar el nombre,direccion, representante o telefono   ")
            if (ed=='nombre'):
                print ("ingresa el nuevo nombre de la empresa. \nIngresa el nombre y despues el id en el cual modificaras la informacion")
                sql = "UPDATE empresa SET nombre_empresa = %s WHERE id = %s"
                val = (input(), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
            elif (ed=='direccion'):
                print ("ingresa la nueva direccion de la empresa. \nIngresa la direccion y despues el id en el cual modificaras la informacion")
                sql = "UPDATE empresa SET direccion = %s WHERE id = %s"
                val = (input(), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
            elif (ed=='representante'):
                print ("ingresa el nuevo nombre de representante de la empresa. \nIngresa el nombre de represntante y despues el id en el cual modificaras la informacion")
                sql = "UPDATE empresa SET representante = %s WHERE id = %s"
                val = (input(), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
            elif (ed=='telefono'):
                print ("ingresa el nuevo numero de telefono de la empresa. \nIngresa el telefono y despues el id en el cual modificaras la informacion")
                sql = "UPDATE empresa SET telefono_empresa = %s WHERE id = %s"
                val = (input(), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
        #actualizar la relacion grupo persona
        elif (e=='contacto grupo'):
            print("edtar relacion grupo-persona")
            gpprint()
            ed= input("deseas cambiar el contacto o el grupo ?")
            if (ed=='contacto'):
                print ("ingresa el nuevo id del contacto al que se relacionara el grupo.\nIngresa el nombre y despues el id del cual modificaras la informacion.  ")
                sql = "UPDATE r_grupo_persona SET ID_Persona = %s WHERE id = %s"
                val = (int(input()), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
            elif (ed=='grupo'):
                print ("ingresa el id del nuevo nombre del grupo para el contacto. \nIngresa el grupo y despues el id del cual modificaras la informacion.  ")
                sql = "UPDATE r_grupo_persona SET ID_Grupo = %s WHERE id = %s"
                val = (int(input()), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
        #actualizar la relacion empresa persona 
        elif (e=='contacto empresa'):
            print("edtar relacion empresa-persona")
            epprint()
            ed= input("deseas cambiar el contacto o la empresa ?")
            if (ed=='contacto'):
                print ("ingresa el nuevo id del contacto al que se relacionara la empesa.\nIngresa el nombre y despues el id del cual modificaras la informacion.  ")
                sql = "UPDATE r_empresa_persona SET ID_Persona = %s WHERE id = %s"
                val = (int(input()), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
            elif (ed=='empresa'):
                print ("ingresa el id del nuevo nombre de la empresa para el contacto. \nIngresa la empresa y despues el id del cual modificaras la informacion.  ")
                sql = "UPDATE r_empresa_persona SET ID_Empresa = %s WHERE id = %s"
                val = (int(input()), int(input()))
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")

    elif (r== 'borrar'):
        tabla= input("de que tabla desea borrar el contacto?(persona, grupo, empresa).")
        if (tabla == 'persona'):   
            idb=input("cual es el ID que deseas eliminar?") 
            sql = "DELETE FROM persona WHERE id = "+ idb
            val = (int(idb))
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted")
 

        elif (tabla == 'grupo'):
            #mostrar tabla grupo
            grupoprint()

            idb=input("cual es el ID del grupo que deseas eliminar?") 
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
            
        elif (tabla == 'empresa'):
            #mostrar tabla empresa
            empresaprint()
            
            idb=input("cual es el ID de al empresa que deseas eliminar? ") 
            sql="SELECT * FROM r_empresa_persona WHERE ID_Empresa = "+idb
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            cregistros= len(myresult)

            if (cregistros != 0 ):
                #borrar relacion personas-empresa
                                
                sql = "DELETE FROM r_empresa_persona WHERE ID_Empresa ="+ idb
                mycursor.execute(sql)
                mydb.commit()
                sql = "DELETE FROM empresa WHERE id = "+idb
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "record(s) deleted")

    elif ( r == 'salir'):
        print("hasta luego")
        break
    
    else:
        print("intente de nuevo")
    input()