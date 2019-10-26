class Base:
    def move(self):
        print('move in Base')


class A(Base):
    pass

class B:
    def move(self):
        print('move in B')

class Child(A, B):
    pass;


def main():
    child = Child()
    child.move()

if __name__ == '__main__':
    main()