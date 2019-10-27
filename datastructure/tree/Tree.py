from abc import ABC, abstractmethod


class Tree(ABC):
    class Position(ABC):
        @abstractmethod
        def element(self):
            raise NotImplementedError()

        @abstractmethod
        def __eq__(self, other):
            raise NotImplementedError()

        def __ne__(self, other):
            return not (self == other)

    @abstractmethod
    def root(self):
        raise NotImplementedError()

    @abstractmethod
    def parent(self, p):
        raise NotImplementedError()

    @abstractmethod
    def num_children(self, p):
        raise NotImplementedError()

    @abstractmethod
    def children(self, p):
        raise NotImplementedError()

    @abstractmethod
    def __len__(self):
        raise NotImplementedError()

    @abstractmethod
    def is_root(self, p):
        raise NotImplementedError()

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0
