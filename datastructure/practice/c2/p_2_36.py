import random


class Animal:

    def __init__(self, position=-1):
        self._position = position

    @staticmethod
    def create_animal(position):
        rand = random.randint(1, 3)
        if rand == 1:
            return Bear(position)
        elif rand == 2:
            return Fish(position)
        else:
            return None

    def next_pos(self, max_position):
        rand = random.randint(-1, 1)
        if rand == -1 and self._position == 0:
            return self._position
        elif rand == 1 and self._position == max_position:
            return self._position
        else:
            return self._position + rand

    def set_position(self, position):
        self._position = position


class Bear(Animal):
    def __repr__(self):
        return "B"

    def __eq__(self, other):
        return isinstance(other, Bear)


class Fish(Animal):
    def __repr__(self):
        return "F"

    def __eq__(self, other):
        return isinstance(other, Fish)


class River:
    def __init__(self, n):
        """Init the river with a length, randomly create animals"""
        self._animals = [Animal.create_animal(i) for i in range(n)]
        self._max_position = n - 1
        print("Animals: {}".format(self._animals))

    def move(self):
        new_positions = []
        for i, animal in enumerate(self._animals):
            if animal is not None:
                new_positions.append(animal.next_pos(self._max_position))
            else:
                new_positions.append(-1)

        print(new_positions)
        for i in range(self._max_position):
            if self.is_race(new_positions, i):
                pass


    @staticmethod
    def is_race(new_positions, i):
        return new_positions[i] == new_positions[i + 1]




if __name__ == '__main__':
    river = River(15)
    river.move()

