def recursive_sum(num):
    if num < 10:
        return num

    return (num % 10) + recursive_sum(num // 10)


print(recursive_sum(58556))
