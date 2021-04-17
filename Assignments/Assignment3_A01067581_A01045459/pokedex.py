import asyncio

from handlers import NameHeadHandler, MoveHeadHandler, InputFileHandler, NameHandler, InputDataHandler, \
    MoveHandler, AbilityHandler, WriteHandler, PrintHandler, AbilityHeadHandler
from pokemon import PokedexMode
from request_module import Request, setup_request_commandline


class PokeDex:
    """
    A Pokedex class responsible for handling requests
    """

    def __init__(self):
        """
        An initializer for the Pokedex
        """

        self.pokemon_name_handler = NameHeadHandler()
        self.pokemon_ability_handler = AbilityHeadHandler()
        self.pokemon_move_handler = MoveHeadHandler()

    def execute_requests(self, req: Request):
        """
        Executes the request by calling the appropriate handler for each of
        the command line inputs.
        :param req: a request object
        :return: A Request object
        """

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
        current_handler.set_handler(next_handler)

        return head_mapper[req.pokedex_mode].handle_request(req)


def main(req: Request):
    PokeDex().execute_requests(req)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)





