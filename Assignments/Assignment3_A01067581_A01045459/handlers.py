import asyncio
import datetime
from abc import ABC, abstractmethod
import aiohttp

from pokemon import Pokemon, PokemonStats, PokemonAbility, PokemonMove
from request_module import Request
from request_module import get_pokemons_data


class BasePokemonHandler(ABC):
    """
    The Base Pokemon Handler
    """
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle_request(self, req: Request):
        pass

    def set_handler(self, handler):
        self.next_handler = handler


class NameHeadHandler(BasePokemonHandler):
    """
    The Name Head Handler
    """
    def handle_request(self, req: Request):
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class MoveHeadHandler(BasePokemonHandler):
    """
    The Move Head Handler
    """
    def handle_request(self, req: Request):
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class AbilityHeadHandler(BasePokemonHandler):
    """
    The Ability Head Handler
    """

    def handle_request(self, req: Request):
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class MoveHandler(BasePokemonHandler):
    """
    The Move Handler, gathering pokedex Move requests
    """
    @staticmethod
    async def process_asyncio_requests(queries):
        url = "https://pokeapi.co/api/v2/move/{}"
        async with aiohttp.ClientSession() as session:
            print("*** Processing your Pokemon Requests ***")
            async_coroutines = [get_pokemons_data(id_, url, session)
                                for id_ in queries.queries_data]
            responses = await asyncio.gather(*async_coroutines)
            poke_list = [PokemonMove(**res, expanded=queries.expanded) for res in responses]
            return poke_list

    def handle_request(self, req: Request):
        loop = asyncio.get_event_loop()
        responses = loop.run_until_complete(self.process_asyncio_requests(req))
        req.pokedex_list = responses
        req.requests_count = len(responses)
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class NameHandler(BasePokemonHandler):
    """
    The Name Handler, gathering pokedex Name requests
    """
    @staticmethod
    async def process_asyncio_requests(queries):
        url = "https://pokeapi.co/api/v2/pokemon/{}"
        async with aiohttp.ClientSession() as session:
            print("*** Processing your Pokemon Requests ***")
            async_coroutines = [get_pokemons_data(id_, url, session)
                                for id_ in queries.queries_data]
            responses = await asyncio.gather(*async_coroutines)
            if queries.expanded:
                moves_list = await MoveHandler().process_asyncio_requests(queries)

                abilities_list = await AbilityHandler().process_asyncio_requests(queries)
                poke_list = [Pokemon(**res, expanded=queries.expanded, expanded_moves=moves_list,
                                     expanded_abilities=abilities_list) for res in responses]
            else:
                poke_list = [Pokemon(**res, expanded=queries.expanded) for res in responses]
            return poke_list

    def handle_request(self, req: Request):
        loop = asyncio.get_event_loop()
        responses = loop.run_until_complete(self.process_asyncio_requests(req))
        req.pokedex_list = responses
        req.requests_count = len(responses)
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class AbilityHandler(BasePokemonHandler):
    """
    The Ability Handler, gathering pokedex ability requests
    """
    @staticmethod
    async def process_asyncio_requests(queries):
        url = "https://pokeapi.co/api/v2/ability/{}"
        async with aiohttp.ClientSession() as session:
            print("*** Processing your Pokemon Requests ***")
            async_coroutines = [get_pokemons_data(id_, url, session)
                                for id_ in queries.queries_data]
            responses = await asyncio.gather(*async_coroutines)
            poke_list = [PokemonAbility(**res, expanded=queries.expanded) for res in responses]
            return poke_list

    def handle_request(self, req: Request):
        loop = asyncio.get_event_loop()
        responses = loop.run_until_complete(self.process_asyncio_requests(req))
        req.pokedex_list = responses
        req.requests_count = len(responses)
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class InputFileHandler(BasePokemonHandler):
    """
    A Handler for input files
    """
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
    """
    A handler for Data inputs
    """
    def handle_request(self, req: Request):
        req.queries_data = req.input_data
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class PrintHandler(BasePokemonHandler):
    """
    A Print handler if there is no output file mentioned
    """
    def handle_request(self, req: Request):
        print("\n----- Printing to Console ----- \n")
        for poke in req.pokedex_list:
            print(poke)
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class WriteHandler(BasePokemonHandler):
    """
    A Write handler responsible for writing onto an output file
    """
    def handle_request(self, req: Request):
        try:
            with open(req.output, 'w', encoding='utf-8') as export_file:
                output = ''
                for object_result in req.pokedex_list:
                    output += str(object_result)
                time_now = datetime.datetime.now().strftime("%d/%m/%y %H:%M")

                export_file.write(f'Timestamp: {time_now}\nNumber Of Requests: {req.requests_count}\n' + output)
            print(f"------ Exported to {req.output} ------")
            if self.next_handler is not None:
                self.next_handler.handle_request(req)
        except FileNotFoundError:
            print("Please provide the correct filename or check if file exists in current directory")
