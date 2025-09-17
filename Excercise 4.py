#Clases de animales
class Animal:
    def comer(self):
        print ("El animal está comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print ("Amamantando a su cría")

class Ave(Animal):
    def volar(self):
        print("Vuelando en el cielo")
    
class Murcielago(Mamifero, Ave):
    pass

Animal1 = Murcielago()
Animal1.comer()      # Método heredado de Animal    
Animal1.amamantar()  # Método heredado de Mamifero
Animal1.volar()      # Método heredado de Ave   