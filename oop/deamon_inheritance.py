class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("Calling method on BaseClass")
        BaseClass.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on LeftSubclass")
        LeftSubclass.num_base_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on RightSubclass")
        RightSubclass.num_base_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        Subclass.num_sub_calls += 1


def main():
    s = Subclass()
    s.call_me()


if __name__ == "__main__":
    main()