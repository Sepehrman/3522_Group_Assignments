"""
module containing the interface for library items
"""
from abc import abstractmethod


class LibraryItem:
    """
        Represents an item in a library which is identified through
        it's call number.
        """
    @abstractmethod
    def __init__(self, call_number, title, num_copies):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_number
        self._title = title
        self._num_copies = num_copies

    def get_title(self):
        """
        Returns the title of the library item.
        :return: a string
        """
        return self._title.title()

    def increment_number_of_copies(self):
        """
        Set's the number of copies of a library item
        """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
        Set's the number of copies of a library item
        """
        self._num_copies -= 1

    def get_num_copies(self):
        """
        Returns the number of copies that are available for this
        specific library item.
        :return: an int
        """
        return self._num_copies

    @property
    def call_number(self):
        """
        Right, this here is another way of using properties.
        We use decorators. The @property decorator defines a property
        that only allows us to GET a value and not set one.

        I want to point out that I have not expected you to do this in
        your labs. I'm using this as an opportunity to introduce you to
        a new way of avoiding mechanical getters and setters.
        :return:
        """
        return self._call_num

    def check_availability(self):
        """
        Returns True if the library item is available and False otherwise
        :return: A Boolean
        """
        return self._num_copies > 0

    def __str__(self):
        return f"---- library item: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}"
