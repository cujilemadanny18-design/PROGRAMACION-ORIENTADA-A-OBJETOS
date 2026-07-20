
class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        # Aquí guardamos las propiedades básicas usando "anotaciones de tipo" (: str, : float)
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def mostrar_informacion(self) -> str:
        # Este método devuelve un texto bonito con los datos del producto
        return f"[{self.categoria.upper()}] Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio:.2f}"