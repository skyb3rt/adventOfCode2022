# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
import unittest
from day11 import get_puzzle, part1, part2

PUZZLE_FILE = "input/day11_test.txt"
DAY = 11


class Tests(unittest.TestCase):
    puzzle = get_puzzle(PUZZLE_FILE)

    def test_part1(self):
        puzzle = self.puzzle
        assert part1(puzzle) == 10605


    def test_part2(self):
        puzzle = self.puzzle
        assert part2(puzzle) == 2713310158


if __name__ == '__main__':
    unittest.main()
