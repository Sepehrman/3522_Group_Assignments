import string
from enum import Enum
from random import random


class InventoryEnum(Enum):
    TOYS = 0
    STUFFED_ANIMALS = 1
    CANDY = 2


class Toys:
    def __init__(self, name, description, product_id, min_age, is_battery_operated):
        self._name = name
        self._description = description
        self._min_age = min_age
        self._is_battery_operated = is_battery_operated
        self._product_id = product_id

    # def generate_id(self):
    #     return ''.join(random.choices(string.ascii_letters + string.digits, 4))


class SatnasWorkshop(Toys):

    def __init__(self, width, height, num_rooms):
        ########## IF NO AGE MENTIONED, THEN NONE????? ############
        super().__init__("Santa's Workshop", "The premium Christmas present, this is not a battery operated toy. "
                                             "The doll house comes in different varieties.", "A0123", None, False)
        self._width = width
        self._height = height
        self._num_rooms = num_rooms


class SpiderTypes(Enum):
    TARANTULA = "Tarantula"
    WOLF_SPIDER = "Wolf Spider"


class RemoteControlledSpider(Toys):
    def __init__(self, speed, jump_height, can_glow, spider_type):
        super().__init__("Remote Controlled Spider", "The RC Spider is the toy to get during Halloween. "
                                                     "This toy is battery operated.", "asfa", None, True)
        self._speed = speed
        self._jump_height = jump_height
        self._can_glow = can_glow
        self._spider_type = spider_type


class RobotBunnyColours(Enum):
    ORANGE = "Orange"
    BLUE = "Blue"
    PINK = "Pink"


class RobotBunny(Toys):
    def __init__(self, num_sound_effects, colour):
        super().__init__("Robot Bunny", "The Robot Bunny is the toy for toddlers and infants out there. "
                                        "The toy is battery operated. These come in different varieties as well!"
                         , "123525sa", 0, True)
        self._num_sound_effects = num_sound_effects
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


class StuffedAnimals:

    def __init__(self, name, description , product_id, stuffing_type, size, fabric_type):
        self._name = name
        self._description = description
        self._stuffing_type = stuffing_type
        self._size = size
        self._fabric_type = fabric_type
        self._product_id = product_id


class DancingSkeleton(StuffedAnimals):

    def __init__(self, ):
        super().__init__("Dancing Skeleton", "The dancing skeleton is made out of Acrylic yarn and "
                                             "stuffed with Polyester Fiberfill. "
                                             "This skeleton is sure to add to your Halloween decorations."
                         , "A1245", StuffingType.POLYESTER, Sizes.MEDIUM, FabricType.ACRYLIC)
        glows = True

class Reindeer(StuffedAnimals):

    def __int__(self):
        super().__init__("Reindeer", "The reindeer comes with its very own personal mini sleigh and is the stuffed"
                                     " animal for Christmas. It is made out of Cotton and and stuffed with Wool."
                         , "asfhjh", StuffingType.WOOL, Sizes.SMALL, FabricType.COTTON)
        glows = True


class EasterBunnyColours(Enum):
    WHITE = "White"
    GREY = "Grey"
    PINK = "Pink"
    BLUE = "Blue"


class EasterBunny(StuffedAnimals):

    def __init__(self):
        super().__init__("Easter Bunny", "AA242", "The Easter Bunny is made out of Linen and stuffed with Polyester Fiberfill.",
                         StuffingType.POLYESTER, Sizes.MEDIUM, FabricType.LINEN)
        colors = EasterBunnyColours


class Candy:

    def __init__(self, name, description, product_id, contains_nuts, is_lactose_free):
        self._name = name
        self._description = description
        self._product_id = product_id
        self._contains_nuts = contains_nuts
        self._is_lactose_free = is_lactose_free


class CaramelToffeeVariety(Enum):
    SEA_SALT = "Sea Salt"
    REGULAR = "Regular"

class CandyStripes(Enum):
    RED = "Red"
    GREEN = "Green"

class PumpkinCaramelToffee(Candy):
    def __init__(self, variety_type):
        super().__init__("Pumpkin Caramel Toffee", "The Pumpkin Caramel Toffee is Halloween themed and is not lactose "
                                                   "free and may contain traces of nuts.", "PMPKN123",
                         True, False)
        variety_type = CaramelToffeeVariety

class CandyCanes(Candy):
    def __init__(self):
        super().__init__("Candy Canes", "Candy Canes are Christmas themed. It is lactose free "
                                        "and does not contain nuts.", "CANE1234", False, False)
        Stripes = CandyStripes



class CremeEggs(Candy):
    def __init__(self):
        super().__init__("Creme Eggs", "Creme Eggs are Easter themed and are not lactose free and may "
                                       "contain traces of nuts.", "CRMEGG125", True, True)
        



