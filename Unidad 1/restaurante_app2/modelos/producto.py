# Clase que representa un producto del restaurante

class Producto:
    def __init__(self, nombre: str, cantidad: int, precio: float, activo: bool):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.activo = activo

    def mostrar_informacion(self):
        print(self)

    def __str__(self):
        estado = "Disponible" if self.activo else "No disponible"
        return (
            f"Producto: {self.nombre}\n"
            f"Cantidad: {self.cantidad}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Estado: {estado}"
        )