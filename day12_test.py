# pylint: skip-file
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
import unittest
from day12 import get_puzzle, part1, part2

PUZZLE_FILE = "input/day12_test.txt"
DAY = 12


class Tests(unittest.TestCase):
    puzzle = get_puzzle(PUZZLE_FILE)

    def test_part1(self):
        puzzle = self.puzzle
        assert part1(puzzle) == ""


    def test_part2(self):
        puzzle = self.puzzle
        assert part2(puzzle) == ""


if __name__ == '__main__':
    unittest.main()
