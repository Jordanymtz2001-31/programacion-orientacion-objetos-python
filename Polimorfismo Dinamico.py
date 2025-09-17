# Polimorfismo Dinámico
# El polimorfismo dinámico permite que diferentes clases tengan métodos con el mismo nombre,
# y el método correcto se llama según el objeto que lo invoca en tiempo de ejecución.
class Gato:
    def sonido(self):
        return "Miau"
    
class Perro:
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal): # Función que acepta cualquier objeto con el método sonido
        print(animal.sonido())

gato = Gato()
perro = Perro()
hacer_sonido(gato)  # Salida: Miau
hacer_sonido(perro) # Salida: Guau