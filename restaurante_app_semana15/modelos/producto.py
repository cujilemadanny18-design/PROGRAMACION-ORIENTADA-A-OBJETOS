class Producto:
    def __init__(self, id_producto: int, nombre: str, categoria: str, precio: float):
        if int(id_producto) <= 0:
            raise ValueError("El ID debe ser mayor que cero.")
        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")
        if float(precio) <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self.id_producto = int(id_producto)
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = float(precio)

    def to_dict(self) -> dict:
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

    convertir_a_diccionario = to_dict

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Producto":
        return cls(
            int(datos["id"]),
            str(datos["nombre"]),
            str(datos["categoria"]),
            float(datos["precio"])
        )
