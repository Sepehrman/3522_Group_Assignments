from user import User
from budget_category import BudgetCategory, CategoryName
from user_types import Angel, Rebel, TroubleMaker


class UserMenu:
    def __init__(self):
        self._users = []
        self._current_user = User

    def add_user(self):
        print("Please enter your child's information")
        try:
            user_name = str(input("Enter the name for your child: "))
            user_age = int(input("Enter the age of your child: "))
            user_account_number = int(input("Enter the account number of your child: "))
            user_bank_name = str(input("What is the name of your child's bank: "))
            user_balance = float(input("What balance is allocated to your child's bank: "))
            user_budgets = float(input("What are your child's budgets: "))
            self._users.append(User(user_name, user_age, user_account_number
                                    , user_bank_name, user_balance, user_budgets))
        except TypeError:
            print("The information you've provided is not of the correct format")
        finally:
            print("Process completed")

    @staticmethod
    def print_given_options():
        print("1. View Budgets\n"
              "2. Record a Transaction\n"
              "3. View Transaction by Budget\n"
              "4. View Bank Account Details\n")

    def view_budget(self):
        pass

    def record_selftransaction(self):
        pass

    def view_transaction_budget(self):
        pass

    def view_bank_account_details(self):
        pass


def main():
    print("------- Welcome to F.A.M -------")

    user_menu = UserMenu()
    user_menu.add_user()

    # transaction_list = TransactionMenu()
    # user_input = ''
    # print("Loading", end='')
    # for seconds in range(1, 4):
    #     time.sleep(0.5)
    #     print(".", end='')
    # print()
    #
    # while user_input != 0:
    #     TransactionMenu.print_given_options()
    #     user_input = int(input(""))
    #     if user_input == 1:
    #         transaction_list.list_all_available_transactions()
    #     elif user_input == 2:
    #         print(str(user_object))
    #     elif user_input == 3:
    #         transaction_list.record_transaction_info()
    #     else:
    #         print("Please enter a number from the given coordinates")

    print("Farewell!")


if __name__ == '__main__':
    main()
