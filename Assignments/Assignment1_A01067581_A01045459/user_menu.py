from transaction import Transaction
from user import User
from budget_category import BudgetCategory, CategoryName
from datetime import datetime
from bank import Bank


class UserMenu:
    user_count = 0

    def __init__(self):
        """
        An Initializer for Users and current users
        """
        self._users = []
        self._current_user = self._users

    def register_user(self):
        """
        Registers a new user into the list of user
        """
        print("Please enter your child's information")
        try:
            user_name = str(input("Enter the name for your child: "))
            user_age = int(input("Enter the age of your child: "))
            user_bank = self.set_bank()
            user_budgets = self.set_budgets()
            user_type = "ANGEL"
            self._users.append(User(user_name, user_age, user_bank, user_budgets, user_type))
        except ValueError:
            print("Try again! Please enter the correct input types")
            return

    def increment_user_count(self):
        """
        Increments the user count
        """
        self.user_count += 1

    @staticmethod
    def set_budgets():
        """
        :return: a budget category
        """
        budget_names = [CategoryName.GAMES.value, CategoryName.CLOTHING.value, CategoryName.DINE.value,
                        CategoryName.MISC.value]
        budget_categories = {0: None, 1: None, 2: None, 3: None}

        for i in range(0, 4):
            print(f"\nThis is for budget {budget_names[i]:}")
            budget_limit = float(input("What is your budget limit? "))
            current_spent = float(input("How much was currently spent?"))
            budget_categories[i] = BudgetCategory(budget_names[i], budget_limit, False, current_spent, [])
        return budget_categories

    def options_menu(self, given_user):
        """
        The program's main menu
        :param given_user: current user
        :return: users selection
        """
        print(f"*** Current User is {given_user._user_name} ***\n")
        while True:
            print("Please choose from the following options")
            try:
                choice = int(input("1. View Budgets\n"
                                   "2. Record a Transaction\n"
                                   "3. View Transaction by Budget\n"
                                   "4. View Bank Account Details\n"
                                   "5. Go to Previous Menu\n"))
            except ValueError:
                print("Value should be of type integer")
            else:
                if choice == 1:
                    self.view_budget(given_user)
                elif choice == 2:
                    self.record_transaction(given_user)
                elif choice == 3:
                    self.view_transaction_budget(given_user)
                elif choice == 4:
                    self.view_bank_account_details(given_user)
                elif choice == 5:
                    print("--- Moving to previous menu ---")
                    break
                else:
                    print("Please choose an option within the given range of numbers")
        return choice

    def add_new_user(self, new_user):
        """
        :param new_user: Adds a new user to the users list
        """
        self._users.append(new_user)

    @staticmethod
    def budgets_menu():
        """
        :return: A Budget Choice
        """
        while True:
            try:
                category_choice = int(input("Please select a budget category: \n"
                                            " 1.Games and Entertainment\n"
                                            " 2.Clothing and Accessories\n"
                                            " 3.Eating Out\n"
                                            " 4.Miscellaneous\n"))
                break
            except ValueError:
                print("Input should be of the right format")
        return category_choice - 1

    @staticmethod
    def set_bank():
        """
        :return: Sets the user's bank details
        """
        while True:
            try:
                account_number = int(input("Enter the account number: "))
                bank_name = str(input("Enter bank name: "))
                balance = float(input("Enter balance: "))
                return Bank(account_number, bank_name, balance)
            except ValueError:
                print("Please enter in the correct input type")

    @staticmethod
    def view_budget(user):
        """
        Prints budgets of users
        :param user: a User object
        """
        for i in range(0, 4):
            print(user._budget[i])

    def record_transaction(self, user_obj):
        """
        Records a transaction info from the user
        """
        while True:
            try:
                transaction_amount = float(input("Please Enter the transaction amount: "))
                transaction_location = str(input("Please Enter the name of the store: "))
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

                transaction_obj = Transaction(transaction_timestamp, transaction_amount, transaction_location,
                                              budget_name)
                budget_category._transactions.append(transaction_obj)
                return
            except ValueError:
                print("Could not record transaction. Please retry")
            except KeyError:
                print("Input should be within bounds!")

    def view_transaction_budget(self, user_obj):
        """
        Retrieves the existing transactions in a budget
        :param user_obj: Current program user
        """
        category_choice = self.budgets_menu()
        print(user_obj._budget[category_choice]._transactions)

    @staticmethod
    def print_all_budgets_transactions(user):
        """
        Displays the transactions in each budget category
        :param user: Current program user
        """
        for i in range(0, 4):
            print(f" - {user._budget[i]._category_name}")
            print(f"   {user._budget[i]._transactions}\n")

    def view_bank_account_details(self, user_obj):
        """
        Displays the users bank account details
        :param user_obj: Current program user
        """
        print("Bank details of the user are:")
        print(user_obj._bank_details)
        print("All transactions to date are:")
        self.print_all_budgets_transactions(user_obj)

    def start_program(self):
        """
        Program start up menu
        """
        print("------- Welcome to F.A.M -------\n")

        while True:
            print("1. Register a new User\n"
                  "2. Load existing users\n"
                  "3. Quit the program\n")
            try:
                user_input = int(input("Please choose between the given options: "))
            except ValueError:
                print("Enter the correct input type!")
            else:
                if user_input == 1:
                    self.register_user()
                elif user_input == 2:
                    self.add_new_user(User.load_test_user_1())
                    self.add_new_user(User.load_test_user_2())
                    self.add_new_user(User.load_test_user_3())
                    this_user = self.choose_a_user()
                    self.options_menu(this_user)
                elif user_input == 3:
                    print("Thank you for choosing F.A.M, we hope to see you soon!")
                    break

    def choose_a_user(self):
        """
        Allows the program user to either make a new user or select an existing one
        :return: selected user choice
        """
        print("Please choose a current user from the following users")
        for user in self._users:
            self.increment_user_count()
            print(f"{self.user_count}. {user._user_name}")
        user = int(input())
        self._current_user = self._users[user - 1]
        return self._current_user


def main():
    """
    Drives the program
    """
    user_menu = UserMenu()
    user_menu.start_program()


if __name__ == '__main__':
    main()
