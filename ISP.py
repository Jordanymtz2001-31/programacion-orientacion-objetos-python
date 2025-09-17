#Para el cumplimiento de ISP es dividir las interfaces(subclases grandes) en partes mas pequeñas y especificas para 
# que las clases no dependan de metodos que no usan.
#En si, no hay que depender de todos los metodos de una clase madre, sino de los que realmente se untilizan en el sistema 
#o por cliente, por eso se crean subclases mas especificas.

from abc import ABC, abstractmethod #Importamos ABC y abstractmethod para crear clases abstractas y metodos abstractos

class Trabajador(ABC): #Creamos una clase abstracta que hereda de ABC

    @abstractmethod     #Definimos un metodo abstracto
    def trabajar(self): #Definimos el metodo trabajar
        pass            #No implementamos nada porque es un metodo abstracto

class Comedor(ABC):     #Creamos una clase abstracta mas especifica 

    @abstractmethod     #Definimos un metodo abstracto
    def comer(self):    #Definimos el metodo comer
        pass            #No implementamos nada porque es un metodo abstracto

class Durmiente(ABC):   #Creamos una clase abstracta mas especifica 

    @abstractmethod     #Definimos un metodo abstracto
    def dormir(self):   #Definimos el metodo dormir
        pass            #No implementamos nada porque es un metodo abstracto

class Humano(Trabajador, Comedor, Durmiente): #Creamos una clase que hereda de las 3 clases abstractas por que un humano trabaja, come y duerme
    def trabajar(self):
        return "El humano esta trabajando"
    def comer(self):
        return "El humano esta comiendo"
    def dormir(self):
        return "El humano esta durmiendo"
    
class Robot(Trabajador): #Creamos una clase que hereda solo de la clase Trabajador porque un robot solo trabaja
    def trabajar(self):
        return "El robot esta trabajando"

robot1 = Robot()
print(robot1.trabajar())
humano1 = Humano()
print(f"{humano1.trabajar()}, {humano1.comer()}, {humano1.dormir()}")