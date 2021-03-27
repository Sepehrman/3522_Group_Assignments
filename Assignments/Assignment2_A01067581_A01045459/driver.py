from storefront import Store
from order_processor import OrderProcessor


class UserMenu:

    def __init__(self):
        self._store = Store()
        self._inventory = None
        self._web_orders = []

    def process_web_orders(self):
        try:
            filename = str(input("Please enter the file name: "))
            order = OrderProcessor(filename)
            order.load_file()
            orders = order.create_orders()
            for i in range(order.count_rows()):
                print(next(orders))
                self._store.receive_order(next(orders))
            print("Orders Processed!")
        except FileNotFoundError:
            print("Please double check the filename")

    def check_inventory(self):
        self._inventory = self._store.get_inventory()
        for item in self._inventory:
            quantity = self._inventory.get(item)
            if quantity >= 10:
                print(f"{item}: In Stock ({quantity})")
            elif quantity < 10 and quantity > 3:
                print(f"{item}: Low ({quantity})")
            elif quantity < 3 and quantity > 0:
                print(f"{item}: Very Low ({quantity})")
            else:
                print(f"{item}: Out of Stock ({quantity})")

    def display_menu(self):
        print("------- Welcome to S&S store -------\n")
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
