#Clases y Objetos
#Ejemplo de una clase con sus atributos y metodos, ademas de retornar valores
#Objeto es una instancia de una clase 
class Celular:
    def __init__(self, marca, modelo, color, almacenamiento):
        #Atributos
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.almacenamiento = almacenamiento

    #Metodos, si estos metodos estan fuera de la clase son funciones normales
    def llamar(self, numero):  #Al parecer podermos crear la variable dentro 
        return f"Llamando al {numero} desde el {self.marca}: {self.modelo}"

    def enviar_mensaje(self, numero, mensaje):
        return f"Enviando mensaje a {numero}: {mensaje}"

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Almacenamiento: {self.almacenamiento}GB"
    
#Creacion del objeto
info = Celular(marca= "Apple", modelo="iPhone 13", color="Azul", almacenamiento="130")
print(info.llamar(123456789))
print(info.enviar_mensaje(2331086911, "Hola, ¿cómo estás?"))
print(info.mostrar_info())