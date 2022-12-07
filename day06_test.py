# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
import unittest
from day06 import get_puzzle, part1, part2

PUZZLE_FILE = "input/day06_test.txt"
DAY = "6"


class Tests(unittest.TestCase):
    puzzle = get_puzzle(PUZZLE_FILE)

    def test_part1(self):
        puzzle = self.puzzle
        assert part1(puzzle) == 7
        assert part1("nppdvjthqldpwncqszvftbrmjlhg") == 6
        assert part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
        assert part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

    def test_part2(self):
        puzzle = self.puzzle
        assert part2(puzzle) == 19
        assert part2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
        assert part2("nppdvjthqldpwncqszvftbrmjlhg") == 23
        assert part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
        assert part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26


if __name__ == '__main__':
    unittest.main()
