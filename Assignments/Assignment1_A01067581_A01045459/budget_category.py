from enum import Enum


class CategoryName(Enum):
    GAMES = "Games and Entertainment"
    CLOTHING = "Clothing and Accessories"
    DINE = "Eating Out"
    MISC = "Miscellaneous"


class BudgetCategory:

    def __init__(self, category_name, budget_limit, is_locked, current_spent
                 , transactions):
        """
        Budget Category initializer
        :param category_name: The name of the budget category
        :param budget_limit: The limit of this category
        :param is_locked: Locked budget boolean
        :param current_spent: Amount spend from budget
        :param transactions: Transaction history of the budget
        """
        self._category_name = category_name
        self._budget_limit = budget_limit
        self._is_locked = is_locked
        self._current_spent = current_spent
        self._budget_count = budget_limit - current_spent
        self._transactions = transactions

    def print_all_transactions(self):
        """
        Prints all transactions
        """
        transactions = ""
        for i in self._transactions:
            transactions = i + "\n"
        return transactions

    def __repr__(self):
        """
        :return: a String representation of the class BudgetCategory
        """
        return f"Category: {self._category_name}" \
               f"\n Total Amount: {self._budget_limit}" \
               f"\n Amount spent: {self._current_spent}" \
               f"\n Amount left: {self._budget_count}" \
               f"\n Locked: {self._is_locked}" \
               f"\n Transactions: " \
               f"\n {self._transactions}"

    def is_overlimit(self):
        """
        Checks if budget limit has exceeded
        :return: a Boolean
        """
        return self._current_spent > self._budget_limit
