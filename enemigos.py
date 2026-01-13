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


def enemigo_aleatorio(nivel):
    enemigos = [Rata, Goblin, Orco]

    enemigo_clase = random.choice(enemigos)
    enemigo = enemigo_clase()

    # Escalado por nivel
    enemigo.vida = enemigo.vida + (nivel * 5)
    enemigo.ataque = enemigo.ataque + (nivel * 2)
    enemigo.defensa = enemigo.defensa + nivel

    return enemigo
