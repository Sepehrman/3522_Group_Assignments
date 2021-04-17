import asyncio
from abc import ABC, abstractmethod
import aiohttp

from pokemon import Pokemon, PokemonStats, PokemonAbility, PokemonMove
from request_module import Request
from request_module import get_pokemons_data

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

    @staticmethod
    async def process_asyncio_requests(queries):
        url = "https://pokeapi.co/api/v2/move/{}"
        async with aiohttp.ClientSession() as session:
            print("*** Processing your Pokemon Requests ***")
            async_coroutines = [get_pokemons_data(id_, url, session)
                                for id_ in queries]
            responses = await asyncio.gather(*async_coroutines)
            poke_list = [PokemonMove(**res) for res in responses]
            return poke_list

    def handle_request(self, req: Request):
        loop = asyncio.get_event_loop()
        responses = loop.run_until_complete(self.process_asyncio_requests(req.queries_data))
        req.pokedex_list = responses
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class NameHandler(BasePokemonHandler):
    @staticmethod
    async def process_asyncio_requests(queries):
        url = "https://pokeapi.co/api/v2/pokemon/{}"
        async with aiohttp.ClientSession() as session:
            print("*** Processing your Pokemon Requests ***")
            async_coroutines = [get_pokemons_data(id_, url, session)
                                for id_ in queries]
            responses = await asyncio.gather(*async_coroutines)
            poke_list = [Pokemon(**res) for res in responses]
            return poke_list

    def handle_request(self, req: Request):
        loop = asyncio.get_event_loop()
        responses = loop.run_until_complete(self.process_asyncio_requests(req.queries_data))
        req.pokedex_list = responses
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class AbilityHandler(BasePokemonHandler):

    @staticmethod
    async def process_asyncio_requests(queries):
        url = "https://pokeapi.co/api/v2/ability/{}"
        async with aiohttp.ClientSession() as session:
            print("*** Processing your Pokemon Requests ***")
            async_coroutines = [get_pokemons_data(id_, url, session)
                                for id_ in queries]
            responses = await asyncio.gather(*async_coroutines)
            poke_list = [PokemonAbility(**res) for res in responses]
            queries.pokedex_list = poke_list

    def handle_request(self, req: Request):
        loop = asyncio.get_event_loop()
        responses = loop.run_until_complete(self.process_asyncio_requests(req.queries_data))
        req.pokedex_list = responses
        if self.next_handler is not None:
            self.next_handler.handle_request(req)



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
        print("\n----- Printing to Console ----- \n")
        for poke in req.pokedex_list:
            print(poke)
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class WriteHandler(BasePokemonHandler):
    def handle_request(self, req: Request):
        try:
            with open(req.output, 'w', encoding='utf-8') as export_file:
                export_file.write(''.join(str(req.pokedex_list)))
            print(f"------ Exported to {req.output} ------")
            if self.next_handler is not None:
                self.next_handler.handle_request(req)
        except FileNotFoundError:
            print("Please provide the correct filename or check if file exists in current directory")

