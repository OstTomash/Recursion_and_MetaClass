class SimpleMetaClass(type):
    def __new__(cls, name, bases, attrs):
        print(f"New class with name {name} was created")
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)


class SimpleClass(metaclass=SimpleMetaClass):
    pass
