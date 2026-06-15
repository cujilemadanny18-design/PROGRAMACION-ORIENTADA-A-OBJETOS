# Función para registrar los datos de la mascota
def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")
    color = input("Ingrese el color de la mascota: ")

    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "color": color
    }

    return mascota


# Función para mostrar los datos de la mascota
def mostrar_mascota(mascota):
    print("\n----- INFORMACIÓN DE LA MASCOTA -----")
    print(f"Nombre  : {mascota['nombre']}")
    print(f"Especie : {mascota['especie']}")
    print(f"Edad    : {mascota['edad']}")
    print(f"Color   : {mascota['color']}")


# Programa principal
mascota = registrar_mascota()
mostrar_mascota(mascota)