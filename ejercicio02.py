"""Ejercicio 2 (2,5 puntos) Tiempo estimado: 20 minutos.


Se propone una extensión del juego propuesto en el ejercicio 4 en la que, en vez de jugar con un solo tipo de Pokémon, se pueda jugar con 4 tipos de Pokémon diferentes: Tierra, Agua, Aire y Electricidad.


En base a estas especificaciones en este ejercicio se solicita que:


a)    Programe una clase que implemente un Pokémon de Tierra (Earth Pokemon).

·        Este Pokemon va a tener un índice de defensa que va a estar entre 11 y 20.

b)    Programe una clase que implemente un Pokémon de Agua (Water Pokemon).

·        Este Pokemon va a tener un índice de ataque que va a estar entre 11 y 20.

c)     Programe una clase que implemente un Pokémon de Aire (Air Pokemon).

·        Este Pokemon tiene el método fight_defense modificado de tal forma que existe un 50% de posibilidad de que no le afecte un ataque. Este 50% se puede calcular utilizando el módulo random.

d)    Programe una clase que implemente un Pokémon de Electricidad (Electric Pokemon).

·        Este Pokemon tiene el método fight_attack modificado de tal forma que existe un 50% de posibilidad de que su ataque valga el doble de lo originalmente expuesto. Este 50% se puede calcular utilizando el módulo random.


Reutilice tanto código como sea posible del ejercicio 4 para hacer esta extensión del juego.


No es necesario implementar el docString correspondiente a las funciones y métodos desarrollados, aunque se recomienda hacerlo para facilitar la comprensión por parte del estudiante."""

#Codigo

from ejercicio01 import Pokemon
from ejercicio01 import Pokemon(Enum)

class EarthPokemon(Pokemon):
    def __init__(self, id, nombre, arma, salud, ataque, defensa):
        super().__init__(id, nombre, arma, salud, ataque, defensa)
        self.defensa = random.randint(11, 20)

class WaterPokemon(Pokemon):
    def __init__(self, id, nombre, arma, salud, ataque, defensa):
        super().__init__(id, nombre, arma, salud, ataque, defensa)
        self.ataque = random.randint(11, 20)

class AirPokemon(Pokemon):
    def __init__(self, id, nombre, arma, salud, ataque, defensa):
        super().__init__(id, nombre, arma, salud, ataque, defensa)

    def fight_defense(self, int points_of_damage):
        if random.randint(0, 1) == 0:
            return False
        else:
            self.salud = self.salud - (points_of_damage - self.defensa)
            return True

class ElectricPokemon(Pokemon):
    def __init__(self, id, nombre, arma, salud, ataque, defensa):
        super().__init__(id, nombre, arma, salud, ataque, defensa)

    def fight_attack(self):
        if random.randint(0, 1) == 0:
            return self.ataque * 2
        else:
            return self.ataque

