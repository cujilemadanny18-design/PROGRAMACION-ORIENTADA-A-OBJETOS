
from modelos.producto import Producto

# Al poner (Producto) al lado de Bebida, le decimos que herede todo lo anterior
class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str) -> None:
        # super().__init__ le pasa los datos básicos al molde papá
        super().__init__(codigo, nombre, categoria, precio)
        # Y aquí guardamos lo que es único de la bebida
        self.tamano: str = tamano

    def mostrar_informacion(self) -> str:
        # Reutilizamos el mensaje del papá y le pegamos el tamaño al final (Polimorfismo)
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tamaño: {self.tamano}"