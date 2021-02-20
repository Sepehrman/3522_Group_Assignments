class Bank:

    def __init__(self, account_number, bank_name, balance):
        self._account_number = account_number
        self._bank_name = bank_name
        self._balance = balance

    def get_bank_name(self):
        return self._bank_name

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __repr__(self):
        return f"Bank Name: {self._bank_name}" \
               f"\n Total Amount: {self._account_number}" \
               f"\n Amount spent: {self._balance}"