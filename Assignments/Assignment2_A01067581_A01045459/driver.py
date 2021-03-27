from store_front import Store
from order_processor import OrderProcessor


class UserMenu:
    """
    A User Menu class responsible for simulating a holiday items factory
    """
    def __init__(self):
        self._store = Store()
        self._inventory = None
        self._web_orders = []

    def process_web_orders(self):
        """
        Processes all the web orders
        """
        try:
            filename = str(input("Please enter the file name: "))
            order = OrderProcessor(filename)
            order.load_file()
            orders = order.create_orders()
            for i in range(order.count_rows()):
                self._store.receive_order(next(orders))
            print("Orders Processed!")
        except FileNotFoundError:
            print("Please double check the filename")
        except TypeError:
            print("Please double check the filename")

    def check_inventory(self):
        """
        Checks all the inventory items
        """
        self._inventory = self._store.get_inventory()
        for item in self._inventory:
            quantity = self._inventory.get(item)
            if quantity >= 10:
                print(f"{item}: In Stock ({quantity})")
            elif 10 > quantity > 3:
                print(f"{item}: Low ({quantity})")
            elif 3 > quantity > 0:
                print(f"{item}: Very Low ({quantity})")
            else:
                print(f"{item}: Out of Stock ({quantity})")

    def display_menu(self):
        """
        Display the menu and all its options
        """
        print("------- Welcome to S&S Holiday store -------\n")
        while True:
            print("1. Process Web Orders\n"
                  "2. Check Inventory\n"
                  "0. Exit\n")
            try:
                user_input = int(input("Please choose between the given options: "))
                if user_input == 1:
                    self.process_web_orders()
                elif user_input == 2:
                    self.check_inventory()
                elif user_input == 0:
                    self._store.daily_transaction_report()
                    break
            except ValueError:
                print("Enter the correct input type!")


def main():
    user_menu = UserMenu()
    user_menu.display_menu()


if __name__ == '__main__':
    main()
