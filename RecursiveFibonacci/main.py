def recursive_fibonacci(n):
    if n <= 0:
        return "Wrong input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


print(recursive_fibonacci(10))
