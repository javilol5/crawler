import random

class Evento:
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def ejecutar(self, jugador):
        pass

class Cofre(Evento):
    def __init__(self):
        super().__init__("Encuentras un cofre misterioso...")

    def ejecutar(self, jugador):
        print(self.descripcion)

        oro = random.randint(10, 30)
        jugador.oro = jugador.oro + oro
        print("Obtienes", oro, "monedas de oro")

class Trampa(Evento):
    def __init__(self):
        super().__init__("¡Has activado una trampa!")

    def ejecutar(self, jugador):
        print(self.descripcion)

        danho = random.randint(5, 15)
        jugador.vida = jugador.vida - danho
        print("Pierdes", danho, "de vida")

class FuenteCurativa(Evento):
    def __init__(self):
        super().__init__("Encuentras una fuente curativa")

    def ejecutar(self, jugador):
        print(self.descripcion)

        cura = random.randint(10, 25)
        jugador.vida = jugador.vida + cura

        if jugador.vida > jugador.vidamax:
            jugador.vida = jugador.vidamax

        print("Recuperas", cura, "de vida")

class CajaPocion(Evento):
    def __init__(self):
        super().__init__("Encuentras una caja misteriosa")

    def ejecutar(self, jugador):
        print(self.descripcion)

        efecto = random.randint(1, 100)
        if efecto <= 40:
            jugador.defensa += 2
            print("Ganas 2 de defensa")
            print("40%")
        if efecto > 40 and efecto <= 70:
            jugador.ataque += 2
            print("Ganas 2 de ataque")
            print("30%")
        if efecto > 70 and efecto <= 90:
            jugador.vidamax += 20
            print("Tu vida maxima aumenta en 20")
            print("20%")
        if efecto > 90 and efecto <= 99:
            jugador.experiencia += 500
            print("Recibes 500 de experiencia")
            print("9%")
        if efecto > 100:
            jugador.vida == jugador.vidamax
            print("Recuperas toda tu vida")
            print("1%")

def evento_aleatorio():
    eventos = [Cofre, Trampa, FuenteCurativa, CajaPocion]

    evento_clase = random.choice(eventos)
    return evento_clase()
