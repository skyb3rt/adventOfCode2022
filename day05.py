# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
from pathlib import Path
import os
import parse
from aocd import submit
from dotenv import load_dotenv

PUZZLE_FILE = "input/day05.txt"
YEAR = os.environ.get("YEAR")
DAY = 5


def get_puzzle(file) -> list:
    return Path(file).read_text(encoding='utf8').splitlines()


def get_crane_index(puzzle: list) -> int:
    return [puzzle.index(l) for l in puzzle if l.strip().startswith("1")].pop()


def get_crane_startvaules(crane_index: int, puzzle: list) -> list:
    crane_count = max((int(l.strip())
                      for l in puzzle[crane_index].split("   ")))
    crane = [[] for _ in range(crane_count)]
    puzzle_crane = [l.replace("    ", " ").split(" ")
                    for l in puzzle[:crane_index]]
    for i in range(crane_index):
        for j in range(crane_count):
            line = puzzle_crane[i][j]
            if line:
                crane[j].append(line)
    return crane


def get_crane_moves(puzzle: list):
    return (parse.search("move {move:d} from {from:d} to {to:d}", line).named
            for line in puzzle if line.startswith("move"))


def move_crates_9000(crane: list, puzzle_crate_moves):
    # CrateMover 9000 moves one crate
    for move in puzzle_crate_moves:
        nr_of_crates = move["move"]
        from_crate = move["from"]-1
        to_crate = move["to"]-1
        for _ in range(nr_of_crates):
            crate = crane[from_crate][0]
            del crane[from_crate][0]
            crane[to_crate].insert(0, crate)
    return crane


def move_crates_9001(crane: list, puzzle_crate_moves):
    # CrateMover 9001 moves multiple crates at once
    for move in puzzle_crate_moves:
        nr_of_crates = move["move"]
        from_crate = move["from"]-1
        to_crate = move["to"]-1
        crate = crane[from_crate][0:nr_of_crates]
        del crane[from_crate][0:nr_of_crates]
        crane[to_crate] = crate+crane[to_crate]
    return crane


def part1(puzzle):
    crane_index = get_crane_index(puzzle)
    crane = get_crane_startvaules(crane_index, puzzle)
    crane_moves = get_crane_moves(puzzle)
    crane = move_crates_9000(crane, crane_moves)
    return ("".join((i[0].replace("[", "").replace("]", "") for i in crane)))


def part2(puzzle):
    crane_index = get_crane_index(puzzle)
    crane = get_crane_startvaules(crane_index, puzzle)
    crane_moves = get_crane_moves(puzzle)
    crane = move_crates_9001(crane, crane_moves)
    return ("".join((i[0].replace("[", "").replace("]", "") for i in crane)))


if __name__ == '__main__':
    load_dotenv()
    puzzle_input = get_puzzle(PUZZLE_FILE)
    submit(part1(puzzle_input), part="a", day=DAY, year=YEAR)
    submit(part2(puzzle_input), part="b", day=DAY, year=YEAR)
