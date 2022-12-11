# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
import unittest
from day07 import get_puzzle, run_commands, part1, part2

PUZZLE_FILE = "input/day07_test.txt"
DAY = 7


class Tests(unittest.TestCase):
    puzzle = get_puzzle(PUZZLE_FILE)
    hdd = run_commands(puzzle)

    def test_part1(self):
        hdd = self.hdd
        assert part1(hdd) == 95437

    def test_part2(self):
        hdd = self.hdd
        assert part2(hdd) == 24933642


if __name__ == '__main__':
    unittest.main()
