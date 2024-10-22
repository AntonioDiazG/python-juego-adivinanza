import random # genera numeros al azar


# primer proceso - definicion de una funcion pasando una variable con una lista y utilizando randim choice
# devuelve(retorna) una palabra al azar de la lista antes creada
def obtener_palabra_secreta() -> str : #agregandi ( -> str ) indica que el tipo de dato es un str(string)
    palabras = ["pyhton", "java", "javascript", "css", "tensorflow", "c++", "git"]
    return random.choice(palabras) #choice sirve para elejir un elemento al azar.


def mostrar_pogreso(palabra_secreta, letras_adivinadas):
    adivinado =""

    for letras in palabra_secreta:
        if letras in letras_adivinadas:
            adivinado += letras
        else:
            adivinado += "_"
    return adivinado

# segundo proceso - creacion de funcion en donde se le pase una variable(palabra_secreta) que es en donde se va a
# almcacenar el valor de la variable(obtener _palabra_secreta), despues se agrega un variable con una lista vacia
# que es en donde se van a alojar las palabras que ya se adivinaron, en seguida se agrega un varibale(intentos)
#con la cantidad de tiros pque se pueden realizar y al final una variable(juego_terminado) que va a funcionar como 
# un bucle para que el juego continue
def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    # impresion en consola de bienvenida al juego 
    print("¡ Bienvenido al juego del ahorcado !")
    print(f" Tienes {intentos} intentos para adivinar la palabra secreta ")
    print(mostrar_pogreso(palabra_secreta, letras_adivinadas), "La cantidad de las letras es:", len(palabra_secreta))

    while not juego_terminado and intentos > 0:
        adivinanza = input("introduce una letra: ").lower()
    
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print(" Por favor introducir una letra valida(solo escribir una letra)")
        elif adivinanza in letras_adivinadas:
            print("  Ya has utilizado esa letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)
            if adivinanza in palabra_secreta:
                print(f" Muy bien acertado, la letra{adivinanza}, esta presente en la palabra")
            else:
                intentos -= 1
                print(f" La letra {adivinanza} no esta en la palabra secreta")
                print(f" te quedan {intentos} intentos")
        
        progreso_acutal = mostrar_pogreso(palabra_secreta, letras_adivinadas)
        print(progreso_acutal)

        if "_" not in progreso_acutal:
            juego_terminado = True
            print(f" !FELICIDADES HAS GANADO¡ La palabra completa es: {palabra_secreta}")

    if intentos == 0:
        print(f" Se te han acabado los intentos, la palabra secreta era {palabra_secreta}")

juego_ahorcado()