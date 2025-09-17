#Getter y setter
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    # Getter para obtener el nombre
    def get_nombre(self):  
        return self.__nombre

    # Setter para modificar el nombre
    def set_nombre(self, new_nombre): #Colocamos una nueva variable para el nuevo nombre
        self.__nombre = new_nombre 

    # Getter para obtener la edad
    def get_edad(self):
        return self.__edad

    # Setter para modificar la edad
    def set_edad(self, new_edad): #Colocamos una nueva variable para la nueva edad
        if new_edad >= 0:  # Validación simple
            self.__edad = new_edad
        else:
            print("La edad no puede ser negativa.")

# Crear una instancia de Persona
persona1 = Persona("Ana", -1)

nombre = persona1.get_nombre() # Acceso al nombre mediante el getter
edad = persona1.get_edad()     # Acceso a la edad mediante el getter
print(f"Nombre: {nombre}, Edad: {edad}")

print(persona1.get_nombre())  # Acceso al nombre mediante el getter
print(persona1.get_edad())    # Acceso a la edad mediante el getter

persona1.set_nombre("María")  # Modificación del nombre mediante el setter
nombre = persona1.get_nombre()  # Verificación del cambio con el metodo getter
print(nombre)                   #Imprimimos en nuevo nombre