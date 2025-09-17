#Para el cumplimiento de DIP (Principio de Inversion de Dependencias) 
#es que las clases de alto nivel no deben depender de las clases de bajo nivel, sino que ambas deben depender de abstracciones.
#Tambien establece que las abstracciones no deben depender de los detalles, sino que los detalles deben depender de las abstracciones.
#En este ejemplo, la clase AltoNivel no depende directamente de la clase BajoNivel, sino que ambas dependen de la abstraccion Interfaz.

from abc import ABC, abstractmethod #Importamos ABC y abstractmethod para crear clases abstractas y metodos abstractos  

class VerificadorOrtografico(ABC): #Creamos una clase abstracta que hereda de ABC

    @abstractmethod     #Definimos un metodo abstracto
    def verificar_palabra(self, palabra): #Definimos el metodo verificar que recibe un parametro palabra
        pass                              #No implementamos nada porque es un metodo abstracto

class Diccionario(VerificadorOrtografico): #Creamos una clase que hereda de la clase abstracta VerificadorOrtografico

    def __init__(self):                             #Definimos el constructor
        self.palabras = {"hola", "mundo", "python"} #Definimos un conjunto de palabras validas

    def verificar_palabra(self, palabra): #Implementamos el metodo verificar_palabra
        return palabra in self.palabras   #Retornamos True si la palabra esta en el conjunto de palabras validas, False en caso contrario 
    
class CorrectorOrtografico: #Creamos una clase de alto nivel que no depende directamente de la clase Diccionario
    def __init__(self, verificador: VerificadorOrtografico): #El constructor recibe un parametro de tipo VerificadorOrtografico
        self.verificador = verificador                       #Asignamos el parametro a un atributo de la clase

    def corregir_texto(self, texto):                        #Definimos un metodo que recibe un parametro texto
        palabras = texto.split()                             #Dividimos el texto en palabras
        palabras_corregidas = []                             #Creamos una lista vacia para almacenar las palabras corregidas
        for palabra in palabras:                             #Iteramos sobre las palabras
            if self.verificador.verificar_palabra(palabra): #Si la palabra es valida segun el verificador
                palabras_corregidas.append(palabra)         #La agregamos a la lista de palabras corregidas
            else:                                          #Si la palabra no es valida
                palabras_corregidas.append(f"*{palabra}*")  #La agregamos a la lista de palabras corregidas con asteriscos
        return " ".join(palabras_corregidas)                #Retornamos el texto corregido uniendo las palabras corregidas con espacios
    
diccionario = Diccionario()                          #Creamos una instancia de la clase Diccionario
corrector = CorrectorOrtografico(diccionario)        #Creamos una instancia de la clase CorrectorOrtografico pasando el diccionario como parametro
texto = "hola mundo python programacion"              #Definimos un texto con una palabra