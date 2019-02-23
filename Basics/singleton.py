class Single(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance


class SingletonClass(Single):
    pass


class UsualClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(f'Comparing two singleton classes {x == y}')

a = UsualClass()
b = UsualClass()
print(f'Comparing two regular classes {a == b}')

