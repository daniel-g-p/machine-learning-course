picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

output = ""

for row in picture:
    pixels = list(enumerate(row))
    for index, pixel in pixels:
        output += "*" if pixel == 1 else " "
        if index == len(pixels) - 1:
            output += "\n"

print(output)
