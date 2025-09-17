#Abstraccion es el proceso de ocultar los detalles complejos y mostrar solo la funcionalidad esencial de un objeto.
#En Python, la abstracción se puede lograr mediante el uso de clases y métodos.
#Una clase abstracto es como una plantilla para otras clases. No se puede instanciar una clase abstracta directamente.
#En su lugar, se debe crear una subclase que implemente los métodos abstractos

from abc import ABC, abstractmethod #Importamos ABC y abstractmethod para crear clases abstractas y metodos abstractos

class Persona(ABC):     #Creamos una clase abstracta que hereda de ABC
    @abstractmethod     #Definimos un metodo abstracto
    def __init__(self, nombre, edad, sexo, activad): #Definimos el metodo constructor
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.activad = activad

    @abstractmethod     #Definimos un metodo abstracto
    def hacer_actividad(self): #En Python, todas las clases hijas de una clase abstracta 
        pass                   #deben implementar todos los metodos abstractos de la clase padre

    def presentarse(self):  #Definimos un metodo concreto
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.sexo} y me gusta {self.activad}.")

class Estudiante(Persona): #Creamos una clase que hereda de Persona
    def __init__(self, nombre, edad, sexo, activad): 
        super().__init__(nombre, edad, sexo, activad)

    def hacer_actividad(self):
        print(f"Estou estudiando en:{self.activad} ")

class Trabajador(Persona): #Creamos una clase que hereda de Persona
    def __init__(self, nombre, edad, sexo, activad): 
        super().__init__(nombre, edad, sexo, activad)

    def hacer_actividad(self):
        print(f"Actualemen estoy trabajando de:{self.activad} ")

melany = Estudiante("Melany",22, "Mujer","programa juegos" )
dany = Trabajador("Dany", 25, "hombre", "Programo sistemas")

melany.presentarse()
melany.hacer_actividad()

dany.presentarse()
dany.hacer_actividad()