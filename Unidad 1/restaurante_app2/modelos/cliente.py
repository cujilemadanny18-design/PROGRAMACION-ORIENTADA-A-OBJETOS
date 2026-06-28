# Clase que representa un cliente

class Cliente:

    def __init__(self, nombre: str, edad: int, saldo: float, vip: bool):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.vip = vip

    def mostrar_informacion(self):
        print(self)

    def __str__(self):
        tipo = "VIP" if self.vip else "Normal"

        return (
            f"Cliente: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Saldo: ${self.saldo:.2f}\n"
            f"Tipo: {tipo}"
        )
