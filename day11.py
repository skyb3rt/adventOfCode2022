# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=duplicate-code
from pathlib import Path
import os
from dataclasses import dataclass
import parse
from aocd import submit
from dotenv import load_dotenv


YEAR = os.environ.get("YEAR")
PUZZLE_FILE = "input/day11.txt"
DAY = 11


def get_puzzle(file) -> list:
    return Path(file).read_text(encoding='utf8').splitlines()


@dataclass
class Operation():
    operation_1: str
    operation_type: str
    operation_2: str


@dataclass
class Test():
    divisible_by: str
    if_true_trow_to_monkey: int
    if_false_trow_to_monkey: int


@dataclass
class Monkey():
    monkey_nr: int
    starting_items: list[int]
    got_items: list[int]
    operation: Operation
    test: Test
    inspected_items = 0

    def get_worry_level(self, value: int, divide: bool, lcm=1):
        self.inspected_items += 1
        operation_1 = self.operation["operation_1"]
        operation_2 = self.operation["operation_2"]
        operation_1 = int(operation_1.replace("old", str(value)))
        operation_2 = int(operation_2.replace("old", str(value)))
        if self.operation["operation_type"] == "*":
            operation_sum = operation_1*operation_2
        if self.operation["operation_type"] == "+":
            operation_sum = (operation_1+operation_2)
        if divide:
            return operation_sum//3
        return operation_sum % lcm

    def throw_to_monkey(self, value):
        if value % self.test["divisible_by"] == 0:
            return self.test["if_true_trow_to_monkey"]
        return self.test["if_false_trow_to_monkey"]


def parse_puzzle(puzzle):
    monkeys = []
    for line in puzzle:
        match line:
            case _ if line.startswith("Monkey"):
                pattern = "Monkey {monkey_nr:d}"
                result = parse.search(pattern, line).named

            case _ if line.startswith("  Starting"):
                result['starting_items'] = [
                    int(item) for item in line.split(":")[1].split(",")]

            case _ if line.startswith("  Operation:"):
                pattern = "  Operation: new = {operation_1:w} {operation_type:W} {operation_2:w}"
                result['operation'] = (parse.search(pattern, line).named)
            case _ if line.startswith("  Test:"):
                pattern = "  Test: divisible by {divisible_by:d}"
                result["test"] = (parse.search(pattern, line).named)
            case _ if line.startswith("    If true:"):
                pattern = "    If true: throw to monkey {if_true_trow_to_monkey:d}"
                result["test"].update(parse.search(pattern, line).named)
            case _ if line.startswith("    If false:"):
                pattern = "    If false: throw to monkey {if_false_trow_to_monkey:d}"
                result["test"].update(parse.search(pattern, line).named)
            case _:
                result['got_items'] = []
                monkeys.append(Monkey(**result))
    return monkeys


def game(puzzle, rounds: int, divide: bool):
    monkeys = parse_puzzle(puzzle)
    lcm = 1
    for monkey in monkeys:
        lcm = (lcm*monkey.test["divisible_by"])
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.starting_items += monkey.got_items
            monkey.got_items = []

            for item in monkey.starting_items:
                worry_level = monkey.get_worry_level(item, divide, lcm)
                throw_to_monkey = monkey.throw_to_monkey(worry_level)
                monkeys[throw_to_monkey].got_items.append(worry_level)
            monkey.starting_items = []
        inspected = []
    for monkey in monkeys:
        #print(f"monkey nr: {monkey.monkey_nr} inspected items {monkey.inspected_items} times.")
        inspected.append(monkey.inspected_items)
        inspected.sort()

    return inspected[-1]*inspected[-2]


def part1(puzzle):
    return game(puzzle=puzzle, rounds=20, divide=True)


def part2(puzzle):
    return game(puzzle=puzzle, rounds=10000, divide=False)


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
    if ready == "2":
        submit(RESULT_PART2, part="b", day=DAY, year=YEAR)
