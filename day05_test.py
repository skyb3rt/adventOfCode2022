# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
import unittest
from day05 import get_puzzle, part1, part2

PUZZLE_FILE = "input/day05_test.txt"

class Tests(unittest.TestCase):
    puzzle = get_puzzle(PUZZLE_FILE)

    def test_part1(self):
        puzzle = self.puzzle
        result= part1(puzzle)
        assert result == "CMZ"

    def test_part2(self):
        puzzle = self.puzzle
        assert part2(puzzle) == "MCD"


if __name__ == '__main__':
    unittest.main()
    