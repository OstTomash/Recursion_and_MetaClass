def recursive_dec_to_bin_converter(num):
    if num < 2:
        return num

    return int(f'{recursive_dec_to_bin_converter(num // 2)}' + f'{num % 2}')


print(recursive_dec_to_bin_converter(27))