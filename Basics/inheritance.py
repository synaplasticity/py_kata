from abc import ABC, abstractmethod


class Abstract(ABC):

    ''' init is pretty much useless as an instance of the abstract class
        cannot be created '''
    def __init__(self, a):
        self.a = a
        print(a)

    @abstractmethod
    def foo(self, x):
        self.x = x
        pass


class Concrete(Abstract):

    def __init__(self, y):
        super().__init__(y*2)
        self.y = y
        print(y)

    def foo(self, x, y):
        super().foo(x)
        self.y = y * 2

    def print_foo(self):
        print(f'y from concrete class is {self.y}')
        print(f'x from abstract class is {self.x}')
