from clases import Arquero, Guerrero, Mago, Vampiro, Clerigo
from enemigos import enemigo_aleatorio
from combate import turno_jugador, turno_enemigo
from evento import evento_aleatorio
from objetos import Objeto,objeto_aleatorio

def combate(jugador):
    enemigo = enemigo_aleatorio(jugador.nivel)

    print("\n¡Un", enemigo.nombre, "salvaje aparece!")
    enemigo.mostrar()

    estado_jugador = None

    while jugador.vida > 0 and enemigo.vida > 0:
        estado_jugador = turno_jugador(jugador, enemigo)

        if enemigo.vida <= 0:
            print("\nHas derrotado al", enemigo.nombre)
            jugador.ganar_experiencia(enemigo.experiencia)
            break

        turno_enemigo(jugador, enemigo, estado_jugador)

        print("\nEstado actual:")
        print("Tu vida:", jugador.vida, "/", jugador.vidamax)
        print("Vida enemigo:", enemigo.vida)

    if jugador.vida <= 0:
        print("\nHas sido derrotado...")
        print("Aquí termina tu aventura.")
        exit()

    return True

class Botin():
    def __init__(self):
        super().__init__("Encuentras algo tirado en el suelo...")

    def ejecutar(self, jugador):
        print(self.descripcion)

        objeto = objeto_aleatorio()
        jugador.inventario.append(objeto)
        print("Obtienes:", objeto.nombre)


def elegir_clase(nombre):
    print("Elige tu clase:")
    print("1. Arquero")
    print("2. Guerrero")
    print("3. Mago")
    print("4. Vampiro")
    print("5. Clerigo")

    opcion = input("Opción: ")

    if opcion == "1":
        return Arquero(nombre)

    if opcion == "2":
        return Guerrero(nombre)

    if opcion == "3":
        return Mago(nombre)

    if opcion == "4":
        return Vampiro(nombre)

    if opcion == "5":
        return Clerigo(nombre)

    print("Opción incorrecta")
    return None


def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Luchar contra enemigo")
    print("2. Explorar")
    print("3. Ver estadísticas")
    print("0. Salir")
    print()


def main():
    print("=== RPG EN CONSOLA ===")

    nombre = input("Introduce el nombre de tu personaje: ")

    personaje = None
    while personaje is None:
        personaje = elegir_clase(nombre)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            combate(personaje)

        elif opcion == "2":
            evento = evento_aleatorio()
            evento.ejecutar(personaje)

        elif opcion == "3":
            personaje.mostrar_stats()

        elif opcion == "4":
            personaje.inventario.append(objeto_aleatorio())
            print("Obtienes" ,objeto_aleatorio())

        elif opcion == "5":
            usar_objeto(personaje)

        elif opcion == "0":
            print("¡Hasta la próxima aventura!")
            break

        else:
            print("Opción inválida")

def usar_objeto(personaje):
    if len(personaje.inventario) == 0:
        print("Inventario vacío")
        return

    print("\nInventario:")
    for i in range(len(personaje.inventario)):
        objeto = personaje.inventario[i]
        print(i + 1, "-", objeto.nombre)

    opcion = input("Elige objeto (0 para cancelar): ")

    if opcion == "0":
        return

    indice = int(opcion) - 1

    if indice < 0 or indice >= len(personaje.inventario):
        print("Opción inválida")
        return

    objeto = personaje.inventario[indice]
    objeto.usar(personaje)

    personaje.inventario.pop(indice)


if __name__ == "__main__":
    main()

print("Objeto generado:", objeto.__class__.__name__)
