def highest_even(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    for number in sorted_numbers:
        is_number = type(number) in {int, float}
        if not is_number:
            break
        is_even = number % 2 == 0
        if is_even:
            return number
    else:
        return None


print(highest_even([10, 2, 3, 4, 84, 11, 15, 7]))
