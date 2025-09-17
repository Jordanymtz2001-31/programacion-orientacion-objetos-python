#Decoracion a otra funcion con decoradores
def decorador(funcion):     #Definimos el decorador y le pasamos como parametro la funcion a decorar
    def nueva_funcion():    #Definimos una nueva funcion que  
        print("Antes de la funcion")   #Codigo que se ejecuta antes de la funcion original
        funcion()                      #Llamamos a la funcion original
        print("Despues de la funcion") #Codigo que se ejecuta despues de la funcion original
    return nueva_funcion               #Retornamos la nueva funcion  

@decorador               #Usamos el decorador antes de la definicion de la funcion a decorar
def funcion_a_decorar(): #Definimos la funcion a decorar
    print("Soy el decorador")
funcion_a_decorar()      #Llamamos a la funcion decorada