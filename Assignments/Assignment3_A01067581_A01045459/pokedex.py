import asyncio

from pokeretriever import PokeDex, setup_request_commandline, process_asyncio_requests
from request_module import Request


def main(req: Request):
    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(process_asyncio_requests(['24', '25']))
    PokeDex().execute_requests(req)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)





