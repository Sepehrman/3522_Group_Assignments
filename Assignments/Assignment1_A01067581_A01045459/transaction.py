from datetime import datetime


class Transaction:
    """
    A class representing a Transaction Record
    """

    def __init__(self, transaction_timestamp: datetime, transaction_amount: float,
                 transaction_location: str, transaction_budget: str):
        """
        Initializer for the Transaction class
        :param transaction_time: a datetime module
        :param transaction_amount: a float
        :param transaction_location: a String
        """
        self._transaction_timestamp = transaction_timestamp
        self._transaction_amount = transaction_amount
        self._transaction_location = transaction_location
        self._transaction_budget = transaction_budget

    def get_transaction_timestamp(self):
        """
        :return: returns the transaction time
        """
        return self._transaction_timestamp

    def get_transaction_amount(self):
        """
        :return: a transaction amount
        """
        return self._transaction_amount

    def get_transaction_location(self):
        """
        :return: a transaction location
        """
        return self._transaction_location

    def get_transaction_budget(self):
        """
        :return: a transaction budget
        """
        return self._transaction_budget

    def __str__(self):
        """
        :return: a real life representation of the Transaction details
        """
        return f"Transaction details:\n" \
               f"Store/Website name: {self._transaction_location}\n" \
               f"Transaction amount: ${self._transaction_amount}\n" \
               f"Budget category: {self._transaction_budget}\n" \
               f"Transaction Time: {self._transaction_timestamp}\n"

    def __repr__(self):
        """
        :return: A String representation of Transaction
        """
        return f"Transaction details:\n" \
               f"Store/Website name: {self._transaction_location}\n" \
               f"Transaction amount: ${self._transaction_amount}\n" \
               f"Budget category: {self._transaction_budget}\n" \
               f"Transaction Time: {self._transaction_timestamp}\n"
