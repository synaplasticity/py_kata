from abc import ABC, abstractmethod
import inspect


class Bird(ABC):

    @abstractmethod
    def call(self):
        pass


class Dove(Bird):

    def __str__(self):
        return "Dove"

    def call(self):
        print("Oot, oot, oot")

    def sing(self):
        print("Oot, la la, oot, la la, oot la, la")


class Pipit(Bird):

    def __str__(self):
        return "Pipit"
 
    def call(self):
        print("Twi, twi, twi")


d = Dove()
p = Pipit()

d.call()
p.call()


class BirdComp():

    def __init__(self, species):
        self.species = species

    def call(self):
        self.species.call()

    def sing(self):
        try:
            self.species.sing()
        except AttributeError:
            print(f'{self.species} does not {inspect.currentframe().f_code.co_name}')


d1 = BirdComp(Dove())
p1 = BirdComp(Pipit())
d1.call()
p1.call()

d1.sing()
p1.sing()  # will fail as it has no sing() attribute