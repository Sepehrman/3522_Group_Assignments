import datetime
from datetime import date
import time

from transaction import Transaction
from user import User

class TransactionMenu:

    def __init__(self):
        """
        An initializer for TransactionMenu
        """
        self._transaction_menu = []

    def list_all_available_transactions(self):
        """
        Displays all available transactions
        """
        if len(self._transaction_menu) == 0:
            print("*** There are currently no transactions available to display ***\n")
        else:
            for transaction in self._transaction_menu:
                print(str(transaction))

    def __str__(self):
        """
        :return: A real life representation of the transaction menu
        """
        return f"There are currently {len(self._transaction_menu)} transactions recorded."

    def __repr__(self):
        """
        :return: a String representation of a Transaction Menu object
        """
        return f"TransactionMenu(list: {self._transaction_menu})"

    @staticmethod
    def print_given_options():
        """
        Prints all available options to choose from
        """
        print("---- Program Initiated ----\n"
              "Please choose one of the given options bellow (Press \"0\" to quit the program)\n"
              "1. Display all available transactions.\n"
              "2. Print User Information.\n"
              "3. Record a new Transaction.")

    def add_new_transaction_record(self, transaction_record):
        """
        Adds a new transaction object to the current transaction records
        :param transaction_record: an Object
        """
        self._transaction_menu.append(transaction_record)

    def record_transaction_info(self):
        """
        Records a transaction info from the user
        """
        transaction_amount = float(input("Please Enter the transaction amount: "))
        transaction_location = str(input("Please Enter the name of the Store/Website: "))
        category_choice = int(input("Please select the budget category: \n"
                                       " 1.Games and Entertainment\n"
                                       " 2.Clothing and Accessories\n"
                                       " 3.Eating Out\n"
                                       " 4.Miscellaneous\n"))
        if category_choice == 1:
            transaction_budget = "Games and Entertainment"
        elif category_choice == 2:
            transaction_budget = "Clothing and Accessories"
        elif category_choice == 3:
            transaction_budget = "Eating Out"
        elif category_choice == 4:
            transaction_budget = "Miscellaneous"
        else:
            print("Invalid Input")
        transaction_day = int(input("Please Enter the transaction day: "))
        transaction_month = int(input("Please Enter the transaction month: "))
        transaction_year = int(input("Please Enter the transaction year: "))
        given_date = date(transaction_year, transaction_month, transaction_day)
        transaction_obj = Transaction(given_date, transaction_amount, transaction_location, transaction_budget)

        self.add_new_transaction_record(transaction_obj)


def main():

    user_object = User.load_test_user()
    transaction_list = TransactionMenu()
    user_input = ''
    print("Loading", end='')
    for seconds in range(1, 4):
        time.sleep(0.5)
        print(".", end='')
    print()

    while user_input != 0:
        TransactionMenu.print_given_options()
        user_input = int(input(""))
        if user_input == 1:
            transaction_list.list_all_available_transactions()
        elif user_input == 2:
            print(str(user_object))
        elif user_input == 3:
            transaction_list.record_transaction_info()
        else:
            print("Please enter a number from the given coordinates")

    print("Farewell!")


if __name__ == '__main__':
    main()
