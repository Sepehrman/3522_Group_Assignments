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


