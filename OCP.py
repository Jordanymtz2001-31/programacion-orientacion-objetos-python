#Ejercicio de OCP - Principio de abierto/cerrado
#Las entidades de software (clases, módulos, funciones, etc.) deben estar abiertas para la extensión, pero cerradas para la modificación.
#Esto significa que el comportamiento de una entidad debe poder extenderse sin modificar su código fuente.

class Notificacion:  #Clase base que no se debe modificar
    def __init__(self,usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def enviar(self):  
        raise NotImplementedError("Este metodo debe ser implementado por las subclases") 

#-------------> Apartir de aqui podemos crear nuevas clases que extiendan la funcionalidad de Notificacion sin modificarla <-----------------

class NotificadorEmail(Notificacion): #Metemos la clase principal Notificacion para que herede sus atributos y metodos
    def Notificar(self):
        print(f"Enviamos un Email al  {self.usuario.email}")

class NotificadorSMS(Notificacion): 
    def Notificar(self):
        print(f"Enviamos un SMS al  {self.usuario.SMS}")

class NotificadorWhassap(Notificacion): 
    def Notificar(self):
        print(f"Enviamos un Whassap al  {self.usuario.Whassap}")