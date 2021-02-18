class Bank:

    def __init__(self, user_name, user_age, account_number, bank_name, balance, budget, user_type):
        super().__init__(user_name, user_age, budget, user_type)
        self._account_number = account_number
        self._bank_name = bank_name
        self._balance = balance

    def get_bank_name(self):
        return self._bank_name

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number
