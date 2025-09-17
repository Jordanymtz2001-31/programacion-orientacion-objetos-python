#LSP es un principio de diseño de software que establece que los objetos de una clase derivada
#deben poder sustituir a los objetos de la clase base sin alterar el correcto funcionamiento del

class Ave:
    def volar(self):
        return "El ave esta volando"

class Pinguino(Ave): #Pinguino hereda de Ave
    def volar(self):
        return "Los pinguinos no pueden volar" #Aqui rompemos el principio de LSP porque un pinguino no puede volar
    
def hacer_volar(ave = Ave): #Ponemos un parametro por defecto para que no de error
    return ave.volar()
#Si pasamos un objeto de la clase Ave, todo funciona correctamente
ave = Ave()