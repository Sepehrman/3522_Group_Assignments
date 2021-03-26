from storefront import Store
from order_processor import OrderProcessor, Order
from items_factory import ItemsFactory


class UserMenu:

    def process_web_orders(self):
        pass

    def display_menu(self):
        print("------- Welcome to S&S store -------\n")
        store = Store()
        while True:
            print("1. Process Web Orders\n"
                  "2. Check Inventory\n"
                  "0. Exit\n")
            try:
                user_input = int(input("Please choose between the given options: "))
                if user_input == 1:
                    try:
                        filename = str(input("Please enter the file name: "))
                        order = OrderProcessor(filename)
                        order.load_file()
                        orders = order.create_orders()
                        for i in range(order.count_rows()):
                            print(next(orders))
                    except FileNotFoundError:
                        print("Please double check the filename")
                elif user_input == 2:
                    inventory = store.get_inventory()
                    for item in inventory:
                        quantity = inventory.get(item)
                        if quantity >=10:
                            print(f"{item}: In Stock ({quantity})")
                        elif quantity < 10 and quantity > 3:
                            print(f"{item}: Low ({quantity})")
                        elif quantity < 3 and quantity > 0:
                            print(f"{item}: Very Low ({quantity})")
                        else:
                            print(f"{item}: Out of Stock ({quantity})")
                elif user_input == 0:
                    store.daily_transaction_report()
                    break
            except ValueError:
                print("Enter the correct input type!")
            except KeyError:
                print("Entered key is not in bounds")


def main():
    user_menu = UserMenu()
    user_menu.display_menu()


if __name__ == '__main__':
    main()
