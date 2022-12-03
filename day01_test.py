import unittest
from day01 import get_max_calories, read_file, get_elfs_sum

PUZZLE_FILE = "input/day01_test.txt"

class Tests(unittest.TestCase):

    def test_get_max_calories(self):
        puzzle = read_file(PUZZLE_FILE)
        puzzle = get_elfs_sum(puzzle)
        assert get_max_calories(puzzle) == 24000


if __name__ == "__main__":
    unittest.main()
