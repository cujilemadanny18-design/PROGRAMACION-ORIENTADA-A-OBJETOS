
from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self) -> None:
        # Creamos dos listas vacías y privadas (con doble guion bajo) para guardar todo
        self.__productos: List[Producto] = []
        self.__clientes: List[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        # Revisamos si el código ya existe en la lista de productos
        for p in self.__productos:
            if p.codigo == producto.codigo:
                print(f"❌ Error: Ya existe un producto con el código '{producto.codigo}'.")
                return False
        # Si no está repetido, lo guardamos
        self.__productos.append(producto)
        print(f"✅ Producto '{producto.nombre}' registrado con éxito.")
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        # Lo mismo, pero revisando la identificación del cliente
        for c in self.__clientes:
            if c.identificacion == cliente.identificacion:
                print(f"❌ Error: Ya existe un cliente con la identificación '{cliente.identificacion}'.")
                return False
        self.__clientes.append(cliente)
        print(f"✅ Cliente '{cliente.nombre}' registrado con éxito.")
        return True

    def listar_productos(self) -> None:
        if not self.__productos:
            print("⚠️ No hay productos registrados.")
            return
        print("\n--- LISTA DE PRODUCTOS Y BEBIDAS ---")
        # Aquí ocurre la magia: no importa si es comida o bebida, llamamos al mismo método
        for producto in self.__productos:
            print(producto.mostrar_informacion())

    def listar_clientes(self) -> None:
        if not self.__clientes:
            print("⚠️ No hay clientes registrados.")
            return
        print("\n--- LISTA DE CLIENTES ---")
        for cliente in self.__clientes:
            print(cliente.mostrar_informacion())