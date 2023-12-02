from functools import reduce

import utils as u


def get_cubes_list(game_input: str) -> list[tuple[int, str]]:
    cubes_list: list[tuple[int, str]] = []
    [_, sets_as_string] = game_input.split(": ")

    for set in sets_as_string.split(";"):
        for cube_value in set.split(","):
            cubes_list.append(u.parse_cube_input(cube_value))

    return cubes_list


def get_game_power(cubes: list[tuple[int, str]]) -> int:
    cubes_storage: dict[str, int] = {}

    for cube in cubes:
        [showed, color] = cube

        if color not in cubes_storage:
            cubes_storage[color] = showed
        else:
            if cubes_storage[color] < showed:
                cubes_storage[color] = showed

    return reduce(lambda acc, current: acc * current, cubes_storage.values(), 0)


def main():
    games = u.read_games_as_list()
    total_power = 0

    for game in games:
        cubes = get_cubes_list(game)
        game_power = get_game_power(cubes)

        u.pretty_print_result(game, game_power)
        total_power += game_power

    print(total_power)


if __name__ == "__main__":
    main()
