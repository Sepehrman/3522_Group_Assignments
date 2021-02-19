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

    def get_category_name(self):
        return self._category_name

    def get_budget_name(self):
        return self._budget_limit

    def get_is_locked(self):
        return self._is_locked

    def get_budget_limit(self):
        return self._budget_limit

    def get_current_spent(self):
        return self._current_spent

    def get_budget_count(self):
        return self._budget_count

    def get_transactions(self):
        return self._transactions

    def print_results(self):
        print(f"Category: {self._category_name}"
        f"\n    Locked: {self._is_locked}"
        f"\n    Total Amount: {self._budget_limit}"
        f"\n    Amount spent: {self._current_spent}"
        f"\n    Amount left: {self._budget_count}")

    def __repr__(self):
        return f"Category: {self._category_name}"
        f"\n Locked: {self._is_locked}"
        f"\n Amount spent: {self._current_spent}"
        f"\n Amount left: {self._budget_count}"
        f"\n Total Amount: {self._budget_limit}"

    def is_overlimit(self):
        return self._current_spent > self._budget_limit
