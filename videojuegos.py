videojuegos = []

plataformas = ("PC", "PS5", "Xbox Series X", "Nintendo switch")

while True:
    print("\n--- MENÚ DE VIDEOJUEGOS ---")
    print("1. Registrar videojuegos")
    print("2. Ver videojuegos")
    print("3. Modificar videojuegos")
    print("4. Eliminar videojuegos")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")
    if opcion == "1":
       
        codigo = int(input("Ingrese el código del videojuego: "))
        nombre = input("Ingrese el nombre del videojuego: ")
        genero = input("Ingrese el género del videojuego: ")

        print("\nPlataformas disponibles:")
        print("1. PC")
        print("1. PS5")
        print("3. Xbox series X")
        print("4. Nintendo Switch")

        plataforma_codigo = int(input("Seleccione el número de la plataforma: "))
        plataforma = plataformas[plataforma_codigo - 1]

        videojuego = {
            "codigo": codigo,
            "nombre": nombre,
            "genero": genero,
            "plataforma": plataforma
            }

        videojuegos.append(videojuego)
        print("Videojuego registrado correctamente.")    
        pass
    elif opcion == "2":
        if len(videojuegos) == 0:
            print("No hay videojuegos registrados.")
        else:
            print("\n---LISTA DE VIDEOJUEGOS ---")
            for v in videojuegos:
                print(f"codigo: {v['codigo']}, Nombre{v['nombre']}, Genero: {v['genero']}, Plataforma: {v['plataforma']}")


        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida.")
        