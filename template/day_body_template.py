

def get_puzzle(file) -> list:
    return Path(file).read_text(encoding='utf8').splitlines()

def part1(puzzle):
    pass


def part2(puzzle):
    pass


if __name__ == '__main__':
    load_dotenv()
    puzzle_input = get_puzzle(PUZZLE_FILE)
    submit(part1(puzzle_input), part="a", day=DAY, year=YEAR)
    submit(part2(puzzle_input), part="b", day=DAY, year=YEAR)
