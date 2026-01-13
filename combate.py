import random

def calcular_danho(ataque, defensa):
    danho = ataque - defensa
    if danho < 1:
        danho = 1
    return danho


def turno_jugador(jugador, enemigo):
    print("\nTu turno")
    print("1. Atacar")
    print("2. Defenderse")

    opcion = input("Elige: ")

    if opcion == "1":
        danho = calcular_danho(jugador.ataque, enemigo.defensa)
        enemigo.vida = enemigo.vida - danho
        print("Has hecho", danho, "de daño a", enemigo.nombre)

    elif opcion == "2":
        print("Te defiendes. Reducirás el daño del próximo ataque.")
        return "defensa"

    else:
        print("Opción inválida, pierdes el turno")

    return None


def turno_enemigo(jugador, enemigo, estado_jugador):
    print("\nTurno de", enemigo.nombre)

    danio = calcular_danho(enemigo.ataque, jugador.defensa)

    if estado_jugador == "defensa":
        danio = danio // 2
        print("Tu defensa reduce el daño a", danio)

    jugador.vida = jugador.vida - danio
    print(enemigo.nombre, "te hace", danio, "de daño")
