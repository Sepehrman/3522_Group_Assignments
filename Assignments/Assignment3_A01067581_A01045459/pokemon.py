from enum import Enum


class PokedexMode(Enum):
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class PokedexObject:
    def __init__(self, name, id, **kwargs):
        self._name = name
        self._id = id


class Pokemon(PokedexObject):
    def __init__(self, height, weight, stats, types, abilities, moves, **kwargs):
        super().__init__(**kwargs)
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves
        self._expanded = False

    def get_types(self):
        return ''.join([poke_type.get('type').get('name') for poke_type in self._types])

    def get_stats(self):
        return '\n'.join([str((stat.get('stat').get('name'), stat.get('base_stat'))) for stat in self._stats])

    def get_abilities(self):
        return '\n'.join(tuple([ability.get('ability').get('name') for ability in self._abilities]))

    def get_moves(self):
        return '\n'.join([str(("Move Name: " + move.get('move').get('name'), "Level Acquired: " +
                               str(move.get('version_group_details')[0].get('level_learned_at')))) for move in
                          self._moves])

    def __repr__(self):
        if self._expanded:
            pass
        else:
            return f"Pokemon Name: {self._name} \nID: {self._id} \nHeight: {self._height} \n" \
                   f"Weight: {self._weight} \nTypes: {self.get_types()} \n" \
                   f"\n------\nStats:\n{self.get_stats()} \n\n-----\nAbilities:\n{self.get_abilities()}" \
                   f"\n\n-----\nMoves:\n" \
                   f"{self.get_moves()}\n\n"


class PokemonMove(PokedexObject):
    def __init__(self, generation: str, accuracy: int, pp: int, power: int, type: str,
                 damage_class: str, effect_entries, **kwargs):
        super().__init__(**kwargs)
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._ability_type = type
        self._damage_class = damage_class
        self._effect_short = effect_entries[0]

    def get_generation(self):
        return dict(self._generation).get('name')

    def get_ability_type(self):
        return dict(self._ability_type).get('name')

    def get_damage_class(self):
        return dict(self._damage_class).get('name')

    def get_effect(self):
        return self._effect_short.get('effect')

    def get_effect_short(self):
        return self._effect_short.get('short_effect')

    def __repr__(self):
        return f"ID: {self._id}\nName: {self._name} \nGeneration: {self.get_generation()} " \
               f"\nAccuracy: {self._accuracy}\nPP: {self._pp} \nPower: {self._power} " \
               f"\nAbility Type: {self.get_ability_type()} \nDamage: {self.get_damage_class()} " \
               f"\nEffect: {self.get_effect()}" \
               f"\n\nEffect Short: {self.get_effect_short()}\n\n"


class PokemonAbility(PokedexObject):
    def __init__(self, generation: str, effect: str, effect_short: str, pokemon: list, **kwargs):
        super().__init__(**kwargs)
        self._generation = generation
        self._effect = effect
        self._effect_short = effect_short
        self._pokemon = pokemon

    def __repr__(self):
        return f"Ability(name: {self._name}, id: {self._id}, generation: {self._generation}, effect: {self._effect}," \
               f"effect_short: {self._effect_short}, pokemon: {self._pokemon})"


class PokemonStats(PokedexObject):
    def __init__(self, name: str, id: int, is_battle_only: bool):
        super().__init__(name, id)
        self._is_battle_only = is_battle_only

    def __repr__(self):
        return f"PokemonStats( Name: {self._name}, Id: {self._id}, IsBattleOnly: {self._is_battle_only})"
