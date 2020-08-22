from operator import pow


def func_power(input_list, power=2):
    return list(map(pow, input_list, [power] * len(input_list)))


FILTER_ODD = 0
FILTER_EVEN = 1
FILTER_SIMPLE = 2


def is_simple(value):
    if value == 0:
        return False  # Zero is not simple number

    for test in range(2, value // 2 + 1):
        if 0 == value % test:
            return False
    return True


def filter_list(input_list, filter_type):
    if filter_type == FILTER_ODD:
        return list(filter(lambda x: 1 == x % 2, input_list))
    elif filter_type == FILTER_EVEN:
        return list(filter(lambda x: 0 == x % 2, input_list))
    elif filter_type == FILTER_SIMPLE:
        return list(filter(is_simple, input_list))

    raise ValueError('Unknown filter type!')


test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("Power zero: ", func_power(test_input, power=0))
print("Power 1: ", func_power(test_input, power=1))
print("Squares: ", func_power(test_input))
print("Cubes: ", func_power(test_input, 3))

print("Odd only: ", filter_list(test_input, FILTER_ODD))
print("Even only: ", filter_list(test_input, FILTER_EVEN))
print("Simple only: ", filter_list(test_input, FILTER_SIMPLE))
