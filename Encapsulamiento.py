#Encapsulamiento es el mecanismo que restringe el acceso a ciertos componentes de un objeto.
#En Python, se puede lograr mediante el uso de convenciones de nomenclatura para indicar
#la visibilidad de los atributos y métodos.

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular          # Atributo público
        self.__saldo = saldo_inicial    # Atributo muy privado con doble guion bajo y privado con un guion bajo

        def informar_saldo(self):
            print (f"El saldo actual es: ${self.__saldo}")

        def informar_titular(self):
            print (f"El titular de la cuenta es: {self.titular}")

titular1 = CuentaBancaria("Juan Pérez", 1000)
titular1.informar_titular()  # Acceso al atributo público   
titular1.informar_saldo()    # Acceso al método que maneja el atributo privado
# titula1.__saldo  # Esto generará un error porque __saldo es privado