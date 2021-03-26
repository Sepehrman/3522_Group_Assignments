import pandas as pd
from items_factory import ChristmasItemsFactory, HalloweenItemsFactory, EasterItemsFactory
from inventory import Toys, StuffedAnimals, Candy, HolidayEnum, InventoryEnum


class OrderProcessor:

    def __init__(self, filename):
        self._file_name = filename
        self._file_object = None
        self._counter = 0
        self._mapping_factory = None
        # print(self._factory)

    holiday_mapper = {
        HolidayEnum.CHRISTMAS.value: ChristmasItemsFactory,
        HolidayEnum.HALLOWEEN.value: HalloweenItemsFactory,
        HolidayEnum.EASTER.value: EasterItemsFactory
    }

    def get_factory(self, item_type: HolidayEnum):
        item_class = self.holiday_mapper.get(item_type)
        return item_class()

    def load_file(self):
        try:
            self._file_object = pd.read_excel(self._file_name, sheet_name="Sheet1")
        except FileNotFoundError:
            print("File does not exist ion current directory!")

    def get_row(self, num):
        return self._file_object.loc[num]

    def get_column(self, *args):
        return self._file_object[[*args]]

    def count_rows(self):
        return len(self._file_object.index)

    def create_orders(self):
        count = 0
        while count != self.count_rows():

            yield Order(**self.get_row(count))
            count += 1

    def __repr__(self):
        return f"{self._file_object}"


class Order:
    def __init__(self, order_number, product_id, item, name, **item_details: dict):
        self._order_number = order_number
        self._product_id = product_id
        self._item = item
        self._name = name
        self._item_type = self.get_item_type(item)
        self._quantity = item_details["quantity"]
        self._item_details = item_details
        # self._reference =
        print(self._item_details["holiday"])
        del self._item_details["holiday"]
        print(self._item)

    def get_order_number(self):
        return self._order_number


    @staticmethod
    def find_factory_category(holiday, item):
        pass

    @staticmethod
    def get_item_type(item_index):
        if item_index == InventoryEnum.TOY.value:
            return InventoryEnum.TOY
        elif item_index == InventoryEnum.CANDY.value:
            return InventoryEnum.CANDY
        else:
            return InventoryEnum.STUFFED_ANIMAL

    def __repr__(self):
        return f"Order {self._order_number}, Item {self._item}, Product ID {self._product_id}, Name {self._name}, " \
               f"Quantity {self._quantity}"
