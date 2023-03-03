
from funciones import *
db = Conectar('localhost','postgres','usuario','jose')




salir = False

# Menú
salir = False
while not salir:
    print("1. Listar todos los proveedores")
    print("2. Buscar una sede por localidad")
    print("3. Buscar trajes por material")
    print("4. Insertar una nueva sede")
    print("5. Borrar un traje")
    print("6. actualizar sede ")
    print("0.salir del programa ")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        proveedores = listar_proveedores(db)
        if proveedores:
            for proveedor in proveedores:
                print(proveedor)

     



    
    elif opcion == "2":
        localidad = input("Ingrese la localidad de la sede que desea buscar: ")
        sede = buscar_sede(db, localidad)

        if sede:
            print("Nombre del coordinador:", sede[0])
            print("Dirección:", sede[1])
        else:
            print("No se encontró ninguna sede en la localidad especificada")

    elif opcion == "3":
        material = input("Ingrese el material del traje: ")
        buscar_trajes(db,material)
    
    elif opcion == "4":
        numerodesede = input("Ingrese el número de sede: ")
        nombrecordinador = input("Ingrese el nombre del coordinador de la nueva sede: ")
        direccion = input("Ingrese la dirección de la nueva sede: ")
        localidad = input("Ingrese la localidad de la nueva sede: ")
        insertar_sede(db, numerodesede, nombrecordinador, direccion, localidad)

    elif opcion == "5":
        codigo = input("Ingrese el código del traje que desea borrar: ")
        borrar_traje(db, codigo)
        db.commit()

    elif opcion == "6":
        nuevo_coordinador = input("Ingrese el nombre del nuevo coordinador: ")
        co= int(input("Ingrese el Codigo de la sede que desea actualizar: "))
        actualizar_sede(db,co,nuevo_coordinador)
    elif opcion == "0":
        salir = True
        print("")
        print("¡HASTA PRONTO!")

    else:
        print("Opción inválida. Ingrese un número del 0 al 6.")

