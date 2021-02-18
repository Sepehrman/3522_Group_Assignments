from user import User
from budget_category import BudgetCategory, CategoryName
from user_types import Angel, Rebel, TroubleMaker

class UserMenu:

    def __init__(self):
        self._users = []
        self._current_user = User

    def view_budget(self):
        return

    def record_selftransaction(self):
        pass

    def view_transaction_budget(self):
        pass

    def view_bank_account_details(self):
        pass

def main():

    user_input = input("Would you like to use a default user?")
    if  user_input == "Y":
        user_object = User.load_test_user()
    else:
        user_name = input("Enter the name for your user\n")
        user_age = input("Enter the age of your user\n")
        user_type = input("What is the user type")
        bank_details = input("")

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
