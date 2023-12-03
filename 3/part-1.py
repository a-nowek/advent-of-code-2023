from functools import reduce

import utils as u


# Conversion rules:
#   - None if the character is a "."
#   - int if the character is a digit
#   - "X" if the character is a "special character"
def create_matrix() -> list[list[str | int | None]]:
    matrix: list[list[str | int | None]] = []

    for line in u.read_input():
        horizontal: list[str | int | None] = []
        for char in line:
            if char == ".":
                horizontal.append(None)
            elif char.isdigit():
                horizontal.append(int(char))
            else:
                horizontal.append("X")

        matrix.append(horizontal)
    return matrix


def get_value_in_line(line: list[str | int | None], x: int) -> int:
    indexed_digits: list[tuple[int, int]] = []

    # # cover top and bottom
    if line[x] != None and line[x] != "X":
        indexed_digits.append((x, line[x]))

    # check left from center
    indexed_digits.extend(u.iterate_horizontaly(line, x - 1, -1))
    indexed_digits.extend(u.iterate_horizontaly(line, x + 1, 1))

    # parse to value
    values = u.transform_indexed_digits_to_values(indexed_digits)
    value = reduce(lambda acc, current: acc + current, values, 0)

    # return value
    return value


def get_value_for_spot(
    matrix: list[list[str | int | None]], spot: tuple[int, int]
) -> int:
    spot_total_value = 0

    x, y = spot

    for y_offset in range(y - 1, y + 2, 1):
        if y_offset < 0 or y_offset >= len(matrix):
            continue
        value = get_value_in_line(matrix[y_offset], x)
        spot_total_value += value

    return spot_total_value


def get_sum_of_spots(
    matrix: list[list[str | int | None]], spots: list[tuple[int, int]]
) -> int:
    total_sum = 0

    for spot in spots:
        spot_value = get_value_for_spot(matrix, spot)
        total_sum += spot_value

    return total_sum


def main():
    matrix = create_matrix()
    spots = u.get_special_spots(matrix)
    total_sum = get_sum_of_spots(matrix, spots)

    print("Total: " + str(total_sum))


if __name__ == "__main__":
    main()
