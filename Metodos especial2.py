#Metodo especial de addición: __add__

class Persona:
    def __init__(self, nombre, edad): #Metodo constructor
        self.nombre = nombre
        self.edad = edad
#---------------------------------------> Primera forma de definir el metodo __add__
 #   def __add__(self, other):  #Metodo especial que define el comportamiento de la suma entre dos objetos
 #       if isinstance(other, Persona): #Verificamos que el otro objeto sea una instancia de Persona
 #           return self.edad + other.edad
 #       return NotImplemented #Si el otro objeto no es una instancia de Persona, devolvemos NotImplemented

#persona1 = Persona("Juan", 30) #Creamos un objeto de la clase Persona
#persona2 = Persona("Ana", 25)  #Creamos otro objeto de la clase Persona 
#print(persona1 + persona2)  #Salida: 55 (suma de las edades)
#Si no definimos el metodo __add__, la salida seria un error de tipo TypeError: unsupported operand type(s) for +: 'Persona' and 'Persona'

#---------------------------------------> Segunda forma de definir el metodo __add__
    
    def __add__(self, other):  #Metodo especial que define el comportamiento de la suma entre dos objetos
        new_nombre = self.edad + other.edad #Concatenamos la edad de las dos personas
        return Persona(self.edad+other.edad, new_nombre) #Devolvemos un nuevo objeto de la clase Persona con la suma de las edades

persona1 = Persona("Juan", 30) #Creamos un objeto de la clase Persona
persona2 = Persona("Ana", 25)  #Creamos otro objeto de la clase Persona 
new_persona=persona1 + persona2 #Creamos un nuevo objeto de la clase Persona con la suma de las edades
print(new_persona.edad)