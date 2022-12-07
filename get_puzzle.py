from aocd.models import Puzzle
import sys,os
from pathlib import Path
from dotenv import load_dotenv

if __name__ == "__main__":
    day=int(sys.argv[1])
    if os.path.exists(f"day{day:02}.py"):
        print(f"day{day:02}.py finnes fra før")
        exit()
    load_dotenv()
    YEAR = os.environ.get("YEAR")
    puzzle = Puzzle(year=YEAR, day=day)

    day_top_template=Path("template/day_top_template.py").read_text(encoding='utf-8')
    day_body_template=Path("template/day_body_template.py").read_text(encoding='utf-8')
    puzzle_input=f"PUZZLE_FILE = \"input/day{day:02}_test.txt\"\n"
    puzzle_day=f"DAY = \"{day}\"\n"
    day_template=day_top_template+puzzle_input+puzzle_day+day_body_template
    
    day_test_top_template=Path("template/day_test_top_template.py").read_text(encoding='utf-8')
    day_test_body_template=Path("template/day_test_body_template.py").read_text(encoding='utf-8')
    imports=f"from day{day:02} import get_puzzle, part1, part2\n\n"
    puzzle_test_input=f"PUZZLE_FILE = \"input/day{day:02}_test.txt\""
    day_test_template=day_test_top_template+imports+puzzle_test_input+puzzle_day+day_test_body_template
    
    Path(f"day{day:02}.py").write_text(day_template)
    Path(f"day{day:02}_test.py").write_text(day_test_template)
    Path(f"input/day{day:02}.txt").write_text(puzzle.input_data)
    Path(f"input/day{day:02}_test.txt").write_text(puzzle.example_data)
