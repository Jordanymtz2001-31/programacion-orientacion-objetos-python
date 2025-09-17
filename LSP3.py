#Cumpliendo con LSP (Principio de Sustitucion de Liskov)

class Aves:
    def comer(self):
        return "El ave esta comiendo"
    def caminar(self):
        return "El ave esta caminando"

class AveVoladora(Aves): #AveVoladora hereda de Aves
    def volar(self):
        return "Esta ave esta volando" 
    
class AveNoVoladora(Aves): #AveNoVoladora hereda de Aves
    def novolar(self):
        return "Eta ave no es voladora" 

class Pinguino(AveNoVoladora): #Pinguino hereda de Aves y AveNoVoladora
    def comer(self):
        return 
    def caminar(self):
        return "El pinguino esta caminando"
    def novolar(self):
        return "El pinguino no puede volar"
    
class Aguila(AveVoladora): #Aguila hereda de Aves y AveVoladora
    def comer(self):
        return "El aguila esta comiendo"
    def caminar(self):
        return "El aguila esta caminando"
    def volar(self):
        return "El aguila esta volando"

def alimentar(ave = Aves): #Ponemos un parametro por defecto para que no de error
    return ave.comer()    #Pasamos el objeto ave y llamamos al metodo comer

pinguino = Pinguino()
print(pinguino.caminar()) 
print(pinguino.comer())
print(pinguino.novolar())

print("-----")

aguila = Aguila()
print(aguila.caminar()) 
print(aguila.comer())
print(aguila.volar())
