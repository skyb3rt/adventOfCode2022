# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
from pathlib import Path

PUZZLE_FILE = "input/day04.txt"


def get_puzzle(file) -> list:
    return [line.split(",") for line in Path(file).read_text(encoding='utf8').splitlines()]


def unpack_assignment(pair: list):
    elv_1 = pair[0].split('-')
    elv_2 = pair[1].split('-')
    elv_1 = set(x for x in range(int(elv_1[0]), int(elv_1[1])+1))
    elv_2 = set(x for x in range(int(elv_2[0]), int(elv_2[1])+1))
    return [elv_1, elv_2]


def compaire_assignments(elv_1, elv_2):
    intersect = elv_1.intersection(elv_2)
    return intersect in (elv_1, elv_2)


def find_overlap(elv_1, elv_2):
    intersect = elv_1.intersection(elv_2)
    return bool(intersect)


def part1(puzzle_input):
    totalt = 0
    for item in puzzle_input:
        assignment = unpack_assignment(item)
        if compaire_assignments(assignment[0], assignment[1]):
            totalt += 1
    return totalt


def part2(puzzle_input):
    totalt = 0
    for item in puzzle_input:
        assignment = unpack_assignment(item)
        if find_overlap(assignment[0], assignment[1]):
            totalt += 1
    return totalt


if __name__ == "__main__":
    puzzle = get_puzzle(PUZZLE_FILE)
    print(f"part1: {part1(puzzle)}")
    print(f"part1: {part2(puzzle)}")
