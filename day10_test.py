# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
import unittest
from day10 import get_puzzle, part1

PUZZLE_FILE = "input/day10_test.txt"
DAY = 10


class Tests(unittest.TestCase):
    puzzle = get_puzzle(PUZZLE_FILE)

    def test_part1(self):
        puzzle = self.puzzle
        assert part1(puzzle) == 13140


if __name__ == '__main__':
    unittest.main()
