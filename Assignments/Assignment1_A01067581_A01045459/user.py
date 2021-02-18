from abc import ABC, abstractmethod
from budget_category import Budget
from bank import Bank

class User:
    """
    A class representing a User of F.A.M
    """

    def __init__(self, user_name, user_age, account_number, bank_name, balance, budget, user_type):
        """
        An initializer for the User Class
        :param user_name: a String
        :param user_age: an Integer
        :param account_number: a String
        :param bank_name: a String
        :param balance: a float
        :param budget: a dictionary
        :param user_type: an enum
        """
        self._user_name = user_name
        self._user_age = user_age
        self._account_number = account_number
        self._bank_name = bank_name
        self._balance = balance
        self._budget = budget
        self._user_type = user_type

    @staticmethod
    def load_test_user():
        """
        :return: a test User object
        """
        return User("Bruce Wayne", 10, "12345678", "Gotham Bank", 98.32,
                    {"Games and Entertainment": 30, "Clothing and Accessories": 20, "Eating Out": 18,
                     "Miscellaneous": 30.32})

    @abstractmethod
    def get_message_warning(self):
        pass

    def __repr__(self):
        """
        :return: a String representation of User
        """
        return f"User(user_name: {self._user_name}, user_age: {self._user_age}, " \
               f"account_number: {self._account_number}," \
               f" bank_name: {self._bank_name}, balance: {self._balance}, budget: {self._budget}"

    def __str__(self):
        """
        :return: a real life String representation of a User object
        """
        return f"{self._user_name} is currently an active member of {self._bank_name}. \n" \
               f"they are {self._user_age} years old with the bank account number {self._account_number}.\n" \
               f"They currently have a balance of ${self._balance} with an allocated budget of ${self._budget}"