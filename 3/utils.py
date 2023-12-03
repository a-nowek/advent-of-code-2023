from functools import reduce


def read_input() -> list[str]:
    with open("./3/input.txt", "r") as file:
        return file.read().splitlines()


def get_special_spots(matrix: list[list[str | int | None]]) -> list[tuple[int, int]]:
    spots: list[tuple[int, int]] = []

    for y, line in enumerate(matrix):
        for x, char in enumerate(line):
            if char == "X":
                spots.append((x, y))
    return spots


def iterate_horizontaly(line: list[str | int | None], start: int, change: int):
    digits_with_position: list[tuple[int, int]] = []
    offset = start

    while True:
        if offset < 0 or offset >= len(line):
            break
        match line[offset]:
            case None:
                break
            case "X":
                break
            case digit:
                digits_with_position.append((offset, digit))
                offset += change

    return digits_with_position


def parse_to_integers(values: list[int], value: str) -> list[int]:
    values.append(int(value))
    return values


def transform_indexed_digits_to_values(
    index_digits: list[tuple[int, int]]
) -> list[int]:
    values_as_text: list[str] = []

    sorted_digits_with_position = sorted(index_digits, key=lambda item: item[0])
    prev_index, series_count = None, 0

    for [index, value] in sorted_digits_with_position:
        if prev_index is None:
            values_as_text.append(str(value))
        elif prev_index == index - 1:
            values_as_text[series_count] += str(value)
        else:
            series_count += 1
            values_as_text.append(str(value))

        prev_index = index

    return reduce(parse_to_integers, values_as_text, [])
