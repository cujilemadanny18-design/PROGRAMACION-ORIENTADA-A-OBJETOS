import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


def main():
    root = tk.Tk()
    servicio = RestauranteServicio()

    def mostrar_main(usuario):
        for widget in root.winfo_children():
            widget.destroy()
        MainView(root, servicio, usuario)

    LoginView(root, servicio, mostrar_main)
    root.mainloop()


if __name__ == "__main__":
    main()
