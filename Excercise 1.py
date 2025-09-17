#Ejercicio UNO

class Alumno:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
 
        #Metodos
    def estudiar(self, años ):
        return f"El estudiante {self.nombre} está estudiando {self.carrera} por {años} años."

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."
    
    def estudiando(self):
        print("Estoy estudiando") 

#Creacion del objeto, pidiendo datos por consola
alumno1 = Alumno(nombre = input("¿Cual es su nombre?"),
                edad = input("¿Que edad tienes?"), 
                carrera = input("¿Que estudias?"))

años = input ("¿Cuantos años estudiaras?")

#Se imprimen los valores mediante los metodos
print(alumno1.nombre) 
print(alumno1.edad) 
print(alumno1.carrera) 

print(alumno1.presentarse()) 
print(alumno1.estudiar(años)) 



#Poner el while(ciclo): si es verdadero siempre podremos meter de nuevo
#otro dato que no sea "estudiar" (Intentos infinitos), hasta que pongasmos la 
#palabra correcta y pueda ejecutarse el metodo estudiar y imprima el print
while True:
    try:
        estudiar = input()  #Nueva variable donde entrara el dato
        if (estudiar.lower() == "estudiar"): #La condicion deve de ser igual = "estudiar"
            alumno1.estudiando()   #Se ejecuta el metodo
    except:
        print("No ha escrito estudiar")
