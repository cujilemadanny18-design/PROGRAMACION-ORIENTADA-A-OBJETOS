from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Restaurante Amazónico")

# Crear productos
p1 = Producto("P001", "Hamburguesa", 5.50)
p2 = Producto("P002", "Gaseosa", 1.25)

# Crear clientes
c1 = Cliente("0102030405", "Juan Pérez")
c2 = Cliente("0912345678", "María López")

# Agregar al sistema
restaurante.agregar_producto(p1)
restaurante.agregar_producto(p2)

restaurante.agregar_cliente(c1)
restaurante.agregar_cliente(c2)

# Mostrar información
print("=== SISTEMA DEL RESTAURANTE ===")
restaurante.mostrar_productos()
restaurante.mostrar_clientes()