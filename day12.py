# pylint: skip-file
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=duplicate-code
from pathlib import Path
import os
from dataclasses import dataclass
import parse
from aocd import submit
from dotenv import load_dotenv

YEAR = os.environ.get("YEAR")
PUZZLE_FILE = "input/day12_test.txt"
DAY = 12


def get_puzzle(file) -> list:
    puzzle=[]
    with open(file, 'r') as f:
        puzzle=[[y for y in x.strip()] for x in f.readlines()]
    return puzzle


class Map():
    def __init__(self,puzzle):
        self.puzzle=puzzle
        self.hight=len(puzzle)
        self.width=len(puzzle[0])
        self.position=(0,0)
    
    def get_letter(self):
        return  self.puzzle[self.position[0]][self.position[1]]   

    def get_new_letter(self,position):
        return self.puzzle[position[0]][position[1]]  

    def get_new_position(self,move):
        return (self.position[0]+move[0],self.position[1]+move[1])

    def is_valid_move(self,move):
            letter=self.get_letter()
            letter=ord(letter) if letter!="S" else ord("a")
            match move:
                case "R":
                    new_position=self.get_new_position((0,1))
                    return self.width> new_position[1] and ord(self.get_new_letter(new_position))<=letter+1
                case "L":
                    new_position=self.get_new_position((0,-1))
                    return 0>= new_position[1] and ord(self.get_new_letter(new_position))<=letter+1
                case "U":
                    new_position=self.get_new_position((-1,0))
                    return 0<= new_position[0] and ord(self.get_new_letter(new_position))<=letter+1
                case "D":
                    new_position=self.get_new_position((1,0))
                    return self.hight> new_position[0] and ord(self.get_new_letter(new_position))<=letter+1


def part1(puzzle):
    my_map=Map(puzzle)
    while True:
        print(my_map.is_valid_move(input("[R,L,U,D]")))


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

