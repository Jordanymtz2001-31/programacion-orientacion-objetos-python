#Proyecto de analisis de sentimientos

from textblob import TextBlob

class Sentimientos:
    def __init__(self, nombre, color): #Ponemos como parametros nombre
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0m".format(self.color, self.nombre) #Codigo de color para la terminal
                                                                     #{} en estos meteremos los parametros de color y nombre

class AnalizadorDeSentimientos: #Clase que depende en que rango se encontrara el dato de entreda
    def __init__(self, rangos):
        self.rango = rangos
    
    def analizador_sentimientos(self, polaridad):
        for rango, sentimiento in self.rango:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimientos("Muy Negativo", "31")
    
rangos = [
    ((-0.6, -0.3), Sentimientos ("Negativo", "31")),
    ((-0.3, -0.1), Sentimientos ("Algo Negativo", "31")),
    ((-0.1, 0.1), Sentimientos ("Neutral", "33")),
    ((0.1,0.4), Sentimientos ("Algo Positivo", "32")),
    ((0.4,0.9), Sentimientos ("Positivo", "32")),
    ((0.9,1), Sentimientos ("Muy Positivo", "32")),
]

analizador = AnalizadorDeSentimientos(rangos)

while True:
    texto = input("¿Que es lo que piensas? si quieres salir solo escribe salir " )
    if texto.lower() == "salir": #el lower es para salir
        break 
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity
    sentimiento = analizador.analizador_sentimientos(polaridad)
    print(f"Polaridad: {polaridad:.2f} - Sentimiento: {sentimiento}")
