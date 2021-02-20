from enum import Enum


class CategoryName(Enum):
    GAMES = "Games and Entertainment"
    CLOTHING = "Clothing and Accessories"
    DINE = "Eating Out"
    MISC = "Miscellaneous"


class BudgetCategory:

    def __init__(self, category_name, budget_limit, is_locked, current_spent
                 , transactions):
        self._category_name = category_name
        self._budget_limit = budget_limit
        self._is_locked = is_locked
        self._current_spent = current_spent
        self._budget_count = budget_limit - current_spent
        self._transactions = transactions

    def print_all_transactions(self):
        transactions = ""
        for i in self._transactions:
            transactions = i + "\n"
        return transactions

    def __repr__(self):
        return f"Category: {self._category_name}" \
               f"\n Total Amount: {self._budget_limit}" \
               f"\n Amount spent: {self._current_spent}" \
               f"\n Amount left: {self._budget_count}" \
               f"\n Locked: {self._is_locked}" \
               f"\n Transactions: " \
               f"\n {self._transactions}"

    def is_overlimit(self):
        return self._current_spent > self._budget_limit
