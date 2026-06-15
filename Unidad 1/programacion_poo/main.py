from mascota import Mascota

# Crear objetos
mascota1 = Mascota("Max", "Perro", 3)
mascota2 = Mascota("Luna", "Gato", 2)

# Mostrar información y sonido de la primera mascota
mascota1.mostrar_informacion()
mascota1.hacer_sonido()

print("\n" + "-" * 30 + "\n")

# Mostrar información y sonido de la segunda mascota
mascota2.mostrar_informacion()
mascota2.hacer_sonido()