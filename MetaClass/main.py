class RenamingMetaClass(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}

        for attr_name, attr_value in attrs.items():
            if attr_name.startswith(f'_{name}'):
                attr_name_parts = attr_name.split('__')
                new_attrs_name = '__private_'.join(attr_name_parts)
                new_attrs[new_attrs_name] = attr_value
            else:
                new_attrs[attr_name] = attr_value

        return super().__new__(cls, name, bases, new_attrs)


class NewClass(metaclass=RenamingMetaClass):
    __id = '12345'
    __secret = 42
    some_attr = 'some_attr'


first_obj = NewClass()

print(dir(first_obj))
