from abc import ABCMeta, abstractmethod


class Animal:
    ...


class Cat(Animal):
    ...


class ZooInterface(metaclass=ABCMeta):
    @abstractmethod
    def random_walk(self) -> Animal:
        ...


class CatOnlyZoo(ZooInterface):
    def random_walk(self) -> Cat:
        # return Animal()  # Incompatible return value type (got "Animal", expected "Cat")
        return Cat()


class CatCageInterface(metaclass=ABCMeta):
    @abstractmethod
    def put_in(self, cat: Cat) -> None:
        ...


class VeryHugeCatCage(CatCageInterface):
    def put_in(self, any_animal: Animal) -> None:
        ...
