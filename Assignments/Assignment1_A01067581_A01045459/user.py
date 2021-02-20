from abc import ABC, abstractmethod
from budget_category import BudgetCategory, CategoryName
# from user_types import Angel
from bank import Bank


class User:
    """
    A class representing a User of F.A.M
    """

    def __init__(self, user_name: str, user_age: int, bank: object, budget: dict, user_type: str):  # change user_type to enumerate
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
        self._bank_details = bank
        self._user_name = user_name
        self._user_age = user_age
        self._budget = budget
        self._user_type = user_type

    @staticmethod
    def load_test_user():
        """
        :return: a test User object
        """
        budget_games = BudgetCategory(CategoryName.GAMES.value, 40, False, 20, [])
        budget_clothing = BudgetCategory(CategoryName.CLOTHING.value, 70, False, 15, [])
        budget_dine = BudgetCategory(CategoryName.DINE.value, 80, False, 20, [])
        budget_miscellaneous = BudgetCategory(CategoryName.MISC.value, 70, False, 15, [])
        user_type = "ANGEL"

        bank_info = Bank("12345678", "Gotham Bank", 1000)

        return User("Bruce Wayne", 20, bank_info,
                    {0: budget_games, 1: budget_clothing, 2: budget_dine, 3: budget_miscellaneous}, user_type)

    def get_bank(self):
        return self._bank_details

    def get_budget(self):
        return self._budget

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
