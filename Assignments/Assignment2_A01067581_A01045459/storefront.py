# from inventory import HolidayEnum
from inventory import Toys, StuffedAnimals, Candy
from items_factory import ChristmasItemsFactory, HalloweenItemsFactory, EasterItemsFactory


class Store:

    def __init__(self):
        self._orders = []
        self._items = {}

    def receive_order(self, order):
        self._orders.append(order)

    # for every order in the orders list, it checks whether the quantity of the order
    # is bigger than the length of the list containing the item at the key value of the
    # dictionary being the product id. Else it removes the order quantity from the list.
    def update_inventory(self):
        for order in self._orders:
            if order._quantity > len(self._item[order._product_id]):
                for i in range(100):
                    self._items[order._product_id].append()
                    # Factory Item created inside append()#
            else:
                for j in range(order._quantity):
                    self._items[order._product_id].pop()

    # def simulate(self):
    #     for order in self._orders:
    #         self._products_dict[item.get_order_number()]

    @staticmethod
    def process_web_orders():
        pass

    @staticmethod
    def check_inventory():
        pass
