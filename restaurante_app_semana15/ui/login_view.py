import tkinter as tk
from tkinter import ttk, messagebox


class LoginView:
    def __init__(self, root, servicio, al_iniciar_sesion):
        self.root = root
        self.servicio = servicio
        self.al_iniciar_sesion = al_iniciar_sesion

        self.root.title("Restaurante App - Inicio de sesión")
        self.root.geometry("430x330")
        self.root.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):
        contenedor = ttk.Frame(self.root, padding=30)
        contenedor.pack(fill="both", expand=True)

        ttk.Label(
            contenedor, text="RESTAURANTE APP",
            font=("Arial", 22, "bold")
        ).pack(pady=(10, 5))

        ttk.Label(
            contenedor, text="Inicio de sesión",
            font=("Arial", 12)
        ).pack(pady=(0, 20))

        formulario = ttk.LabelFrame(contenedor, text="Credenciales", padding=15)
        formulario.pack(fill="x")

        ttk.Label(formulario, text="Usuario:").grid(row=0, column=0, sticky="w", padx=5, pady=7)
        self.usuario_entry = ttk.Entry(formulario)
        self.usuario_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=7)

        ttk.Label(formulario, text="Contraseña:").grid(row=1, column=0, sticky="w", padx=5, pady=7)
        self.contrasena_entry = ttk.Entry(formulario, show="*")
        self.contrasena_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=7)

        formulario.columnconfigure(1, weight=1)

        ttk.Button(
            contenedor, text="Ingresar", command=self.iniciar_sesion
        ).pack(fill="x", pady=18)

        ttk.Label(
            contenedor, text="Ejemplo: admin / 1234",
            foreground="gray"
        ).pack()

        self.usuario_entry.focus_set()

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get()

        if not usuario or not contrasena:
            messagebox.showwarning("Datos requeridos", "Ingrese usuario y contraseña.")
            return

        datos_usuario = self.servicio.validar_usuario(usuario, contrasena)

        if datos_usuario is None:
            messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos.")
            return

        self.al_iniciar_sesion(datos_usuario)
