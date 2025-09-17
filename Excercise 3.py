class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print ( f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."

# Crear una instancia de Persona
persona1 = Estudiante("Luis", 22, "Ingeniería")
print(persona1.estudiar())
Estudiante.saludar(persona1)  # Llamada al método saludar desde la instancia de Estudiante)
persona1.saludar()            # También se puede llamar como persona1.saludar()