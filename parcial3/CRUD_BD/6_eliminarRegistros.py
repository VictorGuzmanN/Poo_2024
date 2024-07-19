from conexionBd import *

try:
    micursor=conexionBd.conexion.cursor()
    sql="delete from clientes where Id='1"

    micursor.execute(sql)
    conexion.commit()

    resultado=micursor.fetchall()

    for fila in resultado:
        print(f"Id:{fila[0]}| Nombre:{fila[1]} | Direccion: {fila[2]}| telefono: {fila[3]}")
    
except:
    print("Ocurrio un error, por favor vuelva a intentar")
else:
    print("Registro eliminado con exito")
    