# pylint: skip-file

def get_puzzle(file) -> list:
    return Path(file).read_text(encoding='utf8').splitlines()

def part1(puzzle):
    pass


def part2(puzzle):
    pass


if __name__ == '__main__':
    load_dotenv()
    puzzle_input = get_puzzle(PUZZLE_FILE)
    RESULT_PART1 = part1(puzzle_input)
    RESULT_PART2 = part2(puzzle_input)
    print(f"part_1: {RESULT_PART1}")
    print(f"part_2: {RESULT_PART2}")
    ready = input("submit [1,2]?")
    if ready == "1":
        submit(RESULT_PART1, part="a", day=DAY, year=YEAR)
    if ready == "2":
        submit(RESULT_PART2, part="b", day=DAY, year=YEAR)

