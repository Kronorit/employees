# Modificar empleados
# Created By José Peralta (Kronorit)
# Programa de práctica

def modificarEmpleado(cursor):
    sentencia = 'SELECT * FROM empleados WHERE id_empleado = %s'
    id_empleado = input('Ingrese el ID del empleado que desea modificar: ')
    cursor.execute(sentencia, (id_empleado,))
    if cursor.fetchone() == None:
        print('Este empleado no existe.')
    else:
        sentencia = 'UPDATE empleados SET nombre=%s, apellido=%s, correo=%s, puesto=%s, sueldo=%s WHERE id_empleado=%s '
        datos = input('Ingrese los nuevos datos del empleado separados por coma(nombre, apellido, correo, puesto, sueldo): ')
        datos = datos.split(',')
        if len(datos) == 5:
            for i in range(5): 
                datos[i] = datos[i].strip()
            datos.append(id_empleado)
            valores = tuple(datos)
            cursor.execute(sentencia, valores)
            print(f'Empleado ID {id_empleado} ha sido modificado correctamente')
        else:
            print('Datos incompletos.')