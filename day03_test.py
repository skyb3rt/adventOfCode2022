# pylint: disable=invalid-name
import unittest
from day03 import get_puzzle, get_common, get_priorities, split_rucksacks

PUZZLE_FILE = "input/day03_test.txt"


class Tests(unittest.TestCase):
    puzzle = get_puzzle(PUZZLE_FILE)
    puzzle_part1 = split_rucksacks(puzzle)
    puzzle_part2 = [set(x) for x in puzzle]

    def test_split_rucksacks(self):
        puzzle = self.puzzle_part1
        assert puzzle[0][0] == set("vJrwpWtwJgWr")
        assert puzzle[0][1] == set("hcsFMMfFFhFp")

    def test_get_common(self):
        puzzle = self.puzzle_part1
        assert get_common(puzzle[0][0], puzzle[0][1]) == "p"

    def test_get_priorities(self):
        assert get_priorities("a") == 1
        assert get_priorities("z") == 26
        assert get_priorities("A") == 27
        assert get_priorities("Z") == 52

    def test_part1(self):
        puzzle = self.puzzle_part1
        assert sum([get_priorities(get_common(x[0], x[1]))
                   for x in puzzle]) == 157

    def test_part2(self):
        puzzle = self.puzzle_part2
        assert get_common(puzzle[0], puzzle[1], puzzle[2]) == "r"
        assert get_common(puzzle[3], puzzle[4], puzzle[5]) == "Z"


if __name__ == '__main__':
    unittest.main()
