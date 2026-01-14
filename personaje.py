class Personaje:
    def __init__(self, nombre, vidamax, ataque, defensa):
        self.nombre = nombre
        self.vidamax = vidamax
        self.vida = vidamax
        self.ataque = ataque
        self.defensa = defensa
        self.oro = 100
        self.nivel = 1
        self.experiencia = 0


    def mostrar_stats(self):
        print("Clase:", self.__class__.__name__)
        print("Nombre:", self.nombre)
        print("Vida:", self.vida, "/", self.vidamax)
        print("Ataque:", self.ataque)
        print("Defensa:", self.defensa)
        print("Oro:", self.oro)
        print("Nivel:", self.nivel)
        print("EXP:", self.experiencia, "/", self.experiencia_necesaria())


    def ganar_experiencia(self, cantidad):
        self.experiencia = self.experiencia + cantidad
        print("Has ganado", cantidad, "EXP")

        while self.experiencia >= self.experiencia_necesaria():
            self.subir_nivel()

    def experiencia_necesaria(self):
        return (self.nivel * 10)

    def subir_nivel(self):
        self.experiencia -= self.experiencia_necesaria()
        self.nivel += 1

        self.vidamax += + 10
        self.ataque += 2
        self.defensa += 2
        self.vida = self.vidamax

        print("\n*** ¡SUBES A NIVEL", self.nivel, "! ***")
        print("Vida máxima +10, Ataque +2, Defensa +2\n")
