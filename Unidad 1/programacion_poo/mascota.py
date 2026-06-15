class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print("Información de la mascota")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")

    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print("Guau Guau")
        elif self.especie.lower() == "gato":
            print("Miau Miau")
        else:
            print("Sonido no definido")