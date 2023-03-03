import sys
import psycopg2



def Conectar(host, user, password, database):
    try:
        db = psycopg2.connect(host=host, user=user, password=password, database=database)
        return db
    except:
        print("No se pudo conectar a la base de datos.")
        





def listar_proveedores(db):
    
    
        otro = db.cursor()
        query = "SELECT * FROM proveedor"
        otro.execute(query)
        proveedores = otro.fetchall()
        for r in proveedores:
            print (r)
        otro.close()
   
        


def buscar_sede(db, localidad):
    cursor = db.cursor()
    query = "SELECT nombrecordinador, direccion FROM sede WHERE localidad = %s"
    cursor.execute(query, (localidad,))
    result = cursor.fetchone()
    if result is not None:
        return result
    else:
        cursor.close()
    return None



def buscar_trajes(db, material):
    cursor = db.cursor()
    query = "SELECT * FROM trajes WHERE material = %s"
    cursor.execute(query, (material,))
    trajes = cursor.fetchall()

    if trajes:
        for traje in trajes:
            query_sede = "SELECT direccion FROM sede WHERE numerodesede = %s"
            cursor.execute(query_sede, (traje[4],))
            sede = cursor.fetchone()[0]

            query_prov = "SELECT nombreproveedor FROM proveedor WHERE cifproveedor = %s"
            cursor.execute(query_prov, (traje[5],))
            proveedor = cursor.fetchone()[0]

            print(f"Código: {traje[0]}")
            print(f"Material: {traje[1]}")
            print(f"Color: {traje[2]}")
            print(f"Diseñador: {traje[3]}")
            print(f"Sede: {sede}")
            print(f"Proveedor: {proveedor}")
            print(f"Temporada: {traje[6]}")
            print("")

    cursor.close()


def insertar_sede(db, numerodesede, nombrecordinador, direccion, localidad):
    cursor = db.cursor()
    query = "INSERT INTO sede (numerodesede, nombrecordinador, direccion, localidad) VALUES (%s, %s, %s, %s)"
    values = (numerodesede, nombrecordinador, direccion, localidad)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    print("Sede insertada correctamente")


def borrar_traje(db, codigo):
    sql=("DELETE FROM trajes WHERE codigotraje = %s")
    cursor = db.cursor()
    try:
        if codigo:
            # Si existe el traje, lo borramos de la base de datos
            cursor.execute(sql,(codigo,))
            db.commit()
            print(f"Se eliminó el traje con código {codigo}")
        else:
            print(f"No se encontró ningún traje con código {codigo}")
    except psycopg2.Error as error:
        print(f"Error al borrar el traje: {error}")
        db.rollback()
    cursor.close()


def actualizar_sede(db, co, nuevo_coordinador):
    cursor = db.cursor()
    query = "UPDATE sede SET nombrecordinador = %s WHERE numerodesede = %s"
    cursor.execute(query, (nuevo_coordinador, co))
    db.commit()
    print(f"Se actualizó la información de la sede en {co}")


def cerrar_conexion(db):
    db.close()
    print("Conexión cerrada correctamente")


