""" This modules houses the catalogue"""
import difflib
from libraryitemgenerator import LibraryItemGenerator


class Catalogue:
    """
    Class representing a catalogue of library items
    """
    def __init__(self, item_list):
        """
        Initialize the library with a list of library items.
        :param item_list: a sequence of library item objects.
        """
        self._library_item_list = item_list

    def get_library_item_list(self):
        """
        Return list of library items.
        :return: list of library item type objects
        """
        return self._library_item_list

    def find_library_item(self, title):
        """
        Find library items with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = [library_item.get_title() for library_item in self._library_item_list]
        results = difflib.get_close_matches(title, title_list, cutoff=0.5)
        return results

    def add_item(self):
        """
        Add a brand new book to the library with a unique call number.
        """
        new_library_item = LibraryItemGenerator.generate_library_item()
        found_library_item = self.retrieve_library_item_by_call_number(new_library_item.call_number)

        if found_library_item:
            print(f"Could not add item with call number "
                  f"{new_library_item.call_number}. It already exists. ")
        else:
            self._library_item_list.append(new_library_item)
            print("item added successfully! item details:")
            print(new_library_item)

    def remove_library_item(self, call_number):
        """
        Remove an existing library item from the catalogue
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_library_item = self.retrieve_library_item_by_call_number(call_number)
        if found_library_item:
            self._library_item_list.remove(found_library_item)
            print(f"Successfully removed {found_library_item.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"library item with call number: {call_number} not found.")

    def reduce_library_item_count(self, call_number):
        """
        Decrement the library item count for a library item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the library item was found and count decremented, false
        otherwise.
        """
        library_item = self.retrieve_library_item_by_call_number(call_number)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_library_item_count(self, call_number):
        """
        Increment the library item count for a library item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the library item was found and count incremented, false
        otherwise.
        """
        library_item = self.retrieve_library_item_by_call_number(call_number)
        result = True if library_item else False
        return result

    def retrieve_library_item_by_call_number(self, call_number):
        """
        Retrieve of a library item with the given call number from the catalogue.
        :param call_number: a string
        :return: library item object if found, None otherwise
        """
        found_library_item = None
        for library_item in self._library_item_list:
            if library_item.call_number == call_number:
                found_library_item = library_item
                break
        return found_library_item
