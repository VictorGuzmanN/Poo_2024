import conexionBd

try:
    micursor=conexionBd.conexion.cursor()
    sql="create table clientes(id int primary key auto_increment, nombre varchar(60), direccion varchar(120), tel varchar (10))"

    micursor.execute(sql)
except:
    print("Ocurrio un error, por favor vuelva a intentar")
else:
    print("Se creo la tabla con exito")


