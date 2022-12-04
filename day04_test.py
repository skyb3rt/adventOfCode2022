# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
import unittest
from day04 import get_puzzle, compaire_assignments, part1, find_overlap, unpack_assignment, part2

PUZZLE_FILE = "input/day04_test.txt"


class Tests(unittest.TestCase):
    puzzle = get_puzzle(PUZZLE_FILE)

    @staticmethod
    def test_unpack_assignment():
        assert unpack_assignment(['2-3', '3-4']) == [{2, 3}, {3, 4}]
        assert unpack_assignment(['1-4', '2-4']) == [{1, 2, 3, 4}, {2, 3, 4}]

    @staticmethod
    def test_compaire_assigments():
        assert compaire_assignments({2, 3}, {2, 3})
        assert compaire_assignments({5, 6}, {2, 3, 4, 5, 6, 7, 8, 9})
        assert not compaire_assignments({2, 3, 4, 5, 6, 7, 8}, {5, 6, 7, 8, 9})
        assert not compaire_assignments({2, 3}, [3, 4, 5])

    def test_part1(self):
        puzzle = self.puzzle
        assert part1(puzzle) == 2

    @staticmethod
    def test_find_overlap():
        assert find_overlap({2, 3}, {3, 4})
        assert not find_overlap({2, 3}, {4, 5})

    def test_part2(self):
        puzzle = self.puzzle
        assert part2(puzzle) == 4


if __name__ == '__main__':
    unittest.main()
