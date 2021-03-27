import pandas as pd
from items_factory import ChristmasItemsFactory, HalloweenItemsFactory, EasterItemsFactory
from inventory import InventoryEnum, HolidayEnum


class OrderProcessor:

    def __init__(self, filename):
        self._file_name = filename
        self._file_object = None
        self._counter = 0
        self._mapping_factory = None

    def load_file(self):
        """
        Load an excel file onto the current working file
        :return:
        """
        try:
            self._file_object = pd.read_excel(self._file_name, sheet_name="Sheet1")
        except FileNotFoundError:
            print("File does not exist ion current directory!")

    def get_row(self, num):
        """
        :param num: an Integer
        :return: a Row Number
        """
        return self._file_object.loc[num]

    def get_column(self, *args):
        """
        :param args: a set of arguments
        :return: the column number
        """
        return self._file_object[[*args]]

    def count_rows(self):
        """
        :return: the number of the rows of the excel file
        """
        try:
            return len(self._file_object.index)
        except AttributeError:
            print("**** Error accessing *****\n")

    def create_orders(self):
        """
        :return: An order object
        """
        count = 0
        while count != self.count_rows():
            yield Order(**self.get_row(count))
            count += 1

    def __repr__(self):
        """
        :return: a String representation of the file object
        """
        return f"{self._file_object}"


class Order:
    """
    An Order Object with details
    """

    def __init__(self, **item_details):
        self._order_number = item_details['order_number']
        self._product_id = item_details['product_id']
        self._item = item_details['item']
        self._name = item_details['name']
        self._item_type = self.get_item_type(self._item)
        self._quantity = item_details["quantity"]
        self._item_details = item_details
        self._holiday = item_details.get('holiday')
        self._factory_object = self.get_factory(self._holiday)

    holiday_mapper = {
        HolidayEnum.CHRISTMAS.value: ChristmasItemsFactory,
        HolidayEnum.HALLOWEEN.value: HalloweenItemsFactory,
        HolidayEnum.EASTER.value: EasterItemsFactory
    }

    def get_object_details(self):
        """
        :return: order details
        """
        return self._item_details

    def get_factory(self, item_type):
        """
        :param item_type: an Enum
        :return: a HolidayClass
        """
        item_class = self.holiday_mapper.get(item_type)
        return item_class()

    def get_type(self):
        """
        :return: item Type
        """
        return self._item

    def get_item_factory_holiday(self):
        """
        :return: factory object
        """
        return self._factory_object

    def get_order_number(self):
        """
        :return: an Order Number
        """
        return self._order_number

    def get_name(self):
        """
        :return: a Name
        """
        return self._name

    def get_quantity(self):
        """
        :return: a Quantity
        """
        return self._quantity

    def get_product_id(self):
        """
        :return: a product id
        """
        return self._product_id

    @staticmethod
    def get_item_type(item_index):
        """
        :param item_index: an item type
        :return: an Inventory Item
        """
        if item_index == InventoryEnum.TOY.value:
            return InventoryEnum.TOY
        elif item_index == InventoryEnum.CANDY.value:
            return InventoryEnum.CANDY
        else:
            return InventoryEnum.STUFFED_ANIMAL

    def __repr__(self):
        """
        :return: a String Representation of Order
        """
        return f"Order {self._order_number}, Item {self._item}, Product ID {self._product_id}, Name \"{self._name}\", "\
               f"Quantity {self._quantity}"
