""" This module houses the library"""
from book import Book
from catalogue import Catalogue
from journal import Journal
from dvd import DVD


class Library:
    """
    The Library consists of a list of library items and provides an
    interface for users to check out, return and find library items.
    """

    def __init__(self, library_item_list):
        """
        Initialize the library with a catalogue of library items.
        :param library_item_list: a sequence of library item objects.
        """
        self._catalogue = Catalogue(library_item_list)

    def check_out(self, call_number):
        """
        Check out an library item with the given call number from the catalogue.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_item = self._catalogue.retrieve_library_item_by_call_number(call_number)
        if library_item.check_availability():
            status = self._catalogue.reduce_library_item_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find item with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_item(self, call_number):
        """
        Return a library item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self._catalogue.retrieve_library_item_by_call_number(call_number)
        if status:
            print("item returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}"
                  f". Return failed.")

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of library items, check out, return, find, add, remove a library item.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Find an item")
            print("5. Add an item")
            print("6. Remove an item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7) ")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.display_available_items()
                user_input = input("Press Enter to continue ")
            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out. ")
                self.check_out(call_number)

            elif user_input == 3:
                call_number = str(input("Enter the call number of the item you wish to return. "))
                self.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the item: ")
                found_titles = self._catalogue.find_library_item(input_title)
                print("We found the following: ")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title ")

            elif user_input == 5:
                self._catalogue.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the item ")
                self._catalogue.remove_library_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7. ")

        print("Thank you for visiting the Library. ")

    def display_available_items(self):
        """
        Display all the items in the library.
        """
        print("List of items in the library")
        print("--------------", end="\n\n")
        for library_item in self._catalogue.get_library_item_list():
            print(library_item)


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """

    item_list = [
        Book("J K Rowling", "100.200.300", "Harry Potter 1", 2),
        Book("J K Rowling", "999.224.854", "Harry Potter 2", 5),
        Book("J K Rowling", "631.495.302", "Dr. Faustus", 4),
        Book("Dr. Seuss", "123.02.204", "The Cat in the Hat", 1),
        Journal("110.234.132", "Life of Bob Dylan", 1, "Alan Jones", 2, "Authentic Publishing"),
        Journal("102.314.324", "Your Kitchen", 1, "Nancy Jameson", 2, "Home Alone"),
        DVD("200.100.600", "Spider-Man 4", 2, "28-Dec-2023", 51235),
        DVD("200.100.200", "Mission Impossible 10", 2, "02-Apr-2025", 81759)
    ]

    my_epic_library = Library(item_list)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
