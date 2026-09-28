import os
from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self):
        self.archivo_servicio = ArchivoServicio()
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ruta_productos = os.path.join(base_dir, "datos", "productos.json")
        self.ruta_usuarios = os.path.join(base_dir, "datos", "usuarios.json")
        self.ruta_ventas = os.path.join(base_dir, "datos", "ventas.json")

    # ---------- Usuarios ----------

    def validar_usuario(self, usuario, contrasena):
        for datos in self.archivo_servicio.leer_json(self.ruta_usuarios):
            if datos.get("usuario") == usuario and datos.get("contrasena") == contrasena:
                return datos
        return None

    def obtener_usuarios(self):
        return self.archivo_servicio.leer_json(self.ruta_usuarios)

    # ---------- Productos ----------

    def obtener_productos(self):
        return self.archivo_servicio.leer_json(self.ruta_productos)

    def obtener_producto(self, id_producto):
        try:
            id_producto = int(id_producto)
        except (TypeError, ValueError):
            return None

        for producto in self.obtener_productos():
            if int(producto.get("id", 0)) == id_producto:
                return producto
        return None

    def registrar_producto(self, nombre, categoria, precio):
        nombre = str(nombre).strip()
        categoria = str(categoria).strip()

        if not nombre:
            return False, "El nombre del producto es obligatorio."
        if not categoria:
            return False, "La categoría es obligatoria."

        try:
            precio = float(precio)
        except (TypeError, ValueError):
            return False, "El precio debe ser numérico."

        if precio <= 0:
            return False, "El precio debe ser mayor que cero."

        productos = self.obtener_productos()
        nuevo_id = max((int(p.get("id", 0)) for p in productos), default=0) + 1
        producto = Producto(nuevo_id, nombre, categoria, precio)

        productos.append(producto.to_dict())
        if self.archivo_servicio.guardar_json(self.ruta_productos, productos):
            return True, "Producto registrado correctamente."
        return False, "No se pudo guardar el producto."

    def actualizar_producto(self, id_producto, nombre, categoria, precio):
        try:
            id_producto = int(id_producto)
        except (TypeError, ValueError):
            return False, "El ID debe ser numérico."

        nombre = str(nombre).strip()
        categoria = str(categoria).strip()

        if not nombre:
            return False, "El nombre es obligatorio."
        if not categoria:
            return False, "La categoría es obligatoria."

        try:
            precio = float(precio)
        except (TypeError, ValueError):
            return False, "El precio debe ser numérico."

        if precio <= 0:
            return False, "El precio debe ser mayor que cero."

        productos = self.obtener_productos()
        for producto in productos:
            if int(producto.get("id", 0)) == id_producto:
                producto["nombre"] = nombre
                producto["categoria"] = categoria
                producto["precio"] = precio
                if self.archivo_servicio.guardar_json(self.ruta_productos, productos):
                    return True, "Producto actualizado correctamente."
                return False, "No se pudo guardar el cambio."

        return False, "No se encontró el producto."

    def eliminar_producto(self, id_producto):
        try:
            id_producto = int(id_producto)
        except (TypeError, ValueError):
            return False, "El ID debe ser numérico."

        productos = self.obtener_productos()
        filtrados = [p for p in productos if int(p.get("id", 0)) != id_producto]

        if len(filtrados) == len(productos):
            return False, "No se encontró el producto."

        if self.archivo_servicio.guardar_json(self.ruta_productos, filtrados):
            return True, "Producto eliminado correctamente."
        return False, "No se pudo eliminar el producto."


    # ---------- Ventas: Semana 15 ----------

    def obtener_ventas(self):
        return self.archivo_servicio.leer_json(self.ruta_ventas)

    def registrar_venta(self, usuario, producto_id):
        usuario = str(usuario).strip()
        if not usuario:
            return False, "Debe seleccionar un usuario."
        try:
            producto_id = int(producto_id)
        except (TypeError, ValueError):
            return False, "Debe seleccionar un producto válido."

        if not any(u.get("usuario") == usuario for u in self.obtener_usuarios()):
            return False, "El usuario seleccionado no está registrado."

        producto = self.obtener_producto(producto_id)
        if producto is None:
            return False, "El producto seleccionado no existe."

        ventas = self.obtener_ventas()
        nuevo_id = max((int(v.get("id", 0)) for v in ventas), default=0) + 1
        from modelos.venta import Venta
        venta = Venta(nuevo_id, usuario, producto["id"], producto["nombre"])
        ventas.append(venta.to_dict())

        if self.archivo_servicio.guardar_json(self.ruta_ventas, ventas):
            return True, f"Venta #{nuevo_id} registrada correctamente."
        return False, "No se pudo guardar la venta."
