from abc import ABC, abstractmethod

########### NAME, ID & GENERATION IS THE SAME AMONG A FEW CLASSES USE KWARGS?

class Pokemon(ABC):
    def __init__(self, id: int, name: str, height: int, weight: int, types: list, stats: list[PokemonAbility],
                 moves: list[PokemonMove]):
        self._id = id
        self._name = name
        self._height = height
        self._weight = weight
        self._types = types
        self._stats = stats
        self._moves = moves


class PokemonMove(Pokemon):
    def __init__(self, id: int, name: str, generation: str, accuracy: int, pp: int, power: int, ability_type: str
                 , damage_class: str, effect_short: str):
        self._name = name
        self._id = id
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._ability_type = ability_type
        self._damage_class = damage_class
        self._effect_short = effect_short

    def __repr__(self):
        return f"PokemonMoves( Id: {self._id}, Name: {self._name}, Generation: {self._generation}, " \
               f"Accuracy: {self._accuracy}, PP: {self._pp}, Power: {self._power}, " \
               f"Ability Type: {self._ability_type}, Damage: {self._damage_class}, Effect Short: {self._effect_short})"


class PokemonAbility(Pokemon):
    def __init__(self, name: str, id: int, generation: str, effect: str, effect_short: str, pokemon: list):
        self._name = name
        self._id = id
        self._generation = generation
        self._effect = effect
        self._effect_short = effect_short
        self._pokemon = pokemon

    def __str__(self):
        return f"Ability(name: {self._name}, id: {self._id}, generation: {self._generation}, effect: {self._effect}," \
               f"effect_short: {self._effect_short}, pokemon: {self._pokemon})"

class PokemonStats(Pokemon):
    def __init__(self, name: str, id: int, is_battle_only: bool):
        self._name = name
        self._id = id
        self._is_battle_only = is_battle_only

    def __repr__(self):
        return f"PokemonStats( Name: {self._name}, Id: {self._id}, Is Battle Only: {self._is_battle_only})"


