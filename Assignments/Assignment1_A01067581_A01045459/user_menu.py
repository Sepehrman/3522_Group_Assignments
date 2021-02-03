class UserMenu:

    def __init__(self, budgets):
        self._budgets = budgets


    def view_budget(self):
        return "---- Budgets ----\n" \
               "Amount Left: " \
               "Amount Spent: " \
               "Amount Allocated to Budget: "

    def record_transaction(self):
        pass

    def view_transaction_budget(self):
        pass

    def view_bank_account_details(self):
        pass

