#El MRO secuencia específica en la que una jerarquía de clases busca un método 
#en las clases. MRO es importante en la herencia múltiple, donde una clase puede
#heredar de múltiples clases padre. Python utiliza el algoritmo C3 Linearization

#AQUI PUEDO VER EL MRO (METHOD RESOLUTION ORDER)
#para determinar el orden en que se buscan los métodos en una jerarquía de clases.
class A:
    def metodo(self):
        print("Método de la clase A")

class B(A):
    def metodo(self):
        print("Método de la clase B")

class C(B):
    def metodo(self):
        print("Método de la clase C")

class D(B, A):
    def metodo(self):
        print("Método de la clase D")

class E(C, B):
    def metodo(self):
        print("Método de la clase E")

d  = E()
d.metodo()
#para determinar el MRO. Puedes ver el MRO de una clase usando el atributo __mro__ o la función mro().
print(E.__mro__)
#El MRO de la clase E es (E, C, B, A, object), lo que significa que cuando llamas a d.metodo(), Python busca el método en el siguiente orden: