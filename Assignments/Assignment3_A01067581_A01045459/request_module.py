import argparse

import aiohttp

from pokemon import PokedexMode


class Request:

    def __init__(self):
        self.pokedex_mode = None
        self.input_data = None
        self.input_file = None
        self.expanded = None
        self.output = None
        self.queries_data = None
        self.pokedex_list = None

    def __str__(self):
        return f"Request: Mode: {self.pokedex_mode}, InputData: {self.input_data}, InputFile: {self.input_file}, " \
               f"Output: {self.output}, Expanded: {self.expanded}, QueryData = {self.queries_data}"


async def get_pokemons_data(id, url, session: aiohttp.ClientSession):
    target_url = url.format(id)
    response = await session.request(method="GET", url=target_url)
    json_dict = await response.json()
    return json_dict


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
        quit()