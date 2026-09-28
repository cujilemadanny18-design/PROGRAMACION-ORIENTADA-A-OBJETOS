from datetime import datetime

class Venta:
    def __init__(self, id_venta, usuario, producto_id, producto_nombre, fecha=None):
        self.id_venta = int(id_venta)
        self.usuario = str(usuario).strip()
        self.producto_id = int(producto_id)
        self.producto_nombre = str(producto_nombre).strip()
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {"id": self.id_venta, "usuario": self.usuario,
                "producto_id": self.producto_id, "producto_nombre": self.producto_nombre,
                "fecha": self.fecha}
