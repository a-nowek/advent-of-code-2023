def read_games_as_list():
    with open("input.txt", "r") as file:
        return file.read().splitlines()


def extract_game_id(heading: str):
    return int(heading.split(" ")[1])


def parse_cube_input(cube_input: str) -> tuple[int, str]:
    [showed, color] = cube_input.strip().split(" ")
    return (int(showed), color)


def pretty_print_result(game: str, result: any) -> None:
    print(game.split(": ")[0] + " | " + str(result))
