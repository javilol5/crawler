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

    danho = calcular_danho(enemigo.ataque, jugador.defensa)

    if estado_jugador == "defensa":
        reducido = danho // 2
        jugador.vida = jugador.vida - reducido
        print("Bloqueas parte del ataque y solo recibes", reducido, "de daño")

        contra = reducido // 2
        enemigo.vida = enemigo.vida - contra
        print("Devuelves", contra, "de daño a", enemigo.nombre)
        return

    jugador.vida = jugador.vida - danho
    if jugador.vida < 0:
        jugador.vida = 0
    print(enemigo.nombre, "te hace", danho, "de daño")
