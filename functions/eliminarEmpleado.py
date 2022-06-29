# Eliminar empleados
# Created By José Peralta (Kronorit)
# Programa de práctica

def eliminarEmpleado(cursor):
    try:
        sentencia = 'DELETE FROM empleados WHERE id_empleado=%s'
        id_empleado = input('Ingrese el ID del empleado que desea eliminar: ')
        datos = (id_empleado,)
        cursor.execute(sentencia, datos)
        if cursor.rowcount != 0:
            print(f'Se ha eliminado al empleado de ID {id_empleado} correctamente')
        else:
            print('No se ha encontrado a este empleado en la lista.')
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
