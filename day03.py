# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
from pathlib import Path
import string

PUZZLE_FILE = "input/day03.txt"
PRIORITIES_LIST = " "+string.ascii_lowercase+string.ascii_uppercase


def get_puzzle(file) -> list:
    return Path(file).read_text(encoding='utf8').splitlines()


def split_rucksacks(rucksaks: list) -> list[list[str]]:
    return [[set(line[0:int(len(line)/2)]), set(line[int(len(line)/2):])] for line in rucksaks]


def get_common(rucksack_1: set, *rucksacks: set) -> str:
    return rucksack_1.intersection(*rucksacks).pop()


def get_priorities(caracter: str) -> int:
    return PRIORITIES_LIST.index(caracter)


def part1():
    puzzle = get_puzzle(PUZZLE_FILE)
    puzzle = split_rucksacks(puzzle)
    sum_puzzle = sum([get_priorities(get_common(x[0], x[1])) for x in puzzle])
    print(f"Sum part 1: {sum_puzzle}")


def part2():
    puzzle = get_puzzle(PUZZLE_FILE)
    puzzle = [set(x) for x in puzzle]
    totalt = 0
    for i in range(0, len(puzzle), 3):
        totalt += get_priorities(
            (get_common(puzzle[i], puzzle[i+1], puzzle[i+2])))
    print(f"Sum part 2: {totalt}")


if __name__ == '__main__':
    part1()
    part2()
