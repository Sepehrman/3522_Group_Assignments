import argparse
import ast
import asyncio
from enum import Enum
from abc import ABC, abstractmethod
import aiohttp



class PokedexMode(Enum):
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class PokedexObject:
    def __init__(self, name, id):
        self._name = name
        self._id = id


class Pokemon(PokedexObject):
    def __init__(self, name, id, **kwargs):
        super().__init__(name, id)
        self._name = name
        self._id = id
        self._abilities = kwargs['abilities']
        self._height = kwargs['height']
        self._weight = kwargs['weight']
        self._types = kwargs['types']
        self._stats = kwargs['stats']
        self._moves = kwargs['moves']

    def __repr__(self):
        return f"Name: {self._name} \nID: {self._id} \nHeight: {self._height} \n" \
               f"Weight: {self._weight} \nTypes: {self._types} \nStats:" \
               f"\n------\n\n{self._stats} \nAbilities\n-----\n\n{self._abilities}" \
               f"\nMoves: \n-----\n" \
               f"{self._moves}\n "


class PokemonMove(PokedexObject):
    def __init__(self, id: int, name: str, generation: str, accuracy: int, pp: int, power: int, ability_type: str,
                 damage_class: str, effect_short: str):
        super().__init__(name, id)
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
    def __init__(self, name: str, id: int, generation: str, effect: str, effect_short: str, pokemon: list):
        super().__init__(name, id)
        self._generation = generation
        self._effect = effect
        self._effect_short = effect_short
        self._pokemon = pokemon

    def __str__(self):
        return f"Ability(name: {self._name}, id: {self._id}, generation: {self._generation}, effect: {self._effect}," \
               f"effect_short: {self._effect_short}, pokemon: {self._pokemon})"


class PokemonStats(PokedexObject):
    def __init__(self, name: str, id: int, is_battle_only: bool):
        super().__init__(name, id)
        self._is_battle_only = is_battle_only

    def __repr__(self):
        return f"PokemonStats( Name: {self._name}, Id: {self._id}, IsBattleOnly: {self._is_battle_only})"


class Request:

    def __init__(self):
        self.pokedex_mode = None
        self.input_data = None
        self.input_file = None
        self.expanded = None
        self.output = None
        self.queries_data = None

    def __str__(self):
        return f"Request: Mode: {self.pokedex_mode}, InputData: {self.input_data}, InputFile: {self.input_file}, " \
               f"Output: {self.output}, Expanded: {self.expanded}, QueryData = {self.queries_data}"


def setup_request_commandline() -> Request:

    parser = argparse.ArgumentParser()
    # parser.add_argument("mode", help="Should be either ability, move, or pokemon")
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
    print("Response object from aiohttp:\n", response)
    print("Response object type:\n", type(response))
    print("-----")
    json_dict = await response.json()
    pok = Pokemon(**json_dict)
    print(pok)
    # print(json_dict)
    return json_dict


async def process_asyncio_requests(requests: list):
    url = "https://pokeapi.co/api/v2/pokemon/{}"
    async with aiohttp.ClientSession() as session:
        print("***process_requests")
        async_coroutines = [get_pokemons_data(id_, url, session)
                            for id_ in requests]
        responses = await asyncio.gather(*async_coroutines)
        for response in responses:
            print(response)
        return responses


async def process_single_request(id: str):
    url = "https://pokeapi.co/api/v2/pokemon/{}"
    async with aiohttp.ClientSession() as session:
        print("***process_single_request")
        response = await get_pokemons_data(id, url, session)
        print(response)
        return response


class BasePokemonHandler(ABC):

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle_request(self, req: Request):
        pass

    def set_handler(self, handler):
        self.next_handler = handler


class NameHeadHandler(BasePokemonHandler):

    def handle_request(self, req: Request):
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class MoveHeadHandler(BasePokemonHandler):

    def handle_request(self, req: Request):
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class AbilityHeadHandler(BasePokemonHandler):

    def handle_request(self, req: Request):
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class MoveHandler(BasePokemonHandler):
    def handle_request(self, req: Request):
        pass


class NameHandler(BasePokemonHandler):

    def handle_request(self, req: Request):
        pass


class AbilityHandler(BasePokemonHandler):
    def handle_request(self, req: Request):
        pass


class InputFileHandler(BasePokemonHandler):

    def handle_request(self, req: Request):
        try:
            print("Inputfile")
            with open(req.input_file, 'r') as file:
                req.queries_data = [line.strip() for line in file.readlines()]
            if self.next_handler is not None:
                self.next_handler.handle_request(req)
        except FileNotFoundError:
            print("Please check if the file exists in current directory!")


class InputDataHandler(BasePokemonHandler):

    def handle_request(self, req: Request):
        req.queries_data = req.input_data
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class PrintHandler(BasePokemonHandler):

    def handle_request(self, req: Request):
        print(req.queries_data)
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class WriteHandler(BasePokemonHandler):
    def handle_request(self, req: Request):
        print("Writing")

        try:
            with open(req.output, 'w', encoding='utf-8') as export_file:
                export_file.write(str(req.output))
            print(f"Exported to {req.output}")
            if self.next_handler is not None:
                self.next_handler.handle_request(req)
        except FileNotFoundError:
            print("Please provide the correct filename or check if file exists in current directory")




def main(req: Request):
    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(process_asyncio_requests(['24', '25']))
    PokeDex().execute_requests(req)



if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)





