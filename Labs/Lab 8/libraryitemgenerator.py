"""
module containing class that generates library item from user input and its module helper functions.
"""
from book import Book
from dvd import DVD
from journal import Journal
from abc import ABC, abstractmethod
from library_factory import JournalFactory, BookFactory, DVDFactory


class LibraryItemGenerator(object):
    """
    Class that generates a library item based off user input
    """
    @staticmethod
    def generate_library_item():
        """
        Return library item with attributes and type chosen by user.
        :return: A library item.
        """
        item_type = get_item_type_from_user()
        return item_type


def get_item_type_from_user():
    """
    Return integer representing what library item the user want to create
    :return: An integer.
    """

    resulting_class = {1: BookFactory, 2: DVDFactory, 3: JournalFactory}
    user_input = None
    factory_item_class = None
    while user_input not in range(1, 4):
        print("\nAdd an item to the library.")
        print("-----------------------")
        print("1. Add a Book")
        print("2. Add a DVD")
        print("3. Add a Journal")
        try:
            user_input = int(input("Please enter your choice (1-3) "))
            if input == '':
                continue
            else:
                factory_item_class = resulting_class.get(user_input)
        except ValueError:
            print("Enter the correct input")
    return factory_item_class()


def build_library_item(item_type, library_item_attributes):
    """
    Return library item of type book, dvd, or journal with class attributes inputted by user.
    :param item_type: A integer
    :param library_item_attributes: A tuple with three values.
    :return: A library item
    """
    if item_type == 1:
        return BookFactory.build_item(library_item_attributes)

    elif item_type == 2:
        return DVDFactory.build_item(library_item_attributes)

    elif item_type == 3:
        return JournalFactory.build_item(*library_item_attributes)

