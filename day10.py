# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
from pathlib import Path
import os
from aocd import submit
from dotenv import load_dotenv

YEAR = os.environ.get("YEAR")
PUZZLE_FILE = "input/day10.txt"
DAY = 10


def get_puzzle(file) -> list:
    return Path(file).read_text(encoding='utf8').splitlines()


class Cpu():
    def __init__(self):
        self.register_x = 1  # register
        self.cycles = 0
        self.signal = 0
        self.screen_lines = []
        self.screen_line_position = 0
        self.sprite = "###....................................."

    def noop(self):
        self.cycles += 1
        if self.cycles == 20:
            self.signal += self.register_x*self.cycles
        elif (self.cycles-20) % 40 == 0:
            self.signal += self.register_x*self.cycles
        self.update_screen()

    def update_screen(self):
        self.screen_lines.append(self.sprite[self.screen_line_position])
        if self.screen_line_position == 39:
            print("".join(self.screen_lines))
            self.screen_lines = []
            self.screen_line_position = 0
        else:
            self.screen_line_position += 1

    def addx(self, value):
        self.register_x += value

    def update_sprite(self):
        dot = "###" if self.register_x >= 1 else "#"*(self.register_x+2)
        self.sprite = "."*(self.register_x-1)+dot+"."*(40-self.register_x-2)

    def execute(self, program):
        for line in program:
            match line:
                case "noop":
                    self.noop()
                case _:
                    self.noop()
                    self.noop()
                    value = int(line.split(" ")[1])
                    self.addx(value)
                    self.update_sprite()


def part1(puzzle):
    cpu = Cpu()
    cpu.execute(puzzle)
    return cpu.signal


if __name__ == '__main__':
    load_dotenv()
    puzzle_input = get_puzzle(PUZZLE_FILE)
    RESULT_PART1 = part1(puzzle_input)
    print(f"part_1: {RESULT_PART1}")
    ready = input("submit [1,2]?")
    if ready == "1":
        submit(RESULT_PART1, part="a", day=DAY, year=YEAR)
    if ready == "2":
        letters=input("Enter letters: ")
        submit(letters, part="b", day=DAY, year=YEAR)
