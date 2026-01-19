class Objeto:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def usar(self, personaje):
        print("Este objeto no se puede usar")

class PocionVida(Objeto):
    def __init__(self):
        super().__init__(
            "Poción de vida",
            "Recupera 30 puntos de vida"
        )

    def usar(self, jugador):
        curacion = 30
        jugador.vida = jugador.vida + curacion

        if jugador.vida > jugador.vidamax:
            jugador.vida = jugador.vidamax

        print("Recuperas", curacion, "de vida")

class Bomba(Objeto):
    def __init__(self):
        super().__init__(
            "Bomba",
            "Hace 25 de daño al enemigo"
        )

    def usar(self, jugador, enemigo):
        danio = 25
        enemigo.vida = enemigo.vida - danio

        if enemigo.vida < 0:
            enemigo.vida = 0

        print("La bomba hace", danio, "de daño")
