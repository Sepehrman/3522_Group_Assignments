from user import User
from budget_category import BudgetCategory, CategoryName
from user_types import Angel, Rebel, TroubleMaker


class UserMenu:

    def __init__(self):
        self._users = []
        # self._current_user = self._users[0]

    def register_user(self):
        print("Please enter your child's information")
        user_name = str(input("Enter the name for your child: "))
        user_age = int(input("Enter the age of your child: "))
        user_account_number = int(input("Enter the account number of your child: "))
        user_bank_name = str(input("What is the name of your child's bank: "))
        user_balance = float(input("What balance is allocated to your child's bank: "))
        user_budgets = self.set_budgets()
        user_type = "ANGEL"
        (self._users).append(User(user_name, user_age, user_account_number
                                ,user_bank_name, user_balance, user_budgets, user_type))


    def set_budgets(self):
        budget_names = [CategoryName.GAMES.value, CategoryName.CLOTHING.value, CategoryName.DINE.value,
                        CategoryName.MISC.value]
        budget_categories = {0: None, 1: None, 2: None, 3: None}

        for i in range(0, 4):
            print(f"\nThis is for budget {budget_names[i]:}")
            budget_limit = float(input("What is your budget limit? "))
            current_spent = float(input("How much was currently spent?"))
            budget_categories[i] = BudgetCategory(budget_names[i], budget_limit, False, current_spent, [])

        return budget_categories

    def print_menu(self):
        choice = int(input("1. View Budgets\n"
                           "2. Record a Transaction\n"
                           "3. View Transaction by Budget\n"
                           "4. View Bank Account Details\n"
                           "0. Quit Program\n"))
        return choice

    def view_budget(self, user):
        for i in range(0, 3):
            user._budget[i].print_results()

    def record_selftransaction(self):
        pass

    def view_transaction_budget(self):
        pass

    def view_bank_account_details(self):
        pass


def main():
    print("------- Welcome to F.A.M -------")
    user_menu = UserMenu()
    user_menu.register_user()
    user_input = ''

    while user_input != 0:
        user_input = user_menu.print_menu()
        if user_input == 1:
            user_menu.view_budget(user_menu._users[0])
        elif user_input == 2:
            user_menu.record_selftransaction()
        elif user_input == 3:
            user_menu.view_transaction_budget()
        elif user_input == 4:
            user_menu.view_bank_account_details()
        else:
            print("Number should be in range 1-4")






    # print(user_budget[2])
    # print(user_budget[3].values())

    # user_menu.register_user()

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
