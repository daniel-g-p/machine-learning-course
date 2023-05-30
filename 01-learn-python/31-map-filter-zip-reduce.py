from functools import reduce


def multiply_a_by_x(a=0, x=0):
    return a * x


def multiply_a_by_2(a=0):
    return multiply_a_by_x(a, 2)


output_map = list(map(multiply_a_by_2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(output_map)


def is_odd(number: int):
    return not number % 2 == 0


output_filter = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(output_filter)


def multiply(initial=1, value=1):
    return initial * value


output_reduce = reduce(multiply, [1, 2, 3, 4, 5, 6], 1)

print(output_reduce)
