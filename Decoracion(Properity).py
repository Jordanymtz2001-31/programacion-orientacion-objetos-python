#Decoracion con property, esto sirve mas para seguridad y datos privadps
#La sintaxis es mejor, mas limpia
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo protegido con un guion bajo
        self.__edad = edad      # Atributo protegido con un guion bajo

    @property  #Esto es un getter con decorador
    def nombre(self):
        return self.__nombre

    @nombre.setter #Esto es un setter pero podemos colocarle un nombre
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property  #Esto es un getter
    def edad(self):
        return self.__edad

    @edad.setter #Esto es un setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad
    
    @nombre.deleter #Esto es un delet
    def nombre(self):
        del self.__nombre

persona1 = Persona("Ana", 30) #Metemos los datos a la clase Persona
nombre = persona1.nombre  # Llamada al getter por su nombre del metodo
print(nombre)             # Salida: Ana

persona1.nombre = "Maria" # Llamada al setter
print(persona1.nombre)    # Salida: Maria

edad = persona1.edad      #Metemos el la edad en una variable
print(edad)               #Salida

persona1.edad = 2
print(persona1.edad)      #Salida de edad pero colocamos primero el objeto

del persona1.nombre      #Con del eliminamos el dato, llamando el metodo 
 