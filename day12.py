# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=duplicate-code
# pylint: disable=missing-class-docstring

import os
from aocd import submit
from dotenv import load_dotenv
import networkx as nx


YEAR = os.environ.get("YEAR")
PUZZLE_FILE = "input/day12.txt"
DAY = 12


def get_puzzle(filename) -> list:
    puzzle = []
    with open(filename, 'r',encoding='utf-8') as file:
        puzzle = [list(x.strip()) for x in file.readlines()]
    return puzzle


class Map():
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.hight = len(puzzle)
        self.width = len(puzzle[0])
        self.position = (0, 0)
        self.paths = []

    def get_letter(self):
        return self.puzzle[self.position[0]][self.position[1]]

    def get_new_letter(self, position):
        return self.puzzle[position[0]][position[1]]

    def get_new_position(self, move, position):
        return (position[0]+move[0], position[1]+move[1])

    def find_letter(self, letter, all_letters=False):
        position_letters = []
        for i in range(self.hight):
            for j in range(self.width):
                if letter == self.puzzle[i][j]:
                    if not all_letters:
                        return (i, j)
                    position_letters.append((i, j))
        return position_letters

    def is_valid_move(self, move, position):
        letter = self.get_new_letter(position)
        letter = ord(letter) if letter != "S" else ord("a")
        match move:
            case "R" | (0, 1):
                new_position = self.get_new_position((0, 1), position)
            case "L" | (0, -1):
                new_position = self.get_new_position((0, -1), position)
            case "U" | (-1, 0):
                new_position = self.get_new_position((-1, 0), position)
            case "D" | (1, 0):
                new_position = self.get_new_position((1, 0), position)
        if self.hight > new_position[0] >= 0 and self.width > new_position[1] >= 0:
            new_letter = self.get_new_letter(new_position)
            return ord(new_letter) <= letter+1 or new_letter == "E"
        return False

    def get_valid_moves(self, position: tuple) -> list[tuple]:
        valid_moves = []
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if self.is_valid_move(move, position):
                valid_moves.append(self.get_new_position(move, position))
        return valid_moves

    def get_all_posible_moves(self) -> list[tuple]:
        valid_moves = []
        for i in range(self.hight):
            valid_moves.append([])
            for j in range(self.width):
                valid_moves[i].append(self.get_valid_moves((i, j)))
        return valid_moves


def part1(puzzle):
    my_map = Map(puzzle)
    start_position = my_map.find_letter("S")
    stop_position = my_map.find_letter("E")
    valid_moves = my_map.get_all_posible_moves()
    graph = nx.DiGraph()
    nodes = [(i, j) for i in range(my_map.hight) for j in range(my_map.width)]
    graph.add_nodes_from(nodes)
    for i in range(my_map.hight):
        for j in range(my_map.width):
            for item in valid_moves[i][j]:
                graph.add_edge((i, j), item)
    return nx.shortest_path_length(graph, start_position, stop_position)


def part2(puzzle):
    my_map = Map(puzzle)
    start_positions = my_map.find_letter("a", all_letters=True)
    all_path_lengths = []
    stop_position = my_map.find_letter("E")
    valid_moves = my_map.get_all_posible_moves()
    graph = nx.DiGraph()
    nodes = [(i, j) for i in range(my_map.hight)
                for j in range(my_map.width)]
    graph.add_nodes_from(nodes)
    for i in range(my_map.hight):
        for j in range(my_map.width):
            for item in valid_moves[i][j]:
                graph.add_edge((i, j), item)
    for start_position in start_positions:
        try:
            all_path_lengths.append(nx.shortest_path_length(
                graph, start_position, stop_position))
        except nx.exception.NetworkXNoPath:
            pass
    return min(all_path_lengths)


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
