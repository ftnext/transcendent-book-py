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
