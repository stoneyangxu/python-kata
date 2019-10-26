from abc import ABC, abstractproperty, abstractmethod

class AbstractClass(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def hello(self):
        pass


class Person(AbstractClass):

    @property
    def name(self):
        return "YangXu"

    def hello(self):
        print('{} say hello'.format(self.name))


def main():
    obj = Person()
    obj.hello()


if __name__ == "__main__":
    main()