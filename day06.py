# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=duplicate-code
from pathlib import Path
import os
from aocd import submit
from dotenv import load_dotenv

YEAR = os.environ.get("YEAR")
PUZZLE_FILE = "input/day06.txt"
DAY = 6


def find_unique(puzzle, nr_of_unique):
    forrige = []
    for i, bokstav in enumerate(puzzle, start=1):
        while bokstav in forrige:
            forrige = forrige[1:]
        forrige.append(bokstav)
        if len(forrige) == nr_of_unique:
            return i


def get_puzzle(file) -> list:
    return Path(file).read_text(encoding='utf8')


def part1(puzzle):
    return find_unique(puzzle, 4)


def part2(puzzle):
    return find_unique(puzzle, 14)


if __name__ == '__main__':
    load_dotenv()
    puzzle_input = get_puzzle(PUZZLE_FILE)
    submit(part1(puzzle_input), part="a", day=DAY, year=YEAR)
    submit(part2(puzzle_input), part="b", day=DAY, year=YEAR)
