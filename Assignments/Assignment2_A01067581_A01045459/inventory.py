from enum import Enum
from abc import abstractmethod, ABC


class HolidayEnum(Enum):
    CHRISTMAS = "Christmas"
    HALLOWEEN = "Halloween"
    EASTER = "Easter"


class InventoryEnum(Enum):
    TOY = "Toy"
    CANDY = "Candy"
    STUFFED_ANIMAL = "Stuffed Animal"


class Toys:
    def __init__(self, name, description, product_id, min_age, has_batteries):
        self._name = name
        self._description = description
        self._min_age = min_age
        self._has_batteries = has_batteries
        self._product_id = product_id


class SantasWorkshop(Toys):

    def __init__(self, name, description, product_id, min_age, has_batteries, dimensions, num_rooms, **kwargs):
        super().__init__(name, description, product_id, min_age, has_batteries)
        self._dimensions = dimensions
        self._num_rooms = num_rooms


class SpiderTypes(Enum):
    TARANTULA = "Tarantula"
    WOLF_SPIDER = "Wolf Spider"


class RemoteControlledSpider(Toys):
    def __init__(self, name, description, product_id, min_age, has_batteries, speed, jump_height,
                 has_glow, spider_type):
        super().__init__(name, description, product_id, min_age, has_batteries)
        self._speed = speed
        self._jump_height = jump_height
        self._has_glow = has_glow
        self._spider_type = spider_type


class RobotBunnyColours(Enum):
    ORANGE = "Orange"
    BLUE = "Blue"
    PINK = "Pink"


class RobotBunny(Toys):

    def __init__(self, name, description, product_id, min_age, has_batteries, num_sound, colour):
        super().__init__(name, description, product_id, min_age, has_batteries)
        self._num_sound = num_sound
        self._colour = colour


class StuffingType(Enum):
    POLYESTER = "Polyester"
    FIBERFILL = "Fiberfill"
    WOOL = "Wool"


class Sizes(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class FabricType(Enum):
    LINEN = "Linen"
    COTTON = "Cotton"
    ACRYLIC = "Acrylic"


class StuffedAnimals(ABC):

    @abstractmethod
    def __init__(self, name, description, product_id, stuffing_type, size, fabric_type):
        self._name = name
        self._description = description
        self._stuffing_type = stuffing_type
        self._size = size
        self._fabric_type = fabric_type
        self._product_id = product_id


class DancingSkeleton(StuffedAnimals):
    def __init__(self, name, description, product_id, stuffing_type, size, fabric_type, has_glow):
        super().__init__(name, description, product_id, stuffing_type, size, fabric_type)
        self._has_glow = has_glow


class Reindeer(StuffedAnimals):
    def __init__(self, name, description, product_id, stuffing_type, size, fabric_type, has_glow):
        super().__init__(name, description, product_id, stuffing_type, size, fabric_type)
        # self._has_glow = has_glow
        self._has_glow = has_glow


class EasterBunnyColours(Enum):
    WHITE = "White"
    GREY = "Grey"
    PINK = "Pink"
    BLUE = "Blue"


class EasterBunny(StuffedAnimals):

    def __init__(self, name, description, product_id, stuffing_type, size, fabric_type, colour):
        super().__init__(name, description, product_id, stuffing_type, size, fabric_type)
        self._colour = colour


class Candy(ABC):

    @abstractmethod
    def __init__(self, name, description, product_id, has_nuts, has_lactose):
        self._name = name
        self._description = description
        self._product_id = product_id
        self._has_nuts = has_nuts
        self._has_lactose = has_lactose


class CaramelToffeeVariety(Enum):
    SEA_SALT = "Sea Salt"
    REGULAR = "Regular"


class CandyStripes(Enum):
    RED = "Red"
    GREEN = "Green"


class PumpkinCaramelToffee(Candy):
    def __init__(self, name, description, product_id, has_nuts, has_lactose, variety):
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self._variety = variety


class CandyCanes(Candy):
    def __init__(self, name, description, product_id, has_nuts, has_lactose, colour):
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self._colour = colour


class CremeEggs(Candy):
    def __init__(self, name, description, product_id, has_nuts, has_lactose, pack_size):
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self._pack_size = pack_size
