import ast

import argparse
from abc import abstractmethod, ABC
import enum

from des import DesKey


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.
    """

    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        req = Request()
        req.encryption_state = CryptoMode(args.mode)
        req.data_input = args.string
        req.input_file = args.file
        req.output = args.output
        req.key = args.key
        print(req)
        return req
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Crypto:

    def __init__(self):
        self.encryption_start_handler = EncryptionHeadHandler()
        self.decryption_start_handler = DecryptionHeadHandler()

    def execute_request(self, req: Request):

        head_mapper = {CryptoMode.EN: self.encryption_start_handler,
                       CryptoMode.DE: self.decryption_start_handler}
        current_handler = head_mapper.get(req.encryption_state)

        if req.input_file is not None:
            next_handler = ReadFileHandler()
            current_handler.set_handler(next_handler)
            current_handler = next_handler
        if req.encryption_state == CryptoMode.DE:
            next_handler = DecryptHandler()
        else:
            next_handler = EncryptHandler()
        current_handler.set_handler(next_handler)
        current_handler = next_handler

        if req.output == "print":
            next_handler = PrintHandler()
        else:
            next_handler = WriteHandler()
        current_handler.set_handler(next_handler)

        return head_mapper[req.encryption_state].handle_request(req)


class BaseCryptoHandler(ABC):

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle_request(self, req: Request):
        pass

    def set_handler(self, handler):
        self.next_handler = handler


class EncryptionHeadHandler(BaseCryptoHandler):

    def handle_request(self, req: Request):
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class DecryptionHeadHandler(BaseCryptoHandler):

    def handle_request(self, req: Request):
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class ReadFileHandler(BaseCryptoHandler):

    def handle_request(self, req: Request):
        try:
            mode_mapping = {CryptoMode.EN: "r",
                            CryptoMode.DE: "br"}

            data = ""
            with open(req.input_file, mode_mapping[req.encryption_state]) as read_file:
                data += "".join((str(line) for line in read_file.readlines()))
                req.data_input = data
            if self.next_handler is not None:
                self.next_handler.handle_request(req)
        except FileNotFoundError:
            print("Please provide the correct filename!")


class PrintHandler(BaseCryptoHandler):

    def handle_request(self, req: Request):
        print_mapper = {CryptoMode.EN: "Encryption:",
                        CryptoMode.DE: "Decryption:"}

        print(print_mapper[req.encryption_state], req.result)
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class WriteHandler(BaseCryptoHandler):

    def handle_request(self, req: Request):
        try:
            print_mapper = {CryptoMode.EN: "Encrypted:",
                            CryptoMode.DE: "Decrypted:"}

            mode_mapper = {CryptoMode.EN: "bw",
                           CryptoMode.DE: "w"}

            with open(req.output, mode_mapper[req.encryption_state]) as file:
                file.write(str(req.result))
            print(print_mapper[req.encryption_state], "to file", req.output)
            if self.next_handler is not None:
                self.next_handler.handle_request(req)
        except FileNotFoundError:
            print("Please provide the correct filename or check if file exists in current directory")


class EncryptHandler(BaseCryptoHandler):

    @staticmethod
    def encrypt_request(req):
        return DesKey(req.key.encode()).encrypt(req.data_input.encode(), padding=True)

    def handle_request(self, req: Request):
        req.result = self.encrypt_request(req)
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


class DecryptHandler(BaseCryptoHandler):

    @staticmethod
    def decrypt_request(req):
        data_decrypt = ast.literal_eval(req.data_input)
        return DesKey(req.key.encode()).decrypt(data_decrypt, padding=True)

    def handle_request(self, req: Request):
        req.result = self.decrypt_request(req)
        if self.next_handler is not None:
            self.next_handler.handle_request(req)


def main(req: Request):
    Crypto().execute_request(req)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
