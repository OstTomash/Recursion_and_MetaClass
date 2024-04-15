def recursive_reverse(string):
    if len(string) == 0:
        return string

    return recursive_reverse(string[1:]) + string[0]


print(recursive_reverse('hello'))
