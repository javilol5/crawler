import random

class Enemigo:
    def __init__(self, nombre, vida, ataque, defensa, experiencia):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.experiencia = experiencia

    def esta_vivo(self):
        if self.vida > 0:
            return True
        return False

    def mostrar(self):
        print(self.nombre, "- Vida:", self.vida, "Ataque:", self.ataque, "Defensa:", self.defensa)

class Rata(Enemigo):
    def __init__(self):
        super().__init__("Rata", 20, 5, 3, 10)

class Goblin(Enemigo):
    def __init__(self):
        super().__init__("Goblin", 25, 8, 5, 20)

class Orco(Enemigo):
    def __init__(self):
        super().__init__("Orco", 50, 12, 8, 35)

class Esqueleto(Enemigo):
    def __init__(self):
        super().__init__("Esqueleto", 60, 10, 6, 25)

class Dementor(Enemigo):
    def __init__(self):
        super().__init__("Dementor",80,15,9,50)

class Pirata(Enemigo):
    def __init__(self):
        super().__init__("Pirata", 70, 20, 10, 150)

ENEMIGOS_POR_NIVEL = {
    1: [
        (Rata, 80),
        (Goblin, 20)
    ],
    2: [
        (Rata, 50),
        (Goblin, 30),
        (Orco, 20)
    ],
    3: [
        (Goblin, 40),
        (Orco, 40),
        (Esqueleto, 20)
    ],
    4: [
        (Goblin, 20),
        (Orco, 30),
        (Esqueleto, 50)
    ],
    5: [
        (Orco, 30),
        (Esqueleto, 70)
    ],
    6: [
        (Esqueleto, 50),
        (Dementor, 40),
        (Pirata, 10)
    ]
}


def enemigo_aleatorio(nivel):

    if nivel in ENEMIGOS_POR_NIVEL:
        lista = ENEMIGOS_POR_NIVEL[nivel]
    else:
        lista = ENEMIGOS_POR_NIVEL[max(ENEMIGOS_POR_NIVEL)]

    total = 0
    for enemigo in lista:
        total = total + enemigo[1]

    tirada = random.randint(1, total)

    acumulado = 0
    for enemigo in lista:
        acumulado = acumulado + enemigo[1]

        if tirada <= acumulado:
            clase = enemigo[0]
            break

    enemigo = clase()

    # Escalado por nivel
    enemigo.vida = enemigo.vida + (nivel * 5)
    enemigo.ataque = enemigo.ataque + (nivel * 2)
    enemigo.defensa = enemigo.defensa + nivel

    return enemigo
