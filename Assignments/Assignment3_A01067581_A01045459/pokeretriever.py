import argparse
import asyncio
from enum import Enum

import aiohttp

from handlers import NameHeadHandler, MoveHeadHandler, InputFileHandler, NameHandler, InputDataHandler, \
    MoveHandler, AbilityHandler, WriteHandler, PrintHandler, AbilityHeadHandler
from request_module import Request


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
                   f"{self.get_moves()}\n\n "


class PokemonMove(PokedexObject):
    def __init__(self, generation: str, accuracy: int, pp: int, power: int, ability_type: str,
                 damage_class: str, effect_short: str, **kwargs):
        super().__init__(**kwargs)
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._ability_type = ability_type
        self._damage_class = damage_class
        self._effect_short = effect_short

    def __repr__(self):
        return f"PokemonName: {self._id}, Name: {self._name}, Generation: {self._generation}, " \
               f"Accuracy: {self._accuracy}, PP: {self._pp}, Power: {self._power}, " \
               f"Ability Type: {self._ability_type}, Damage: {self._damage_class}, Effect Short: {self._effect_short})"


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


def setup_request_commandline() -> Request:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", "-m", help="Should be either ability, move, or pokemon")
    group_args = parser.add_mutually_exclusive_group()
    group_args.add_argument("--inputfile", help="File input needs to be .txt")
    group_args.add_argument("--inputdata", nargs='+', help="Input must be name or id")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("--expanded", default="print",
                        help="The app will expand the queries if this argument is provided."
                             " But will simply print the given data if nothing is given.")

    try:
        args = parser.parse_args()
        requ = Request()
        requ.pokedex_mode = PokedexMode(args.mode)
        requ.input_data = args.inputdata
        requ.input_file = args.inputfile
        requ.output = args.output
        if requ.input_file is not None and ".txt" not in requ.input_file:
            requ.input_file, requ.input_data = None, args.inputfile
        print(requ)
        return requ
    except Exception as e:
        print(f"Error! cannot read arguments. {e}")
        # quit()


class PokeDex:

    def __init__(self):
        self.pokemon_name_handler = NameHeadHandler()
        self.pokemon_ability_handler = AbilityHeadHandler()
        self.pokemon_move_handler = MoveHeadHandler()

    def execute_requests(self, req):

        head_mapper = {PokedexMode.POKEMON: self.pokemon_name_handler,
                       PokedexMode.ABILITY: self.pokemon_ability_handler,
                       PokedexMode.MOVE: self.pokemon_move_handler}
        current_handler = head_mapper.get(req.pokedex_mode)

        # Check for Input File | Data
        if req.input_file is not None:
            next_handler = InputFileHandler()
        else:
            next_handler = InputDataHandler()
        current_handler.set_handler(next_handler)
        current_handler = next_handler

        # Check for Pokedex Mode
        if req.pokedex_mode == PokedexMode.POKEMON:
            next_handler = NameHandler()
        elif req.pokedex_mode == PokedexMode.MOVE:
            next_handler = MoveHandler()
        else:
            next_handler = AbilityHandler()
        current_handler.set_handler(next_handler)
        current_handler = next_handler

        # Check for Output
        if req.output != "print":
            next_handler = WriteHandler()
        else:
            next_handler = PrintHandler()

        # APPARENTLY IT'S NOT WRITTING!
        current_handler.set_handler(next_handler)

        return head_mapper[req.pokedex_mode].handle_request(req)
        # Check for Expanded:


async def get_pokemons_data(id, url, session: aiohttp.ClientSession):
    target_url = url.format(id)
    response = await session.request(method="GET", url=target_url)

    json_dict = await response.json()
    pok = Pokemon(**json_dict)
    print(pok)
    return json_dict


async def process_asyncio_requests(requests: list):
    url = "https://pokeapi.co/api/v2/pokemon/{}"
    async with aiohttp.ClientSession() as session:
        print("*** Processing your Pokemon Requests ***")
        async_coroutines = [get_pokemons_data(id_, url, session)
                            for id_ in requests]
        responses = await asyncio.gather(*async_coroutines)
        poke_list = [Pokemon(**res) for res in responses]
        for poke in poke_list:
            print(poke)


async def process_single_request(id: str):
    url = "https://pokeapi.co/api/v2/pokemon/{}"
    async with aiohttp.ClientSession() as session:
        print("***process_single_request")
        response = await get_pokemons_data(id, url, session)
        print(response)
        return response
