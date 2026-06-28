# Clase que administra los productos y clientes

class Restaurante:

    def __init__(self):
        self.productos = []
        self.clientes = []

    # Agregar producto
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Agregar cliente
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    # Mostrar productos
    def mostrar_productos(self):
        print("\n===== PRODUCTOS =====")

        for producto in self.productos:
            print(producto)
            print("-" * 30)

    # Mostrar clientes
    def mostrar_clientes(self):
        print("\n===== CLIENTES =====")

        for cliente in self.clientes:
            print(cliente)
            print("-" * 30)
