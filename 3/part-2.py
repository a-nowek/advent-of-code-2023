from functools import reduce

import utils as u


# Conversion rules:
#   - None if the character is not a digit or an "*"
#   - int if the character is a digit
#   - "X" if the character is an "*"
def create_matrix() -> list[list[str | int | None]]:
    matrix: list[list[str | int | None]] = []

    for line in u.read_input():
        horizontal: list[str | int | None] = []
        for char in line:
            if char.isdigit():
                horizontal.append(int(char))
            elif char == "*":
                horizontal.append("X")
            else:
                horizontal.append(None)

        matrix.append(horizontal)
    return matrix


def get_value_in_line(line: list[str | int | None], x: int) -> list[int]:
    indexed_digits: list[tuple[int, int]] = []

    # # cover top and bottom
    if line[x] != None and line[x] != "X":
        indexed_digits.append((x, line[x]))

    # check left from center
    indexed_digits.extend(u.iterate_horizontaly(line, x - 1, -1))
    indexed_digits.extend(u.iterate_horizontaly(line, x + 1, 1))

    # parse to integers
    values = u.transform_indexed_digits_to_values(indexed_digits)

    # return values
    return values


def get_value_for_spot(
    matrix: list[list[str | int | None]], spot: tuple[int, int]
) -> int:
    spot_values: list[int] = []

    x, y = spot

    for y_offset in range(y - 1, y + 2, 1):
        if y_offset < 0 or y_offset >= len(matrix):
            continue
        spot_values.extend(get_value_in_line(matrix[y_offset], x))

    if len(spot_values) != 2:
        return 0

    return spot_values[0] * spot_values[1]


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
