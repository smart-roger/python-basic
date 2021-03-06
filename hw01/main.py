from operator import pow
from time import time
from functools import wraps


def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"time_decorator for {func.__name__} with args {args}")
        start_time = time()
        res = func(*args, **kwargs)
        end_time = time()
        print(f"computed in {end_time - start_time} secs")
        return res

    return wrapper


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


@benchmark
def filter_list(input_list, filter_type):
    if filter_type == FILTER_ODD:
        return list(filter(lambda x: 1 == x % 2, input_list))
    elif filter_type == FILTER_EVEN:
        return list(filter(lambda x: 0 == x % 2, input_list))
    elif filter_type == FILTER_SIMPLE:
        return list(filter(is_simple, input_list))

    raise ValueError('Unknown filter type!')


test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("Demo func_power")
print("Power zero: ", func_power(test_input, power=0))
print("Power 1: ", func_power(test_input, power=1))
print("Squares: ", func_power(test_input))
print("Cubes: ", func_power(test_input, 3))

print("\n\nDemo filter_list (with benchmark decorator)")
print("Odd only: ", filter_list(range(0, 10000), FILTER_ODD), "\n")
print("Even only: ", filter_list(range(0, 10000), FILTER_EVEN), "\n")
print("Simple only: ", filter_list(range(0, 10000), FILTER_SIMPLE), "\n")


def trace(func):
    trace.level = 0
    trace.splitter = "----"

    @wraps(func)
    def wrapper(*args, **kwargs):
        trace.level += 1
        print(f" {trace.level * trace.splitter} call {func.__name__}({args[0]})")
        res = func(*args, **kwargs)
        trace.level -= 1
        return res

    return wrapper


@trace
def fib(n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(10))
