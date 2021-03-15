from abc import abstractmethod, ABC
from inventory import Toys, StuffedAnimals, Candy


class ItemsFactory(ABC):


    @abstractmethod
    def create_toy(self) -> Toys:
        pass

    @abstractmethod
    def create_stuffed_animal(self) -> StuffedAnimals:
        pass

    @abstractmethod
    def create_candy(self):
        pass


