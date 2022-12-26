# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
import unittest
from day09 import get_puzzle, part1, part2

PUZZLE_FILE = "input/day09_test.txt"
DAY = 9


class Tests(unittest.TestCase):
    puzzle = get_puzzle(PUZZLE_FILE)

    def test_part1(self):
        puzzle = self.puzzle
        assert part1(puzzle) == 13

    def test_part2(self):
        puzzle = self.puzzle
        assert part2(puzzle) == 1


if __name__ == '__main__':
    unittest.main()
