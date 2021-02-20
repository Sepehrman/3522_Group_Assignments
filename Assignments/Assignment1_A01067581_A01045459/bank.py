class Bank:

    def __init__(self, account_number, bank_name, balance):
        """
        An Initializer for a bank
        :param account_number: a String
        :param bank_name: A String
        :param balance: A Float
        """
        self._account_number = account_number
        self._bank_name = bank_name
        self._balance = balance

    def get_bank_name(self):
        """
        Getter for Bank Name
        :return: a String
        """
        return self._bank_name

    def get_balance(self):
        """
        Getter for Bank's balance
        :return: a Float
        """
        return self._balance

    def get_account_number(self):
        """
        Getter for Bank Account Number
        :return: A String
        """
        return self._account_number

    def __repr__(self):
        """
        :return: A String representation of the Bank Class
        """
        return f"Bank Name: {self._bank_name}" \
               f"\n Account Number: {self._account_number}" \
               f"\n Total Balance: {self._balance}\n"
