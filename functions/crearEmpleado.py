# Crear empleado de empleados
# Created By José Peralta (Kronorit)
# Programa de práctica

def crearEmpleado(cursor):
        while True:
            sentencia = 'INSERT INTO empleados(nombre, apellido, correo, puesto, sueldo) VALUES(%s, %s, %s, %s, %s)'
            datos_empleado = input('Ingrese los datos del empleado divididos por comas(nombre, apellido, correo, puesto, sueldo): ')
            datos = datos_empleado.split(',')
            
            # Validación de datos del empleado completos
            if len(datos) == 5:
                for a in range(5): 
                    datos[a] = datos[a].strip()
                datos = tuple(datos)
                cursor.execute(sentencia, datos)
                sentencia = f"SELECT * FROM empleados WHERE correo='{datos[2]}'"
                cursor.execute(sentencia)
                id = cursor.fetchone()[0]

                print(f'Se ha agregado el empleado {datos[0]} {datos[1]} con ID: {id}\nCorreo: {datos[2]}\nPuesto: {datos[3]}\nSueldo: {datos[4]}')
                break
            else:
                print('Recuerde seguir la estructura de datos para agregar nuevos empleados.')
                continue