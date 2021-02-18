from user import User


def view_budget():
    return "---- Budgets ----\n" \
           "Amount Left: " \
           "Amount Spent: " \
           "Amount Allocated to Budget: "


class UserMenu:

    def __init__(self):
        self._users = []
        self._current_user = User

    def record_transaction(self):
        pass

    def view_transaction_budget(self):
        pass

    def view_bank_account_details(self):
        pass
