# Programa de gestión de bases de datos sobre empleados
# Created By José Peralta (Kronorit)
# Programa de práctica

import psycopg2
from functions.consultarLista import consultarLista
from functions.consultarEmpleado import consultarEmpleado
from functions.crearEmpleado import crearEmpleado
from functions.eliminarEmpleado import eliminarEmpleado
from functions.modificarEmpleado import modificarEmpleado

# Conexión base de datos

mensaje = '''===Manejo de bases de datos===\n
1) Consultar empleado mediante el ID.
2) Crear empleado nuevo.
3) Eliminar un empleado.
4) Modificar un empleado.
5) Consultar lista completa de empleados registrados en la base de datos.\n
Escriba la opción con el número indicado: '''

conexion = psycopg2.connect(
        user='postgres',
        password='admin',
        host='127.0.0.1',
        port='5432',
        database='test_db'    
    )

try:
    with conexion:
        with conexion.cursor() as cursor:
            decision = input(mensaje)

            if decision == '1':
                consultarEmpleado(cursor)
            elif decision == '2':    
                crearEmpleado(cursor)
            elif decision == '3':
                eliminarEmpleado(cursor)
            elif decision == '4':
                modificarEmpleado(cursor)
            elif decision == '5':
                consultarLista(cursor)

except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()