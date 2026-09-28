# Restaurante App - Semana 15

Evolución de la aplicación de restaurante de la Semana 14. Se incorporan los fundamentos básicos del manejo de eventos con el flujo:

**acción del usuario → `command=` → callback → RestauranteServicio → persistencia → respuesta visual**

## Nueva funcionalidad: Ventas

La sección Ventas permite seleccionar un usuario existente y un producto existente mediante `ttk.Combobox`. El botón **Registrar venta** utiliza `command=self.registrar_venta`.

El callback obtiene las selecciones y delega la validación y registro a `RestauranteServicio.registrar_venta()`. El servicio guarda la venta en `datos/ventas.json`. Después, la interfaz actualiza el `Treeview` y muestra un mensaje al usuario.

## Estructura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
│   ├── logo_restaurante.svg
│   └── ventas.svg
├── main.py
└── README.md
```

## Funciones conservadas

- Inicio de sesión.
- Consulta de usuarios.
- Registro, consulta, actualización y eliminación de productos.
- Persistencia mediante JSON.

## Eventos básicos

El botón de venta usa `command=` para asociar la acción del usuario con el callback `registrar_venta`. El callback no manipula directamente `ventas.json`: solicita la operación al servicio.

No se utilizan `bind()`, doble clic, eventos de teclado/mouse ni selección reactiva de `Treeview`.

## Recursos visuales

La carpeta `assets/` contiene el logotipo del sistema y un recurso visual para ventas, cumpliendo el requisito de incorporar recursos visuales al proyecto.

## Credenciales de prueba

- Usuario: `admin`
- Contraseña: `1234`
- Usuario: `mesero`
- Contraseña: `1234`

## Ejecución

Desde la carpeta `restaurante_app`:

```bash
python main.py
```

No se requieren librerías externas.

## Prueba de ventas

1. Iniciar sesión.
2. Abrir **Ventas**.
3. Seleccionar usuario.
4. Seleccionar producto.
5. Presionar **Registrar venta**.
6. Verificar el mensaje y la tabla.
7. Revisar `datos/ventas.json`.
8. Cerrar y ejecutar nuevamente para comprobar la persistencia.
