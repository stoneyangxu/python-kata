from abc import ABC, abstractmethod
from collections import deque


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

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def positions(self):
        # return self.preorder()
        return self.postorder()

    def is_root(self, p):
        raise self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height(p)

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            return self._subtree_postorder(self.root())

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadfirst(self):
        if not self.is_empty():
            fringe = deque()
            fringe.append(self.root())

            while len(fringe) > 0:
                p = fringe.popleft()
                for c in self.children(p):
                    fringe.append(c)
