from pathlib import Path

PUZZLE_FILE = "input/day01.txt"


def read_file(filename: str) -> list:
    return Path(filename).read_text(encoding="UTF-8").splitlines()


def get_elfs_sum(puzzle: list) -> list[list[int]]:
    elf = []
    elfs = []
    for item in puzzle:
        if item:
            elf.append(int(item))
        else:
            elfs.append(sum(elf))
            elf.clear()
    elfs.append(sum(elf))
    return elfs


def get_max_calories(elfs: list, nr_of_elfs=1) -> int:
    elfs.sort()
    return sum(elfs[-nr_of_elfs:])


def main() -> None:
    puzzle = read_file(PUZZLE_FILE)
    puzzle = get_elfs_sum(puzzle)
    max_calories = get_max_calories(puzzle)
    print(f"Part1: {max_calories}")
    max_calories = get_max_calories(puzzle, 3)
    print(f"Part2: {max_calories}")


if __name__ == "__main__":
    main()
