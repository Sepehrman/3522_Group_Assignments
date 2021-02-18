from enum import Enum

class CategoryName(Enum):
    GAMES = "Games and Entertainment"
    CLOTHING = "Clothing and Accessories"
    DINE = "Eating Out"
    MISC = "Miscellaneous"

class Budget:

    def __init__(self, category_name, budget_limit, is_locked, current_spent
                 , budget_count, transactions):
        self._category_name = category_name
        self._budget_limit = budget_limit
        self._is_locked = is_locked
        self._current_spent = current_spent
        self._budget_count = budget_count
        self._transactions = transactions


    def get_categories(self):
        return self._category_name

    def add_category(self):
        pass

    def display_categories(self):
        pass

    def is_overlimit(self):
        return self._current_spent > self._budget_limit


