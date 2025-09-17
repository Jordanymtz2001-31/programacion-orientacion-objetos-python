#Ejercicio 5
#Programa que hace funcion de poder de personajes de un juego

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __str__(self):
        return f"Nombre={self.nombre}, Poder={self.fuerza}), Velocidad={self.velocidad}"
    
    def __add__(self, other_pers):
        new_nombre = self.nombre + other_pers.nombre
        new_poder = round(((self.fuerza + other_pers.fuerza)/2)**1.2) #El round es para redondear el poder a un numero entero
        new_velocidad = round(((self.velocidad + other_pers.velocidad)/2)**1.1)
        return Personaje(new_nombre, new_poder, new_velocidad) #Devolvemos un nuevo objeto de la clase Personaje con las fuciones combinadas
    
goku = Personaje("Goku", 500, 800)
vegeta = Personaje("Vegeta", 800, 750)

gogeta = goku + vegeta #Creamos un nuevo objeto de la clase Personaje con la suma de las funciones
print(gogeta) #Salida: Personaje(nombre=Goku & Vegeta, poder=10466)