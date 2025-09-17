#Ejercicio TWO

class Alumno:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
 
        #Metodo estudiar 
    def estudiar(self):
        print("Estoy estudiando") 

        #Pidiendo datos por consola 
nombre = input("¿Cual es su nombre?")
edad = input("¿Que edad tienes?")
carrera = input("¿Que estudias?")

#Creacion del objeto, pidiendo datos por consola
alumno1 = Alumno(nombre, edad, carrera)

#Imprimimos los datos en fotma de vertical
print(f"""
      Datos del alumno: \n\n
        Nombre: {alumno1.nombre} \n
        Edad: {alumno1.edad} \n
        Carrera: {alumno1.carrera}\n
      """)

#Poner el while(ciclo): si es verdadero siempre podremos meter de nuevo
#otro dato que no sea "estudiar" (Intentos infinitos), hasta que pongasmos la 
#palabra correcta y pueda ejecutarse el metodo estudiar y imprima el print
while True:
    try:
        estudiar = input()  #Nueva variable donde entrara el dato
        if (estudiar.lower() == "estudiar"): #La condicion deve de ser igual = "estudiar"
            alumno1.estudiar()   #Se ejecuta el metodo
    except:
        print("No ha escrito estudiar")
