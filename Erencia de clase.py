#Herencias

#Clase padre
class Persona:
    def __init__(self,position, name, surname, age ):
        self.position = position
        self.name = name
        self.surname = surname
        self.age = age

#Clase hijos

class Empleado(Persona):  #Heredando de la clase padre Persona
    def __init__(self,position, name, surname, age, job, salary):
        super().__init__(position,name, surname, age) #el super hereda los atributos de la clase padre
        self.job = job #Atributos propios de la clase hija
        self.salary = salary
        

class Cliente(Persona):  #Heredando de la clase padre Persona
    def __init__(self,position, name, surname, age, email, purchase):
        super().__init__(position, name, surname, age) #el super hereda los atributos de la clase padre
        self.email  = email  #Atributos propios de la clase hija        
        self.purchase = purchase
    
position = input("¿Cual es su posicion? (Empleado/Cliente): ")
name = input("¿Cual es su nombre? : ")  
surname = input("¿Cual es su apellido? : ")
age = input("¿Cual es su edad? : ")         
job = input("¿Cual es su trabajo? : ")
salary = input("¿Cual es su salario? : ")   
email = input("¿Cual es su email? : ")
purchase = input("¿Cual fue su ultima compra? : ")



if position.lower() == "empleado":
    empleado1 = Empleado(position ,name, surname, age, job, salary)
    print(f"""
          Datos del empleado: \n\n
            Nombre: {empleado1.name} \n
            Apellido: {empleado1.surname} \n
            Edad: {empleado1.age} \n
            Trabajo: {empleado1.job} \n
            Salario: {empleado1.salary} \n
          """)
elif position.lower() == "cliente":
    cliente1 = Cliente(position, name, surname, age, email, purchase)
    print(f"""
          Datos del cliente: \n\n
            Nombre: {cliente1.name} \n
            Apellido: {cliente1.surname} \n
            Edad: {cliente1.age} \n
            Email: {cliente1.email} \n
            Ultima compra: {cliente1.purchase} \n
          """)


    