class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando")

class Empleado:
    def __init__(self, salario, puesto):
        self.salario = salario
        self.puesto = puesto

    def trabajar(self):
        return("Estoy trabajando") #El return sirve para regresar un valor

class Persona_Programador(Persona, Empleado): #Herencia multiple de las clases Persona y Empleado
    def __init__(self, nombre, edad, nacionalidad, salario, puesto, lenguaje):
        Persona.__init__(self, nombre, edad, nacionalidad) #Inicializando el constructor de la clase Persona para heredar sus atributos
        Empleado.__init__(self, salario, puesto) #Inicializando el constructor de la clase Empleado para heredar sus atributos
        self.lenguaje = lenguaje

    def presentarme(self):
        print(f"""
          Datos del empleado: \n
            Nombre: {self.nombre} \n
            Edad: {self.edad} \n
            Nacionalidad: {self.nacionalidad} \n
            Salrio: {self.salario} \n
            Puesto: {self.puesto} \n
            Lenguaje: {self.lenguaje}\n
          """)
        

persona = Persona_Programador("Juan", 30, "Mexicano", 50000, "Desarrollador", "Python")
persona.hablar()
persona.presentarme()