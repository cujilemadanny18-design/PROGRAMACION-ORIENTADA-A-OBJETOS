import tkinter as tk
from tkinter import ttk, messagebox


class MainView:
    def __init__(self, root, servicio, usuario):
        self.root = root
        self.servicio = servicio
        self.usuario = usuario

        self.root.title("Restaurante App - Panel principal")
        self.root.geometry("1050x680")
        self.root.minsize(900, 600)

        self.estilo = ttk.Style()
        try:
            self.estilo.theme_use("clam")
        except tk.TclError:
            pass

        self.crear_interfaz()

    def crear_interfaz(self):
        principal = ttk.Frame(self.root, padding=12)
        principal.pack(fill="both", expand=True)

        encabezado = ttk.Frame(principal)
        encabezado.pack(fill="x", pady=(0, 12))

        ttk.Label(
            encabezado, text="RESTAURANTE APP",
            font=("Arial", 21, "bold")
        ).pack(side="left")

        ttk.Label(
            encabezado,
            text=f"Sesión: {self.usuario.get('nombre', self.usuario.get('usuario', ''))}"
        ).pack(side="right")

        cuerpo = ttk.Frame(principal)
        cuerpo.pack(fill="both", expand=True)

        self.navegacion = ttk.LabelFrame(cuerpo, text="Navegación", padding=10)
        self.navegacion.pack(side="left", fill="y", padx=(0, 12))

        ttk.Button(
            self.navegacion, text="👤 Usuarios",
            command=self.mostrar_usuarios, width=18
        ).pack(fill="x", pady=5)

        ttk.Button(
            self.navegacion, text="🍽 Productos",
            command=self.mostrar_productos, width=18
        ).pack(fill="x", pady=5)

        ttk.Button(
            self.navegacion, text="💰 Ventas",
            command=self.mostrar_ventas, width=18
        ).pack(fill="x", pady=5)

        ttk.Separator(self.navegacion, orient="horizontal").pack(fill="x", pady=10)

        ttk.Button(
            self.navegacion, text="Limpiar vista",
            command=self.limpiar_contenido, width=18
        ).pack(fill="x", pady=5)

        self.contenido = ttk.Frame(cuerpo)
        self.contenido.pack(side="left", fill="both", expand=True)

        self.mostrar_productos()

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    # ---------- Usuarios ----------

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        ttk.Label(
            self.contenido, text="Consulta de usuarios",
            font=("Arial", 17, "bold")
        ).pack(anchor="w", pady=(0, 10))

        ttk.Label(
            self.contenido,
            text="Información disponible desde RestauranteServicio."
        ).pack(anchor="w", pady=(0, 10))

        marco = ttk.LabelFrame(self.contenido, text="Usuarios registrados", padding=10)
        marco.pack(fill="both", expand=True)

        tabla = ttk.Treeview(
            marco, columns=("usuario", "nombre"), show="headings"
        )
        tabla.heading("usuario", text="Usuario")
        tabla.heading("nombre", text="Nombre")
        tabla.column("usuario", width=180)
        tabla.column("nombre", width=350)

        scroll = ttk.Scrollbar(marco, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=scroll.set)

        tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        for usuario in self.servicio.obtener_usuarios():
            tabla.insert("", "end", values=(
                usuario.get("usuario", ""),
                usuario.get("nombre", "")
            ))

    # ---------- Productos ----------

    def mostrar_productos(self):
        self.limpiar_contenido()

        ttk.Label(
            self.contenido, text="Gestión de productos",
            font=("Arial", 17, "bold")
        ).pack(anchor="w", pady=(0, 10))

        formulario = ttk.LabelFrame(
            self.contenido, text="Datos del producto", padding=12
        )
        formulario.pack(fill="x")

        ttk.Label(formulario, text="ID:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.id_entry = ttk.Entry(formulario)
        self.id_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(formulario, text="Nombre:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.nombre_entry = ttk.Entry(formulario)
        self.nombre_entry.grid(row=0, column=3, sticky="ew", padx=5, pady=5)

        ttk.Label(formulario, text="Categoría:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.categoria_entry = ttk.Entry(formulario)
        self.categoria_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(formulario, text="Precio:").grid(row=1, column=2, sticky="w", padx=5, pady=5)
        self.precio_entry = ttk.Entry(formulario)
        self.precio_entry.grid(row=1, column=3, sticky="ew", padx=5, pady=5)

        formulario.columnconfigure(1, weight=1)
        formulario.columnconfigure(3, weight=2)

        acciones = ttk.LabelFrame(
            self.contenido, text="Acciones", padding=8
        )
        acciones.pack(fill="x", pady=10)

        ttk.Button(acciones, text="Registrar", command=self.registrar_producto).pack(side="left", padx=4)
        ttk.Button(acciones, text="Cargar / Consultar", command=self.cargar_producto).pack(side="left", padx=4)
        ttk.Button(acciones, text="Actualizar", command=self.actualizar_producto).pack(side="left", padx=4)
        ttk.Button(acciones, text="Eliminar", command=self.eliminar_producto).pack(side="left", padx=4)
        ttk.Button(acciones, text="Limpiar", command=self.limpiar_formulario).pack(side="left", padx=4)

        marco_tabla = ttk.LabelFrame(
            self.contenido, text="Productos registrados", padding=8
        )
        marco_tabla.pack(fill="both", expand=True)

        self.tabla_productos = ttk.Treeview(
            marco_tabla,
            columns=("id", "nombre", "categoria", "precio"),
            show="headings"
        )

        for columna, titulo, ancho in (
            ("id", "ID", 70),
            ("nombre", "Nombre", 260),
            ("categoria", "Categoría", 180),
            ("precio", "Precio", 100),
        ):
            self.tabla_productos.heading(columna, text=titulo)
            self.tabla_productos.column(columna, width=ancho, anchor="center" if columna in ("id", "precio") else "w")

        scroll = ttk.Scrollbar(
            marco_tabla, orient="vertical", command=self.tabla_productos.yview
        )
        self.tabla_productos.configure(yscrollcommand=scroll.set)

        self.tabla_productos.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.cargar_tabla_productos()

    def registrar_producto(self):
        exito, mensaje = self.servicio.registrar_producto(
            self.nombre_entry.get(),
            self.categoria_entry.get(),
            self.precio_entry.get()
        )
        self.mostrar_resultado(exito, mensaje)
        if exito:
            self.limpiar_formulario()
            self.cargar_tabla_productos()

    def cargar_producto(self):
        id_producto = self.id_entry.get().strip()
        if not id_producto:
            messagebox.showwarning("Dato requerido", "Ingrese el ID del producto.")
            return

        producto = self.servicio.obtener_producto(id_producto)
        if producto is None:
            messagebox.showwarning("Producto", "No se encontró el producto.")
            return

        self._poner_texto(self.nombre_entry, producto.get("nombre", ""))
        self._poner_texto(self.categoria_entry, producto.get("categoria", ""))
        self._poner_texto(self.precio_entry, producto.get("precio", ""))
        messagebox.showinfo("Consulta", "Producto cargado en el formulario.")

    def actualizar_producto(self):
        exito, mensaje = self.servicio.actualizar_producto(
            self.id_entry.get(),
            self.nombre_entry.get(),
            self.categoria_entry.get(),
            self.precio_entry.get()
        )
        self.mostrar_resultado(exito, mensaje)
        if exito:
            self.limpiar_formulario()
            self.cargar_tabla_productos()

    def eliminar_producto(self):
        id_producto = self.id_entry.get().strip()
        if not id_producto:
            messagebox.showwarning("Dato requerido", "Ingrese el ID del producto.")
            return

        if not messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de eliminar este producto?"
        ):
            return

        exito, mensaje = self.servicio.eliminar_producto(id_producto)
        self.mostrar_resultado(exito, mensaje)
        if exito:
            self.limpiar_formulario()
            self.cargar_tabla_productos()

    def cargar_tabla_productos(self):
        if not hasattr(self, "tabla_productos"):
            return

        for elemento in self.tabla_productos.get_children():
            self.tabla_productos.delete(elemento)

        for producto in self.servicio.obtener_productos():
            self.tabla_productos.insert(
                "", "end",
                values=(
                    producto.get("id"),
                    producto.get("nombre"),
                    producto.get("categoria"),
                    f"${float(producto.get('precio', 0)):.2f}"
                )
            )

    def limpiar_formulario(self):
        for entrada in (
            self.id_entry, self.nombre_entry,
            self.categoria_entry, self.precio_entry
        ):
            entrada.delete(0, tk.END)

    @staticmethod
    def _poner_texto(entrada, texto):
        entrada.delete(0, tk.END)
        entrada.insert(0, str(texto))

    @staticmethod
    def mostrar_resultado(exito, mensaje):
        if exito:
            messagebox.showinfo("Operación realizada", mensaje)
        else:
            messagebox.showerror("Error", mensaje)


    # ---------- Ventas: Semana 15 ----------

    def mostrar_ventas(self):
        self.limpiar_contenido()

        ttk.Label(self.contenido, text="Registro de ventas",
                  font=("Arial", 17, "bold")).pack(anchor="w", pady=(0, 5))
        ttk.Label(self.contenido,
                  text="Seleccione un usuario y un producto y registre la venta.",
                  foreground="gray").pack(anchor="w", pady=(0, 10))

        formulario = ttk.LabelFrame(self.contenido, text="Nueva venta", padding=12)
        formulario.pack(fill="x")

        ttk.Label(formulario, text="Usuario:").grid(row=0, column=0, padx=6, pady=8, sticky="w")
        usuarios = self.servicio.obtener_usuarios()
        self.usuarios_map = {
            f"{u.get('usuario','')} - {u.get('nombre','')}": u.get('usuario','')
            for u in usuarios
        }
        self.usuario_combo = ttk.Combobox(
            formulario, values=list(self.usuarios_map), state="readonly", width=38)
        self.usuario_combo.grid(row=0, column=1, padx=6, pady=8, sticky="ew")

        ttk.Label(formulario, text="Producto:").grid(row=1, column=0, padx=6, pady=8, sticky="w")
        productos = self.servicio.obtener_productos()
        self.productos_map = {
            f"{p.get('id')} - {p.get('nombre')} (${float(p.get('precio',0)):.2f})": int(p.get('id'))
            for p in productos
        }
        self.producto_combo = ttk.Combobox(
            formulario, values=list(self.productos_map), state="readonly", width=48)
        self.producto_combo.grid(row=1, column=1, padx=6, pady=8, sticky="ew")
        formulario.columnconfigure(1, weight=1)

        ttk.Button(
            formulario, text="💰 Registrar venta", command=self.registrar_venta
        ).grid(row=2, column=1, sticky="w", padx=6, pady=10)

        marco = ttk.LabelFrame(self.contenido, text="Ventas registradas", padding=8)
        marco.pack(fill="both", expand=True, pady=12)

        self.tabla_ventas = ttk.Treeview(
            marco, columns=("id","usuario","producto","fecha"), show="headings")
        for col, title, width in (
            ("id","ID",60), ("usuario","Usuario",150),
            ("producto","Producto",300), ("fecha","Fecha",180)):
            self.tabla_ventas.heading(col, text=title)
            self.tabla_ventas.column(col, width=width)
        scroll = ttk.Scrollbar(marco, orient="vertical", command=self.tabla_ventas.yview)
        self.tabla_ventas.configure(yscrollcommand=scroll.set)
        self.tabla_ventas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self.cargar_tabla_ventas()

    def registrar_venta(self):
        # Callback: interfaz -> servicio. El servicio valida y persiste.
        if not self.usuario_combo.get():
            messagebox.showwarning("Venta", "Seleccione un usuario.")
            return
        if not self.producto_combo.get():
            messagebox.showwarning("Venta", "Seleccione un producto.")
            return

        usuario = self.usuarios_map[self.usuario_combo.get()]
        producto_id = self.productos_map[self.producto_combo.get()]
        exito, mensaje = self.servicio.registrar_venta(usuario, producto_id)

        if exito:
            messagebox.showinfo("Venta registrada", mensaje)
            self.cargar_tabla_ventas()
            self.usuario_combo.set("")
            self.producto_combo.set("")
        else:
            messagebox.showerror("Error", mensaje)

    def cargar_tabla_ventas(self):
        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)
        for venta in self.servicio.obtener_ventas():
            self.tabla_ventas.insert(
                "", "end",
                values=(venta.get("id"), venta.get("usuario"),
                        f"{venta.get('producto_id')} - {venta.get('producto_nombre')}",
                        venta.get("fecha"))
            )
