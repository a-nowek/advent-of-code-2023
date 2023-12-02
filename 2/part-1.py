import utils as u


cubes_in_bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def validate_sets(sets_as_string: str):
    # I just wanted to use a try...except block
    try:
        for set in sets_as_string.split(";"):
            for cube_value in set.split(","):
                [showed, color] = u.parse_cube_input(cube_value)

                if cubes_in_bag[color] < showed:
                    raise Exception("Impossible combination")
        return True

    except:
        return False


def parse_game_input(game_input: str) -> int | None:
    [heading, sets_as_string] = game_input.split(": ")

    game_id = u.extract_game_id(heading)
    is_valid = validate_sets(sets_as_string)

    if is_valid:
        return game_id
    else:
        return None


def main():
    games = u.read_games_as_list()
    total_result = 0
    for game in games:
        game_result = parse_game_input(game)

        u.pretty_print_result(game, game_result)
        if game_result is None:
            continue

        total_result += game_result

    print(total_result)


if __name__ == "__main__":
    main()
