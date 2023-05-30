my_list = [number * 2 for number in range(1, 51) if number % 2 == 0]

original_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

my_dict = {key: value * 2 for key, value in original_dict.items()}

print(my_list)
print(my_dict)
