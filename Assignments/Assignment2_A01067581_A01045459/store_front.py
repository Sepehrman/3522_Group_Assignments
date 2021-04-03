import datetime
from inventory import InventoryEnum


class Store:
    """
    A Store class
    """
    def __init__(self):
        self._orders = []
        self._items = {}
        self._item_name = {}

    def receive_order(self, order):
        """
        :param order: an Order object
        """
        self._orders.append(order)
        if order.get_product_id() not in self._items:
            self._items[order.get_product_id()] = []
            self._item_name[order.get_name()] = 1
        self.update_inventory()

    def update_inventory(self):
        """
        Update the current inventory with new orders being created by the factory method
        """
        for order in self._orders:
            if order.get_quantity() > len(self._items[order.get_product_id()]):
                factory_class = order.get_item_factory_holiday()
                object_details = order.get_object_details()
                for i in range(100):
                    if order.get_type() == InventoryEnum.TOY.value:
                        self._items[order.get_product_id()].append(factory_class.create_toy(**object_details))
                    elif order.get_type() == InventoryEnum.STUFFED_ANIMAL.value:
                        self._items[order.get_product_id()]\
                            .append(factory_class.create_stuffed_animal(**object_details))
                    else:
                        self._items[order.get_product_id()].append(factory_class.create_candy(**object_details))
                    self._item_name[order.get_name()] += 1
            else:
                for j in range(order.get_quantity()):
                    self._items[order.get_product_id()].pop()
                    self._item_name[order.get_name()] -= 1

    def get_inventory(self):
        """
        :return: item name
        """
        return self._item_name

    def daily_transaction_report(self):
        """
        Upon program exit, record all transaction details onto a file
        """
        time_now = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        file_name = datetime.datetime.now().strftime("%d%m%y_%H%M")
        with open(f"DTR_{file_name}.txt", mode='w', encoding='utf-8') as my_text_file:
            my_text_file.write(f"HOLIDAY STORE - DAILY TRANSACTION REPORT (DTR)\n")
            my_text_file.write(f"{time_now}\n")
            for order in self._orders:
                my_text_file.write(f"{order}\n")
