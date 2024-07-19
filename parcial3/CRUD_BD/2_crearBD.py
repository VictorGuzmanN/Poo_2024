import mysql.connector 
from mysql.connector import Error 

#Forma que enseño el profesor

#Conexion a base de datos mediante una funcion 
def conexion():
    try:
        conexion = mysql.connector.connect(
            host ='localhost',
            user= 'root',
            password='',
            database='bd_python'
        )

        #Crear un objeto de tipo cursor para ejecutar SQL
        cursor = conexion.cursor()
        db_name = input("Ingresa el nombre de la BD: ")
        sql = f'CREATE DATABASE {db_name}'
        cursor.execute(sql)
    

    except Error as e:
        print(f"Error: {e}")
        print(f"Tipo de error: {type(e)._name_}")
        print(f"Ocurrio un error intenta nuevamente...")
    else:
        print("Se creo la base de datos exitosamente")
        sql = "SHOW DATABASES"
        cursor.execute(sql)
        for x in cursor:
            print(x)
    finally:
        cursor.close()
        conexion.close()

