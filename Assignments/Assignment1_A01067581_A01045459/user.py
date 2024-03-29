from abc import abstractmethod
from budget_category import BudgetCategory, CategoryName
from bank import Bank
from transaction import Transaction
from datetime import datetime


class User:
    """
    A class representing a User of F.A.M
    """

    def __init__(self, user_name: str, user_age: int, bank: object, budget: dict, user_type: str):
        """
        An initializer for the User Class
        :param user_name: a String
        :param user_age: an Integer
        :param budget: a dictionary
        :param user_type: an enum
        """
        self._bank_details = bank
        self._user_name = user_name
        self._user_age = user_age
        self._budget = budget
        self._user_type = user_type

    @staticmethod
    def load_test_user_1():
        """
        Loads test user 1 into the program
        :return: a test User object
        """
        transaction_list_game = Transaction(datetime(2020, 12, 11, 19, 55), 300, "Gotham Bank",
                                            CategoryName.GAMES.value)
        transaction_list_clothes = Transaction(datetime(2020, 12, 11, 19, 55), 300, "Towers",
                                               CategoryName.CLOTHING.value)
        transaction_list_dine = Transaction(datetime(2020, 12, 11, 19, 55), 320, "Paul's", CategoryName.DINE.value)
        transaction_list_misc = Transaction(datetime(2020, 12, 11, 19, 55), 100, "Gotham Asylum",
                                            CategoryName.MISC.value)

        budget_games = BudgetCategory(CategoryName.GAMES.value, 40, False, 20, [transaction_list_game])
        budget_clothing = BudgetCategory(CategoryName.CLOTHING.value, 70, False, 50, [transaction_list_clothes])
        budget_dine = BudgetCategory(CategoryName.DINE.value, 50, False, 20, [transaction_list_dine])
        budget_miscellaneous = BudgetCategory(CategoryName.MISC.value, 70, False, 15, [transaction_list_misc])
        user_type = "Angel"
        bank_info = Bank("12345678", "Gotham Bank", 40000)

        return User("Bruce Wayne", 40, bank_info,
                    {0: budget_games, 1: budget_clothing, 2: budget_dine, 3: budget_miscellaneous}, user_type)

    @staticmethod
    def load_test_user_2():
        """
        Loads test user 2 into the program
        :return: a test User object
        """
        budget_games = BudgetCategory(CategoryName.GAMES.value, 50, False, 20, [])
        budget_clothing = BudgetCategory(CategoryName.CLOTHING.value, 70, False, 15, [])
        budget_dine = BudgetCategory(CategoryName.DINE.value, 80, False, 20, [])
        budget_miscellaneous = BudgetCategory(CategoryName.MISC.value, 70, False, 15, [])
        user_type = "Rebel"

        bank_info = Bank("00994421", "BMO", 2000)

        return User("Sepehr Mansouri", 22, bank_info,
                    {0: budget_games, 1: budget_clothing, 2: budget_dine, 3: budget_miscellaneous}, user_type)

    @staticmethod
    def load_test_user_3():
        """
        Loads test user 3 into the program
        :return: a test User object
        """
        budget_games = BudgetCategory(CategoryName.GAMES.value, 80, False, 20, [])
        budget_clothing = BudgetCategory(CategoryName.CLOTHING.value, 30, False, 15, [])
        budget_dine = BudgetCategory(CategoryName.DINE.value, 100, False, 90, [])
        budget_miscellaneous = BudgetCategory(CategoryName.MISC.value, 50, False, 15, [])
        user_type = "Troublemaker"

        bank_info = Bank("0987654", "RBC", 2000)

        return User("Sam Merati", 20, bank_info,
                    {0: budget_games, 1: budget_clothing, 2: budget_dine, 3: budget_miscellaneous}, user_type)

    def get_bank(self):
        """
        :return: Bank details
        """
        return self._bank_details

    def get_budget(self):
        """
        :return: Budget details
        """
        return self._budget

    @abstractmethod
    def get_message_warning(self):
        """
        :return: User type warning
        """
        pass

    def __repr__(self):
        """
        :return: a String representation of User
        """
        return f"User(user_name: {self._user_name}, user_age: {self._user_age}, " \
               f"bank: {self._bank_details}, budget: {self._budget}"

    def __str__(self):
        """
        :return: a real life String representation of a User object
        """
        return f"{self._user_name} is currently an active member of the bank {self._bank_details}. \n" \
               f"they are {self._user_age} years old with an allocated budget of ${self._budget}.\n" \
               f"they are also of the user type {self._user_type}"
