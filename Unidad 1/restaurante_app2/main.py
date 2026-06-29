# Archivo principal

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():

    # Crear servicio principal
    restaurante = Restaurante()

    # Crear productos
    producto1 = Producto("Hamburguesa", 15, 4.50, True)
    producto2 = Producto("Pizza Familiar", 8, 12.99, True)

    # Crear clientes
    cliente1 = Cliente("Danny Cujilema", 18, 25.75, True)
    cliente2 = Cliente("María López", 22, 15.00, False)

    # Agregar productos
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)

    # Agregar clientes
    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)

    # Mostrar información
    restaurante.mostrar_productos()
    restaurante.mostrar_clientes()


if __name__ == "__main__":
    main()