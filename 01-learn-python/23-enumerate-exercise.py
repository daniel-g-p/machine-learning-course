enum = enumerate(range(0, 100, 2))

for index, value in enum:
    if value == 50:
        print(f"Index of \"50\": {index}")
