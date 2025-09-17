#SRP - Principio de responsabilidad unica 
#Una clase debe tener una, y solo una, razon para cambiar.
#Programa que calcule cuanto de gasta de gasolida dependiendo de los kilometros recorridos y los litros consumidos

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100 #El tanque empieza con 100 litros de combustible

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad    #Agregamos la cantidad de combustible al tanque

    def consumir_combustible(self, cantidad):
        self.combustible -= cantidad    #Consumimos la cantidad de combustible del tanque 

    def obtener_combustible(self):
        return self.combustible         #Devolvemos la cantidad de combustible del tanque
class Coche:
    def __init__(self,tanque):
        self.tanque = tanque
        self.kilometros_recorridos = 0

    def conducir(self, kilometros):
        if self.tanque.obtener_combustible() >= kilometros / 2: #Lo que recorre de kilometros me quita la mitad de combistible que tiene
            self.kilometros_recorridos += kilometros            #Aumentamos los kilometros recorridos
            self.tanque.consumir_combustible(kilometros / 2)    #Llamamos ak metodo consumir_combustible y le metemos el parametro kilometros / 2
            print("Se ha movido el coche exitosamente")
            print(f"Combustible restante: {self.tanque.obtener_combustible()} litros") #Mostramos el combustible restante
        else:
            print("No hay suficiente combustible para recorrer esa distancia")

    def obtener_kilometros_recorridos(self): #Devolvemos los kilometros recorridos
        return self.kilometros_recorridos
    
tanque = TanqueDeCombustible() #Creamos un objeto de la clase TanqueDeCombustible
auto1  = Coche(tanque) #Creamos un objeto de la clase Coche y le pasamos el objeto tanque

print(auto1.obtener_kilometros_recorridos()) #Salida: 0
auto1.conducir(10)                           #Conducimos el coche 2 kilometros
print(auto1.obtener_kilometros_recorridos()) #Salida: 2
auto1.conducir(20)
print(auto1.obtener_kilometros_recorridos()) 
auto1.conducir(60)
print(auto1.obtener_kilometros_recorridos())