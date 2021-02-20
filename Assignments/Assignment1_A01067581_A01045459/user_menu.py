from transaction import Transaction
from user import User
from budget_category import BudgetCategory, CategoryName
# from user_types import Angel, Rebel, TroubleMaker
from datetime import datetime
from bank import Bank

class UserMenu:

    def __init__(self):
        self._users = []
        # self._current_user = self._users[0]

    def register_user(self):
        print("Please enter your child's information")
        user_name = str(input("Enter the name for your child: "))
        user_age = int(input("Enter the age of your child: "))
        user_bank = self.set_bank()
        user_budgets = self.set_budgets()
        user_type = "ANGEL"
        self._users.append(User(user_name, user_age, user_bank, user_budgets, user_type))

    @staticmethod
    def set_budgets():
        budget_names = [CategoryName.GAMES.value, CategoryName.CLOTHING.value, CategoryName.DINE.value,
                        CategoryName.MISC.value]
        budget_categories = {0: None, 1: None, 2: None, 3: None}

        for i in range(0, 4):
            print(f"\nThis is for budget {budget_names[i]:}")
            budget_limit = float(input("What is your budget limit? "))
            current_spent = float(input("How much was currently spent?"))
            budget_categories[i] = BudgetCategory(budget_names[i], budget_limit, False, current_spent, [])
        return budget_categories

    @staticmethod
    def options_menu():
        choice = int(input("1. View Budgets\n"
                           "2. Record a Transaction\n"
                           "3. View Transaction by Budget\n"
                           "4. View Bank Account Details\n"
                           "0. Quit Program\n"))
        return choice

    def add_new_user(self, new_user):
        self._users.append(new_user)

    @staticmethod
    def budgets_menu():
        category_choice = int(input("Please select a budget category: \n"
                                    " 1.Games and Entertainment\n"
                                    " 2.Clothing and Accessories\n"
                                    " 3.Eating Out\n"
                                    " 4.Miscellaneous\n"))
        return category_choice - 1

    @staticmethod
    def set_bank():
        account_number = int(input("Enter the account number: "))
        bank_name = str(input("Enter bank name: "))
        balance = float(input("Enter balance: "))
        return Bank(account_number, bank_name, balance)

    @staticmethod
    def view_budget(user):
        for i in range(0, 4):
            print(user._budget[i])

    def record_transaction(self, user_obj):
        """
        Records a transaction info from the user
        """
        transaction_amount = float(input("Please Enter the transaction amount: "))
        transaction_location = str(input("Please Enter the name of the Location: "))
        transaction_year = int(input("Please Enter the transaction year: "))
        transaction_month = int(input("Please Enter the transaction month: "))
        transaction_day = int(input("Please Enter the transaction day: "))
        transaction_hour = int(input("Please Enter the transaction hour: "))
        transaction_minute = int(input("Please Enter the transaction minute: "))
        transaction_timestamp = datetime(transaction_year, transaction_month, transaction_day,
                                         transaction_hour, transaction_minute)

        category_choice = self.budgets_menu()
        budget_category = user_obj._budget[category_choice]
        budget_name = ''
        if category_choice == 1:
            budget_name = CategoryName.GAMES.value
        elif category_choice == 2:
            budget_name = CategoryName.CLOTHING.value
        elif category_choice == 3:
            budget_name = CategoryName.DINE.value
        elif category_choice == 4:
            budget_name = CategoryName.MISC.value

        transaction_obj = Transaction(transaction_timestamp, transaction_amount, transaction_location, budget_name)
        budget_category._transactions.append(transaction_obj)

    def view_transaction_budget(self, user_obj):
        category_choice = self.budgets_menu()
        print(user_obj._budget[category_choice]._transaction)

    # def view_bank_account_details(self, user):
    #     print(user._bank_details)


def main():
    print("------- Welcome to F.A.M -------\n")
    user_menu = UserMenu()
    new_user = User.load_test_user()
    user_menu.add_new_user(new_user)
    # user_menu.register_user()
    # user_menu.
    user_input = ''

    while user_input != 0:
        user_input = user_menu.options_menu()
        if user_input == 1:
            # add back to method user_menu._users[0]
            user_menu.view_budget(user_menu._users[0])
        elif user_input == 2:
            user_menu.record_transaction(user_menu._users[0])
        elif user_input == 3:
            user_menu.view_transaction_budget(user_menu._users[0])
        elif user_input == 4:
            user_menu.view_bank_account_details(user_menu._users[0])
        else:
            print("Number should be in range 1-4")

    print("Farewell!")


if __name__ == '__main__':
    main()
