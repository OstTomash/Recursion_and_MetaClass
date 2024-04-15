class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name


first_obj = Singleton('First')
second_obj = Singleton('Second')

print(id(first_obj) == id(second_obj))  # True
