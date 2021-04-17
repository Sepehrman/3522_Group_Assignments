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

    def set_to_expanded(self):
        self._expanded = True

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
                   f"{self.get_moves()}\nIs Expanded: {self._expanded}\n\n"


class PokemonMove(PokedexObject):
    def __init__(self, generation: str, accuracy: int, pp: int, power: int, type: str,
                 damage_class: str, effect_entries, **kwargs):
        super().__init__(**kwargs)
        self._generation = dict(generation).get('name')
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._ability_type = dict(type).get('name')
        self._damage_class = dict(damage_class).get('name')
        self._effect_short = effect_entries[0]
        self._expanded = False

    def set_to_expanded(self):
        self._expanded = True

    def get_effect_short(self):
        return self._effect_short.get('short_effect')

    def __repr__(self):
        return f"ID: {self._id}\nName: {self._name} \nGeneration: {self._generation} " \
               f"\nAccuracy: {self._accuracy}\nPP: {self._pp} \nPower: {self._power} " \
               f"\nAbility Type: {self._ability_type} \nDamage: {self._damage_class} " \
               f"\nEffect (Short): {self.get_effect_short()}" \
               f"\nIs Expanded: {self._expanded}\n\n"


class PokemonAbility(PokedexObject):
    def __init__(self, generation: str, effect_entries: str, pokemon: list, **kwargs):
        super().__init__(**kwargs)
        self._generation = dict(generation).get('name')
        self._effect = dict(effect_entries[1]).get('effect')
        self._effect_short = dict(effect_entries[1]).get('short_effect')
        self._pokemon = ', '.join(([poke_name.get('pokemon').get('name') for poke_name in pokemon]))
        self._expanded = False

    def set_to_expanded(self):
        self._expanded = True

    def __repr__(self):
        return f"Ability Name: {self._name}\nID: {self._id}\nGeneration: {self._generation} \nEffect: {self._effect}" \
               f"\nEffect (Short): {self._effect_short}\nPokemon: {self._pokemon}\nIs Expanded: {self._expanded}\n\n"


class PokemonStats(PokedexObject):
    def __init__(self, name: str, id: int, is_battle_only: bool):
        super().__init__(name, id)
        self._is_battle_only = is_battle_only

    def __repr__(self):
        return f"Name: {self._name}\nID: {self._id}\nIs Battle Only: {self._is_battle_only}\n\n"
