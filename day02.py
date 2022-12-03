from pathlib import Path

PUZZLE_FILE = "input/day02.txt"

moves = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
         'Y': 'Paper', 'X': 'Rock', 'Z': 'Scissors'}
rules_winner = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
rules_point_hand = {"Rock": 1, "Paper": 2, "Scissors": 3}
rules_point_outcome = {'Winner': 6, "Loser": 0, "Draw": 3}


def is_winner(move_elf: str, move: str) -> str:
    move_elf = moves.get(move_elf)
    move = moves.get(move)
    if move_elf == move:
        return "Draw"
    if rules_winner.get(move_elf) == move:
        return "Loser"
    if rules_winner.get(move) == move_elf:
        return "Winner"


def get_points(outcome: str, move) -> int:
    move = moves.get(move)
    points = rules_point_outcome.get(outcome, 0)
    points += rules_point_hand.get(move, 0)
    return points


def part1(guide: list[set]) -> int:
    points_round = 0
    for i, v in guide:
        outcom = is_winner(i, v)
        points = get_points(outcom, v)
        points_round += points
    return points_round


def part2(guide: list[set]) -> int:
    points_round = 0
    for i, v in guide:
        #Y : draw
        if v == "Y":
            v = i
        #Z : win
        elif v == "Z":
            i_move = moves.get(i)
            v_move = [k for k, v in rules_winner.items() if v == i_move][0]
            v_move = [k for k, v in moves.items() if v == v_move][1]
            v = v_move
        #X : lose
        elif v == "X":
            i_move = moves.get(i)
            v_move = rules_winner.get(i_move)
            v_move = [k for k, v in moves.items() if v == v_move][1]
            v = v_move
        outcom = is_winner(i, v)
        points = get_points(outcom, v)
        points_round += points
    return points_round


def get_guide(filename: str) -> list:
    return [(line.split(" ")) for line in Path(filename).read_text(encoding="UTF-8").splitlines()]


if __name__ == "__main__":
    guide = get_guide(PUZZLE_FILE)
    points_game_1 = part1(guide)
    points_game_2 = part2(guide)
    print(f"Part1: {points_game_1}")
    print(f"Part2: {points_game_2}")
