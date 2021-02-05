import datetime
from datetime import date
import time

from transaction import Transaction
from user import User


class TransactionMenu:

    def __init__(self):
        self._transaction_menu = []
        # self.user = super().__init__(user_name, user_age, account_number, bank_name, balance, budget)

    def add_new_transaction_record(self, transaction_record):
        self._transaction_menu.append(transaction_record)

    def list_all_available_transactions(self):
        if self._transaction_menu == 0:
            print("There are currently no transactions available to display")
        else:
            for transaction in self._transaction_menu:
                print(transaction)

    def __str__(self):
        return f"There are currently {len(self._transaction_menu)} transactions recorded."

    @staticmethod
    def prompt_user_the_menu():
        print("---- Program Initiated ----\n"
              "Please enter the following information\n"
              "To keep a record of the transaction for the given user:\n")

    @staticmethod
    def prompt_user_for_transaction_amount():
        print("Please Enter the transaction amount: ")

    @staticmethod
    def prompt_user_for_transaction_day():
        print("Please Enter the transaction day: ")

    @staticmethod
    def prompt_user_for_transaction_month():
        print("Please Enter the transaction day: ")

    @staticmethod
    def prompt_user_for_transaction_year():
        print("Please Enter the transaction day: ")

    @staticmethod
    def prompt_user_for_transaction_location():
        print("Please Enter the location of the transaction: ")

    @staticmethod
    def print_user_info():
        return

    @staticmethod
    def print_given_options():
        print("Please choose one of the given options bellow (Press \"Q\" to quit the program)\n"
              "1. Display all available transactions.\n"
              "2. Print User Information.\n"
              "3. Record a new Transaction.\n")

    def record_transaction_info(self):
        transaction_amount = float(input(TransactionMenu.prompt_user_for_transaction_amount()))
        transaction_location = str(input(TransactionMenu.prompt_user_for_transaction_location()))

        transaction_day = int(input(TransactionMenu.prompt_user_for_transaction_day()))
        transaction_month = int(input(TransactionMenu.prompt_user_for_transaction_month()))
        transaction_year = int(input(TransactionMenu.prompt_user_for_transaction_year()))
        given_date = date(transaction_year, transaction_month, transaction_day)

        self.add_new_transaction_record(Transaction(given_date, transaction_amount, transaction_location))

    # @property
    # def user_details(self):
    #     return self._user_details


def main():
    user_object = User.load_test_user()
    transaction_list = TransactionMenu()
    print(TransactionMenu.prompt_user_the_menu())
    user_input = ''
    print("Loading", end='')
    for seconds in range(1, 4):
        # time.sleep(1)
        print(".", end='')
    print()

    # user_options = {1: transaction_list.list_all_available_transactions(),
    #                 2: str(transaction_list.user_details), 3: transaction_list.record_transaction_info()}

    while user_input != "Q":
        print(TransactionMenu.print_given_options())
        user_input = int(input(""))


if __name__ == '__main__':
    main()
