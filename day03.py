# pylint: disable=invalid-name
from pathlib import Path
import logging
import string

logging.basicConfig(level=logging.INFO)

PRIORITIES_LIST = " "+string.ascii_lowercase+string.ascii_uppercase


def get_puzzle(file) -> list:
    return Path(file).read_text(encoding='utf8').splitlines()


def split_rucksacks(rucksaks: list) -> list[list[str]]:
    return [[set(line[0:int(len(line)/2)]), set(line[int(len(line)/2):])] for line in rucksaks]


def get_common(rucksack_1: set, *rucksacks: set)->str:
    return rucksack_1.intersection(*rucksacks).pop()



def get_priorities(caracter: str) -> int:
    return PRIORITIES_LIST.index(caracter)


def tests():
    # part1
    puzzle = get_puzzle("3_test.txt")
    puzzle = split_rucksacks(puzzle)
    assert puzzle[0][0] == set("vJrwpWtwJgWr")
    assert puzzle[0][1] == set("hcsFMMfFFhFp")
    assert get_common(puzzle[0][0], puzzle[0][1]) == "p"
    assert get_priorities("a") == 1
    assert get_priorities("z") == 26
    assert get_priorities("A") == 27
    assert get_priorities("Z") == 52
    assert sum([get_priorities(get_common(x[0], x[1])) for x in puzzle]) == 157
    logging.debug("Tests part 1 runs ok")

    # part2
    puzzle = get_puzzle("3_test.txt")
    puzzle = [set(x) for x in puzzle]
    assert get_common(puzzle[0], puzzle[1], puzzle[2]) == "r"
    assert get_common(puzzle[3], puzzle[4], puzzle[5]) == "Z"
    logging.debug("Tests part 2 runs ok")


def part1():
    puzzle = get_puzzle("3.txt")
    puzzle = split_rucksacks(puzzle)
    sum_puzzle = sum([get_priorities(get_common(x[0], x[1])) for x in puzzle])
    logging.info("Sum part 1: %s",sum_puzzle)


def part2():
    puzzle = get_puzzle("3.txt")
    puzzle = [set(x) for x in puzzle]
    totalt = 0
    for i in range(0, len(puzzle), 3):
        totalt += get_priorities(
            (get_common(puzzle[i], puzzle[i+1], puzzle[i+2])))
    logging.info("Sum part 2: %s",totalt)


def main():
    tests()
    part1()
    part2()


if __name__ == '__main__':
    main()
