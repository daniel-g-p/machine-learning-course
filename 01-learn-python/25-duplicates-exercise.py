my_list = ["a", "b", "c", "d", "e", "a", "c", "a"]

unique_items = set(my_list)

duplicate_items = []

for item in unique_items:
    is_duplicate = my_list.count(item) > 1
    if is_duplicate:
        duplicate_items.append(item)

print(duplicate_items)
