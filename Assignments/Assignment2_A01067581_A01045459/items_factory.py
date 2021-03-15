from abc import abstractmethod, ABC
from inventory import Toys, StuffedAnimals, Candy, SatnasWorkshop, RemoteControlledSpider,



class ItemsFactory(ABC):

    @abstractmethod
    def create_toy(self) -> Toys:
        pass

    @abstractmethod
    def create_stuffed_animal(self) -> StuffedAnimals:
        pass

    @abstractmethod
    def create_candy(self) -> Candy:
        pass


class ChristmasItemsFactory(ItemsFactory):

    def create_toy(self) -> Toys:
        return SatnasWorkshop()

    def create_stuffed_animal(self) -> StuffedAnimals:
        return StuffedAnimals()

    def create_candy(self) -> Candy:
        return Candy()


