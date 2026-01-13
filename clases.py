from personaje import Personaje

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 80, 12, 8)

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 120, 10, 12)

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 60, 16, 6)

class Vampiro(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 150, 6,4)