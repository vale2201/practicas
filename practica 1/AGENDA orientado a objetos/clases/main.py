from empresa import Empresa
from persona import Persona
from grupo import Grupo
from r_grupo_persona import Gp
from r_empresa_persona import Ep
#agenda completa prueba 1
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="agenda"
)
mycursor = mydb.cursor()
while True:
    print("""
    ***  MENU   ***
-------------------------
    ¿Que desea hacer?

       1- Crear 
       2- Leer
       3- Actualizar
       4- Borrar 
       5- Buscar   
       *- Salir """)
    r = input()
# Crear
    if (r =='1'):
        resp= input("""
            ¿Que desea crear?
            1- persona 
            2- grupo
            3- empresa
            4- relacion persona-grupo
            5- relacion persona-empresa
            """)
        if (resp == '1'):  #persona
            nombre=input("ingresa el nombre:  ")
            apellidos=input("ingresa el apellido:  ")
            telefono= input("ingresa el telefono:  "  )
            perso=Persona(nombre, apellidos, telefono)
            perso.crear(mydb,mycursor)
            
        elif (resp == '2'):  #grupo
            nombre=input("ingresa el nombre del grupo:  ")
            descripcion=input("ingresa la descripcion del grupo:  ")           
            grup=Grupo(nombre, descripcion)
            grup.crear(mydb,mycursor)
        elif (resp == '3'): #empresa
            nombre_empresa=input("ingresa el nombre de la empresa:  ")
            representante=input("ingresa el nombre del representante:  ")
            telefono_empresa=input("ingresa el telefono de la empresa:  ")
            direccion= input("ingresa la direccion de la empresa:  ")         
            empre=Empresa(nombre_empresa,representante,telefono_empresa,direccion)
            empre.crear(mydb,mycursor)   

        elif (resp == '4'): #relacion grupo persona
            ID_Persona=input("indica el ID de contacto:  ")   
            ID_Grupo=input("indica el ID del grupo al que pertenecera el contacto: ") 
            rela=Gp(ID_Persona,ID_Grupo)
            rela.crear(mydb,mycursor)  
           
        elif (resp == '5'): #relacion empresa persona
            ID_Persona=input("indica el ID de contacto:  ")   
            ID_Erupo=input("indica el ID de la empresa a la que pertenecera el contacto: ") 
            relaE=Ep(ID_Persona,ID_Erupo)
            relaE.crear(mydb,mycursor)         
# Leer 
    elif (r== '2'):
        qq= input("""¿Que desea leer?
            1- persona 
            2- grupo
            3- empresa
            4- relacion persona-grupo
            5- relacion persona-empresa
            """)
        if (qq=='1'):
            Persona.leer(mycursor)
        elif (qq=='2'):
            Grupo.leer(mycursor)
        elif (qq=='3'):
            Empresa.leer(mycursor)
        elif (qq=='4'):
            Gp.leer(mycursor)
        elif (qq=='5'):
            Ep.leer(mycursor)
# Actualizar        
    elif (r =='3'):
        resp= input("""
    ¿Que desea actualizar?
       1- persona 
       2- grupo
       3- empresa """)
    
        if (resp == '1'):  #persona
            Persona.leer(mycursor)
            valor=input("ingresa el id al que vas a actulizar:  ")
            ed= input("deseas cambiar el nombre, apellidos o telefono   ")
            campo = ''           

            if (ed=='nombre'):
                campo=input("ingresa el nuevo nombre: ")
            elif (ed=='apellidos'):
                campo=input("ingresa el nuevo apellido:  ")
            elif (ed=='telefono'):
                campo= input("ingresa el nuevo telefono"  )
            #valor=input("ingresa el id al que vas a actulizar:  ")
            personaA=Persona('','', '')
            personaA = personaA.actualizar(mydb,mycursor,ed,campo,valor) 
        
        elif (resp == '2'): #GRUPO
            Grupo.leer(mycursor)
            ed= input("deseas cambiar el nombre o la descripcion?   ")
            campo = ''
            valor = ''
            if (ed=='nombre'):
                campo=input("ingresa el nuevo nombre: ")
            elif (ed=='descripcion'):
                campo= input("ingresa la nueva descripcion:  "  )
            valor=input("ingresa el id al que vas a actulizar:  ")
            personaAg=Grupo('','')
            personaAg = personaAg.actualizar(mydb,mycursor,ed,campo,valor)
            
        elif (resp == '3'): #EMPRESA

            Empresa.leer(mycursor)
            ed= input("deseas cambiar el nombre, direccion, representante o telefono?   ")
            campo = ''
            valor = ''
            
            if (ed=='nombre'):
                campo=input("ingresa el nuevo nombre de la empresa: ")
            elif (ed=='direccion'):
                campo=input("ingresa la nueva direccion:  ")
            elif (ed=='representante'):
                campo= input("ingresa el nombre del nuevo representante:  "  )
            elif (ed=='telefono'):
                campo= input("ingresa el nuevo telefono:  "  )
            valor=input("ingresa el id al que vas a actulizar:  ")
            personaAe=Empresa('','','','')
            personaAe = personaAe.actualizar(mydb,mycursor,ed,campo,valor) 
            
        elif (resp == '4'): #RELACION grupo-PERSONA
            Gp.leer(mycursor)
            ed= input("deseas cambiar el contacto o el grupo?   ")
            campo = ''
            valor = ''
            if (ed=='contacto'):
                campo=input("ingresa el id del contacto: ")
            elif (ed=='grupo'):
                campo= input("ingresa el id del nuevo grupo al que pertenece:  "  )
            valor=input("ingresa el id al que vas a actulizar:  ")
            pers=Grupo('','')
            pers = pers.actualizar(mydb,mycursor,ed,campo,valor)


# Borrar        
    elif (r== '4'):
        ed= input("""
    ¿Que desea borrar?
       1- persona 
       2- grupo
       3- empresa
       """)
        if (ed=='1'):
           Persona.leer(mycursor)
           idb=input("cual es el ID que deseas eliminar?") 
           personab=Persona('','','')
           personab = personab.borrar(mydb,mycursor,ed,idb)
        elif (ed=='2'):
           Grupo.leer(mycursor)
           idb=input("cual es el ID que deseas eliminar?") 
           personaG=Grupo('','')
           personaG = personaG.borrar(mydb,mycursor,ed,idb) 
        elif (ed=='3'):
           Empresa.leer(mycursor)
           idb=input("cual es el ID que deseas eliminar?") 
           personaE=Empresa('','','','')
           personaE = personaE.borrar(mydb,mycursor,ed,idb) 

#buscar 
    elif (r== '5'):
        b=input("desea buscar por nombre del contacto(1), número(2) o empresa?(3) ") 
        if(b =='1'):
            n= input("ingresa el nombre que buscas ")
            personabu=Persona('','','')
            personabu = personabu.buscar(mydb,mycursor,b,n) 

        elif(b =='2'):
            n= input("ingresa el numero que buscas ")
            personabu=Persona('','','')
            personabu = personabu.buscar(mydb,mycursor,b,n)

        elif(b =='3'):
            n= input("ingresa el nombre que buscas ")
            personabb=Empresa('','','','')
            personabb = personabb.buscar(mydb,mycursor,b,n)   
#salir   
    elif ( r == 'salir'):
        print("hasta luego")
        break
    
    else:
        print("intente de nuevo") 
    print("presione cualquier tecla para continuar")
    input()
