from abc import ABC, abstractmethod

from request_module import Request


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

