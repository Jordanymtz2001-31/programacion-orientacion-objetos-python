#Cumpliendo LSP (Principio de Sustitucion de Liskov)
#Los objetos de una clase derivada deben poder sustituir a los objetos de la clase base

class Ave:
    pass

class Pinguino(Ave): #Pinguino hereda de Ave
    def comer(self):
        return "Esta Comiendo" #Aqui cumplimos el principio de LSP porque un pinguino puede comer
    
class Aguila(Ave): #Aguila hereda de Ave
    def comer(self):
        return "Esta Comiendo" #Aqui cumplimos el principio de LSP porque un aguila puede comer

class Loro(Ave): #Loro hereda de Ave
    def comer(self):
        return "Esta Comiendo" #Aqui cumplimos el principio de LSP porque un loro puede comer
    
def alimentar(ave = Ave): #Ponemos un parametro por defecto para que no de error
    return ave.comer()    #Pasamos el objeto ave y llamamos al metodo comer

print(alimentar(Pinguino())) #Salida: Esta Comiendo
print(alimentar(Aguila()))   #Salida: Esta Comiendo
print(alimentar(Loro()))     #Salida: Esta Comiendo
#Si pasamos un objeto de la clase Ave, todo funciona correctamente
    