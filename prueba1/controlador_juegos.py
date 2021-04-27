from bd import obtener_conexion

def obtener_juegos():
    conexion = obtener_conexion()
    juegos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, apellidos, telefono FROM persona")
        juegos = cursor.fetchall()
    conexion.close()
    return juegos





