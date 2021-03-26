from inventory import HolidayEnum
from inventory import Toys, StuffedAnimals, Candy
from items_factory import ChristmasItemsFactory, HalloweenItemsFactory, EasterItemsFactory



class Store:

    def __init__(self):
        self._orders = {}
        self._products_dict = {
            "C1230" : ["objects"]
        }

        # self._items_factory = orders
        # print(self._items_factory)

    # def simulate(self):
    #     for order in self._orders:
    #         self._products_dict[item.get_order_number()]


    @staticmethod
    def process_web_orders():
        pass

    @staticmethod
    def check_inventory():
        pass


