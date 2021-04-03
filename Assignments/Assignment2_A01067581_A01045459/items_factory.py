from abc import abstractmethod, ABC

from inventory import Toys, StuffedAnimals, Candy, SantasWorkshop, RemoteControlledSpider, Reindeer, CandyCanes
from inventory import DancingSkeleton, EasterBunny, PumpkinCaramelToffee, RobotBunny, CremeEggs


class ItemsFactory(ABC):
    """
    The base factory class responsible for creating factory items
    """

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
        """
        :return: a SantasWorkshop Toy
        """
        return SantasWorkshop(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimals:
        """
        :return: a Reindeer StuffedAnimal
        """
        return Reindeer(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        """
        :return: a CandyCane Candy
        """
        return CandyCanes(**kwargs)


class HalloweenItemsFactory(ItemsFactory):

    def create_toy(self, **kwargs) -> Toys:
        """
        :return: a RemoteControlledSpider Toy
        """
        return RemoteControlledSpider(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimals:
        """
        :return: a DancingSkeleton StuffedAnimals
        """
        return DancingSkeleton(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        """
        :return: a PumpkinCaramelToffee Candy
        """
        return PumpkinCaramelToffee(**kwargs)


class EasterItemsFactory(ItemsFactory):

    def create_toy(self, **kwargs) -> Toys:
        """
        :return: a RobotBunny Toy
        """
        return RobotBunny(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimals:
        """
        :return: a EasterBunny StuffedAnimal
        """
        return EasterBunny(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        """
        :return: a CremeEggs Candy
        """
        return CremeEggs(**kwargs)
