def my_sum(numbers: list):
    '''Sum up the provided array of numbers'''
    total = 0
    for number in numbers:
        is_valid = type(number) in {int, float}
        total += number if is_valid else 0
    return total


def super_sum(*args, **kwargs):
    return my_sum(args) + my_sum(kwargs.values())


print(super_sum(1, 2, 3, 4, 5, num6=6, num7=7))
