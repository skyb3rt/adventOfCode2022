# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
import sys
import os
from pathlib import Path
from aocd.models import Puzzle
from dotenv import load_dotenv

if __name__ == "__main__":
    DAY = int(sys.argv[1])
    if os.path.exists(f"day{DAY:02}.py"):
        print(f"day{DAY:02}.py finnes fra før")
        sys.exit()
    load_dotenv()
    YEAR = os.environ.get("YEAR")
    puzzle = Puzzle(year=YEAR, day=DAY)
    PYLINT_SKIP_FILE = "# pylint: skip-file"
    day_top_template = Path(
        "template/day_top_template.py").read_text(encoding='utf-8')
    day_body_template = Path(
        "template/day_body_template.py").read_text(encoding='utf-8').replace(PYLINT_SKIP_FILE, "")
    puzzle_input = f"PUZZLE_FILE = \"input/day{DAY:02}_test.txt\"\n"
    puzzle_day = f"DAY = {DAY}\n"
    day_template = day_top_template+puzzle_input+puzzle_day+day_body_template

    day_test_top_template = Path(
        "template/day_test_top_template.py").read_text(encoding='utf-8')
    day_test_body_template = Path(
        "template/day_test_body_template.py").read_text(
            encoding='utf-8').replace(PYLINT_SKIP_FILE, "")
    imports = f"from day{DAY:02} import get_puzzle, part1, part2\n\n"
    puzzle_test_input = f"PUZZLE_FILE = \"input/day{DAY:02}_test.txt\"\n"
    day_test_template = day_test_top_template+imports + \
        puzzle_test_input+puzzle_day+day_test_body_template

    Path(f"day{DAY:02}.py").write_text(day_template, encoding='utf-8')
    Path(f"day{DAY:02}_test.py").write_text(
        day_test_template, encoding='utf-8')
    Path(f"input/day{DAY:02}.txt").write_text(puzzle.input_data,
                                              encoding='utf-8')
    Path(
        f"input/day{DAY:02}_test.txt").write_text(puzzle.example_data, encoding='utf-8')
