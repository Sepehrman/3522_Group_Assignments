from abc import abstractmethod, ABC

from inventory import Toys, StuffedAnimals, Candy, SantasWorkshop, RemoteControlledSpider, Reindeer, CandyCanes
from inventory import DancingSkeleton, EasterBunny, PumpkinCaramelToffee, RobotBunny, CremeEggs


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

    def create_toy(self, **kwargs) -> Toys:
        return SantasWorkshop(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimals:
        return Reindeer(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        return CandyCanes(**kwargs)


class HalloweenItemsFactory(ItemsFactory):

    def create_toy(self, **kwargs) -> Toys:
        return RemoteControlledSpider(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimals:
        return DancingSkeleton(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        return PumpkinCaramelToffee(**kwargs)


class EasterItemsFactory(ItemsFactory):

    def create_toy(self, **kwargs) -> Toys:
        return RobotBunny(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimals:
        return EasterBunny(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        return CremeEggs(**kwargs)
