



import random


def jugar():
    usuario = input(" Escoge una opcion: ´pi´ para piedra, ´pa´para papel o ´ti´ para tijera.\n ").lower()
    computadora = random.choice(["pi", "pa", "ti"])

    if usuario == computadora:
        return print(" ¡Empate! ")

    if gano_el_jugador(usuario, computadora):
        return " ¡Ganaste! "
    
    return "¡ Perdiste !"

def gano_el_jugador(jugador, oponente):
    #retorna valor true si gana el jugador
    #piedra y gana a tijera (pi > ti)
    # tijera gana a papel ( ti > pa)
    # papel gana a piedra (pa > pi)
    if(( jugador == "pi" and oponente == "ti"
        or jugador == "ti" and oponente == "pa"
        or jugador == "pa" and oponente == "pi"
    )):
        return True
    else:
        return False

print(jugar())