import unittest
from day02 import get_guide, is_winner, get_points, part1, part2

PUZZLE_FILE = "input/day02_test.txt"


class Tests(unittest.TestCase):

    test_guide = get_guide(PUZZLE_FILE)

    def test_is_winner(self):
        assert is_winner('A', 'A') == "Draw"
        assert is_winner('A', 'Y') == "Winner"
        assert is_winner('Y', 'A') == "Loser"

    def test_get_points(self):
        assert get_points("Winner", "Y") == 6+2
        assert get_points("Winner", "X") == 6+1
        assert get_points("Winner", "Z") == 6+3
        assert get_points("Loser", "Y") == 0+2
        assert get_points("Loser", "X") == 0+1
        assert get_points("Loser", "Z") == 0+3
        assert get_points("Draw", "Y") == 3+2
        assert get_points("Draw", "X") == 3+1
        assert get_points("Draw", "Z") == 3+3

    def test_part1(self):
        assert part1(self.test_guide) == 8+1+6

    def test_part2(self):
        assert part2(self.test_guide) == 4+1+7


if __name__ == "__main__":
    unittest.main()
