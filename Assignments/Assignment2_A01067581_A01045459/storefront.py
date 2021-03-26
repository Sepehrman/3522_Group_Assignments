# from inventory import HolidayEnum
from inventory import Toys, StuffedAnimals, Candy
# from items_factory import ChristmasItemsFactory, HalloweenItemsFactory, EasterItemsFactory
import pandas as pd


class Store:

    def __init__(self):
        self._orders = []
        self._items = {}
        self._item_name = {}

    def receive_order(self, order):
        self._orders.append(order)
            # For each order, it's making a key with the product id in the dictionary and
            # initializing an empty list to load product objects into.
        if order._product_id not in self._items:
            self._items[order._product_id] = []
            self._item_name[order._name] = 1
        self.update_inventory()

    # For every order in the orders list, it checks whether the quantity of the order
    # is bigger than the length of the list containing the item at the key value of the
    # dictionary being the product id. Else it removes the order quantity from the list.
    def update_inventory(self):
        for order in self._orders:
            if order._quantity > len(self._item[order._product_id]):
                for i in range(100):
                    self._items[order._product_id].append()
                    # Factory Item created inside append()#
                    self._item_name[order._name] += 1
            else:
                for j in range(order._quantity):
                    self._items[order._product_id].pop()
                    self._item_name[order._name] -= 1

    def get_inventory(self):
        return self._item_name

    def daily_transaction_report(self):
        file_name = pd.datetime.now().strftime("DTR_%d%m%Y_%I%M")
        timestamp = pd.datetime.now().strftime("%d-%m-%Y %I:%M")
        f = open(file_name, "x")
        f.write("HOLIDAY STORE - DAILY TRANSACTION REPORT (DTR)")
        f.write(timestamp)
        for order in self._orders:
            order.__repr__()

    @staticmethod
    def process_web_orders():
        pass

    @staticmethod
    def check_inventory():
        pass
