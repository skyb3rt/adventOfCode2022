# pylint: skip-file

class Tests(unittest.TestCase):
    puzzle = get_puzzle(PUZZLE_FILE)

    def test_part1(self):
        puzzle = self.puzzle
        assert part1(puzzle) == ?


    def test_part2(self):
        puzzle = self.puzzle
        assert part2(puzzle) == ?


if __name__ == '__main__':
    unittest.main()