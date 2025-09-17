#Metodo especial 1: str

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):  #Metodo especial que devuelve una cadena representativa del objeto
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
persona = Persona("Juan", 30) #Creamos un objeto de la clase Persona
print(persona)  #Salida: Persona(nombre=Juan, edad=30)

#Si no definimos el metodo __str__, la salida seria algo como <__main__.Persona object at 0x7f9b8c8c8c8c>