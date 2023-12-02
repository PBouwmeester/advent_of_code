from enum import Enum
from math import prod


class colors(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


max_cube_count = {colors.RED: 12, colors.GREEN: 13, colors.BLUE: 14}


def get_min_cube_count(game: str) -> dict[colors, int]:
    min_cube_count = {color: 0 for color in colors}
    rounds = game.split("; ")
    for round in rounds:
        colored_cubes = round.split(", ")
        for cubes in colored_cubes:
            amount, color = cubes.split(" ")
            min_cube_count[colors(color)] = max(
                min_cube_count[colors(color)], int(amount)
            )
    return min_cube_count


def check_valid_game(game: str) -> bool:
    min_cube_count = get_min_cube_count(game)
    for color in min_cube_count:
        if min_cube_count[color] > max_cube_count[color]:
            return False
    return True


def get_cube_power(game: str) -> int:
    min_cube_count = get_min_cube_count(game)
    return prod(values for values in min_cube_count.values())


def main():
    with open("input.txt", "r") as file:
        lines = [line for line in file.readlines()]

    index_sum = 0
    power_sum = 0
    for line in lines:
        index, game = line.strip("\n").removeprefix("Game ").split(": ")
        index_sum += int(index) * check_valid_game(game)
        power_sum += get_cube_power(game)
    print(f"The sum of ID's is {index_sum}")
    print(f"The sum of products is {power_sum}")


if __name__ == "__main__":
    main()
