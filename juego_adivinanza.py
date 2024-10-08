import random  # libreria para generar numeros al azar


def juego_adivinanza():
    # generar un numero del 1 al 100
    numero_secreto = random.randint(1, 100)  # randint genera numeros enteros
    intentos = 0
    adivinado = False  # se mantiene en false, para que se mantenga el bucle por que se va a preguntar continuamente

    # Primer entrada en consola bienvenida del juego
    print(" ¡Bienvenido al juego de adivinanza de numero! ")
    print(" Debes de adivinar un numero del 1 al 100 ")
    print(" ¡Intenta adivinarlo!")


    while not adivinado:
    # solicitar un numero del 1 al 100
    # se solicita el numero y se almacena en una variable
        adivinanza = input(" Intriduzca un numero del 1 al 100: ")

    # verifica si es un numero ya que el input recibe str(string)
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # lo esta convirtiendo en entero o number
            intentos += 1

            if adivinanza < numero_secreto:
                print(f" El numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero es menor a {adivinanza}")
            else:
                print(f" ¡Felicidades has ganado! El numero {adivinanza} es el secreto y lo has logrado en {intentos} intentoss. " )
        else:
            print(" Por favor introduzca un numero valido entre el 1 al 100 ")

juego_adivinanza()