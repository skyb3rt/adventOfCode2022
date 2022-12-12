# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
from pathlib import Path
import os
from aocd import submit
from dotenv import load_dotenv

YEAR = os.environ.get("YEAR")
PUZZLE_FILE = "input/day08.txt"
DAY = 8


def get_puzzle(file) -> list:
    return [[*line] for line in Path(file).read_text(encoding='utf8').splitlines()]


def part1(puzzle):
    edges = len(puzzle)*4-4
    for i in range(1, len(puzzle[0])-1):
        for j in range(1, len(puzzle[0])-1):
            treesize = int(puzzle[i][j])
            row = [int(x) for x in puzzle[:][i]]
            col = [int(x[j]) for x in puzzle]
            max_col_1 = max(col[:i])
            max_col_2 = max(col[i+1:])
            max_row_1 = max(row[:j])
            max_row_2 = max(row[j+1:])
            if max_col_1 >= treesize <= max_col_2 and max_row_1 >= treesize <= max_row_2:
                pass
            else:
                edges += 1
    return edges


def count_view(trees, treesize):
    sum_view = 0
    for item in trees:
        if item < treesize:
            sum_view += 1
        if item >= treesize:
            sum_view += 1
            break
        if item > treesize:
            break
    return sum_view


def part2(puzzle):
    max_view = 0
    for i in range(1, len(puzzle[0])-1):
        for j in range(1, len(puzzle[0])-1):
            treesize = int(puzzle[i][j])
            row = [int(x) for x in puzzle[:][i]]
            col = [int(x[j]) for x in puzzle]
            col_1 = col[:i]
            col_2 = col[i+1:]
            row_1 = row[:j]
            row_2 = row[j+1:]
            col_1.reverse()
            row_1.reverse()
            view = count_view(col_1, treesize)*count_view(col_2, treesize) * \
                count_view(row_1, treesize)*count_view(row_2, treesize)
            if view > max_view:
                max_view = view
    return max_view


if __name__ == '__main__':
    load_dotenv()
    puzzle_input = get_puzzle(PUZZLE_FILE)
    result_part1 = part1(puzzle_input)
    result_part2 = part2(puzzle_input)
    print(f"part_1: {result_part1}")
    print(f"part_2: {result_part2}")
    ready = input("klar?")
    if ready == "1":
        submit(result_part1, part="a", day=DAY, year=YEAR)
    if ready == "2":
        submit(result_part2, part="b", day=DAY, year=YEAR)
