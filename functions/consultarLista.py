# Consultar lista completa de empleados
# Created By José Peralta (Kronorit)
# Programa de práctica

def consultarLista(cursor):
    sentencia = 'SELECT * FROM empleados'
    cursor.execute(sentencia)
    for registro in cursor.fetchall():
        print(registro)