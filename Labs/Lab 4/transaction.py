class Transaction:
    """
    A class representing a Transaction Record
    """

    def __init__(self, transaction_time, transaction_amount, transaction_location):
        """
        Initializer for the Transaction class
        :param transaction_time: a datetime module
        :param transaction_amount: a float
        :param transaction_location: a String
        """
        self._transaction_time = transaction_time
        self._transaction_amount = transaction_amount
        self._transaction_location = transaction_location

    def get_transaction_time(self):
        """
        :return: returns the transaction time
        """
        return self._transaction_time

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

    def __str__(self):
        return f"There are currently {self}"

    def __repr__(self):
        return f"Transaction(transaction_time: {self._transaction_time}, " \
               f" transaction_amount: {self._transaction_amount}," \
               f" transaction_location: {self._transaction_location})"
