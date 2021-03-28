from book import Book
from dvd import DVD
from journal import Journal
from abc import abstractmethod, ABC


class FactoryItem(ABC):

    @abstractmethod
    def build_item(self):
        pass


class BookFactory(FactoryItem):

    def build_item(self):
        """
        Return book object with class attributes inputted by user.
        :return: A book object.
        """
        title = input("Enter the title: ")
        num_copies = int(input("Enter number of copies (positive number): "))
        author = input("Enter the book author: ")
        call_number = input("Enter the call number: ")
        return Book(author, call_number=call_number, title=title, num_copies=num_copies)


class DVDFactory(FactoryItem):

    def build_item(self):
        """
        Return dvd object with class attributes inputted by user.
        :return: A dvd object.
        """
        call_number = input("Enter the call number: ")
        title = input("Enter the title: ")
        num_copies = int(input("Enter number of copies (positive number): "))
        release_date = input("Enter the release date: ")
        region_code = int(input("Enter the region code: "))
        return DVD(release_date, region_code, call_number=call_number, title=title, num_copies=num_copies)


class JournalFactory(FactoryItem):

    def build_item(self):
        """
        Return journal object with class attributes inputted by user.
        :return: A journal object.
        """
        call_number = input("Enter the call number: ")
        title = input("Enter the title: ")
        num_copies = int(input("Enter number of copies (positive number): "))
        issue_number = int(input("Enter the issue number: "))
        publisher = input("Enter the publisher: ")
        return Journal(issue_number, publisher, call_number=call_number, title=title, num_copies=num_copies)
