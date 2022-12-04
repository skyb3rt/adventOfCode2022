# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
import unittest
from day01 import get_max_calories, read_file, get_elfs_sum

PUZZLE_FILE = "input/day01_test.txt"


class Tests(unittest.TestCase):
    puzzle = read_file(PUZZLE_FILE)

    def test_get_elfs_sum(self):
        puzzle = self.puzzle
        assert get_elfs_sum(puzzle) == [6000, 4000, 11000, 24000, 10000]

    def test_get_max_calories(self):
        puzzle = get_elfs_sum(self.puzzle)
        assert get_max_calories(puzzle) == 24000


if __name__ == "__main__":
    unittest.main()
