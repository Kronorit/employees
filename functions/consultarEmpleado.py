# Consulta de empleados
# Created By José Peralta (Kronorit)
# Programa de práctica

def consultarEmpleado(cursor):
    try:
        sentencia = 'SELECT * FROM empleados WHERE id_empleado=%s'
        id_empleado = input('Ingrese el ID del empleado del que quiere consultar: ')
        valor = (id_empleado,)
        cursor.execute(sentencia, valor)
        resultado = cursor.fetchone()
        if resultado != None:
            print(resultado) 
        else:
            print('No hay empleado registrado con este ID.')       
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')