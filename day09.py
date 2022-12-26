# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
from pathlib import Path
import os
import parse
from aocd import submit
from dotenv import load_dotenv


YEAR = os.environ.get("YEAR")
PUZZLE_FILE = "input/day09.txt"
DAY = 9


def get_puzzle(file) -> list:
    return Path(file).read_text(encoding='utf8').splitlines()


class Bridge:

    def __init__(self, length) -> None:
        self.start = [10, 0]
        self.rope = [[10, 0] for _ in range(length)]
        self.tail_visit = []

    def get_tail_visit(self):
        return len(list(self.tail_visit))

    def move(self, direction, magnitude: int):
        for _ in range(magnitude):

            match direction:
                case "R":
                    self.rope[-1][1] += 1
                case "L":
                    self.rope[-1][1] -= 1
                case "U":
                    self.rope[-1][0] -= 1
                case "D":
                    self.rope[-1][0] += 1
            self.move_tail()
            if self.rope[0] not in self.tail_visit:
                self.tail_visit.append(self.rope[0][:])

    def move_tail(self):
        for i in range(-2, -len(self.rope)-1, -1):
            diff_vertical = self.rope[i+1][0] - self.rope[i][0]
            diff_horizontal = self.rope[i+1][1] - self.rope[i][1]
            if abs(diff_horizontal) == 2:
                self.rope[i][1] += 1 if diff_horizontal > 0 else -1
                self.rope[i][0] += 1 if diff_vertical > 0 else - \
                    1 if diff_vertical < 0 else 0
            elif abs(diff_vertical) == 2:
                self.rope[i][0] += 1 if diff_vertical > 0 else -1
                self.rope[i][1] += 1 if diff_horizontal > 0 else - \
                    1 if diff_horizontal < 0 else 0


def part1(puzzle):
    bridge = Bridge(2)
    for line in puzzle:
        result = parse.search("{direction:l} {magnitude:d}", line).named
        bridge.move(result["direction"], result["magnitude"])
    return bridge.get_tail_visit()


def part2(puzzle):
    bridge = Bridge(10)
    for line in puzzle:
        result = parse.search("{direction:l} {magnitude:d}", line).named
        bridge.move(result["direction"], result["magnitude"])
    return bridge.get_tail_visit()


if __name__ == '__main__':
    load_dotenv()
    puzzle_input = get_puzzle(PUZZLE_FILE)
    RESULT_PART1 = part1(puzzle_input)
    RESULT_PART2 = part2(puzzle_input)
    print(f"part_1: {RESULT_PART1}")
    print(f"part_2: {RESULT_PART2}")
    ready = input("submit [1,2]?")
    if ready == "1":
        submit(RESULT_PART1, part="a", day=DAY, year=YEAR)
        # 6284 riktig!
    if ready == "2":
        # 2661
        submit(RESULT_PART2, part="b", day=DAY, year=YEAR)
