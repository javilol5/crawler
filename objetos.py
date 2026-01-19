import random

class Objeto:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def usar(self, personaje):
        print("Este objeto no se puede usar")

    def __str__(self):
        return self.nombre + " " + self.descripcion


class PocionVida(Objeto):
    def __init__(self):
        super().__init__(
            "Poción de vida",
            "Recupera 30 puntos de vida"
        )

    def usar(self, personaje):

        personaje.vida += 30

        if personaje.vida > personaje.vidamax:
            personaje.vida = personaje.vidamax

        print("Recuperas 30 de vida")

class Bomba(Objeto):
    def __init__(self):
        super().__init__(
            "Bomba",
            "Hace 25 de daño al enemigo"
        )

    def usar(self, personaje, enemigo):
        danho = 25
        enemigo.vida -= danho

        if enemigo.vida < 0:
            enemigo.vida = 0

        print("La bomba hace", danho, "de daño")

def objeto_aleatorio():
    tirada = random.randint(1, 100)
    if tirada <= 50:
        return PocionVida()

    else:
        return Bomba()