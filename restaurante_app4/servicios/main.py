
from servicios.restaurante import Restaurante
from restaurante_app4.servicios.modelos.producto import Producto
from restaurante_app4.servicios.modelos.bebida import Bebida
from restaurante_app4.servicios.modelos.cliente import Cliente

def ejecutar_sistema() -> None:
    # Encendemos nuestro cerebro de servicios
    servicio = Restaurante()

    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        print("1. Registrar producto")
        print("2. Registrar bebida")
        print("3. Registrar cliente")
        print("----------------------------------------")
        print("4. Listar productos")
        print("5. Listar clientes")
        print("----------------------------------------")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            print("\n[REGISTRAR PRODUCTO]")
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            try:
                precio = float(input("Precio: "))
                nuevo = Producto(codigo, nombre, categoria, precio)
                servicio.registrar_producto(nuevo)
            except ValueError:
                print("❌ El precio debe ser un número.")

        elif opcion == "2":
            print("\n[REGISTRAR BEBIDA]")
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            try:
                precio = float(input("Precio: "))
                tamano = input("Tamaño (ej: 500ml): ")
                nueva = Bebida(codigo, nombre, "Bebida", precio, tamano)
                servicio.registrar_producto(nueva)
            except ValueError:
                print("❌ El precio debe ser un número.")

        elif opcion == "3":
            print("\n[REGISTRAR CLIENTE]")
            identificacion = input("Identificación: ")
            nombre = input("Nombre completo: ")
            correo = input("Correo: ")
            nuevo_cliente = Cliente(identificacion, nombre, correo)
            servicio.registrar_cliente(nuevo_cliente)

        elif opcion == "4":
            servicio.listar_productos()

        elif opcion == "5":
            servicio.listar_clientes()

        elif opcion == "6":
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    ejecutar_sistema()