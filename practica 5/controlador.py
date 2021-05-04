from conexion import obtener_conexion
from conexion import segunda_conexion

def obtener_agen():
    conexion = obtener_conexion()
    agen = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, apellidos, telefono FROM persona")
        agen = cursor.fetchall()
    conexion.close()
    return agen

def obtener_J():
    conexion = segunda_conexion()
    juegos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM juegos")
        juegos = cursor.fetchall()
    conexion.close()
    return juegos
