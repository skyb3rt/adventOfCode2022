# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
# pylint: disable=duplicate-code
from pathlib import Path
import os
from aocd import submit
from dotenv import load_dotenv
from pydantic import BaseModel

YEAR = os.environ.get("YEAR")
PUZZLE_FILE = "input/day07.txt"
DAY = 7


def get_puzzle(file) -> list:
    return Path(file).read_text(encoding='utf8').splitlines()


class File(BaseModel):
    name: str = ""
    size: int = 0


class Directory(BaseModel):
    files: list[File] = []
    name: str = ""
    path: str = None
    size: int = 0
    total_size: int = 0

    def get_size(self):
        return sum(file.size for file in self.files)


class Harddrive(BaseModel):
    current_dir: Directory = []
    directorys: list[Directory] = []

    def get_current_dir_index(self):
        return self.directorys.index(
            [dir for dir in self.directorys if dir.name == self.current_dir.name].pop())

    def get_dir_index_name(self, name):
        try:
            return self.directorys.index(
                [directory for directory in self.directorys if directory.name == name].pop())
        except IndexError:
            return None

    def get_dir_index_path(self, path):
        try:
            return self.directorys.index(
                [directory for directory in self.directorys if directory.path == path].pop())
        except IndexError:
            return None


def run_commands(puzzle):
    hdd = Harddrive()
    hdd.directorys.append(Directory(name="/", path="/"))
    hdd.current_dir = 0
    for line in puzzle:
        match line:
            case "$ cd ..":
                path = hdd.directorys[hdd.current_dir].path
                path = "/".join(path.split("/")[0:-1])
                path = "/" if path == "" else path
                hdd.current_dir = hdd.get_dir_index_path(path)
            case "$ cd /":
                hdd.current_dir = 0
            case _ as command if command.startswith("$ cd"):
                directory = command = command.split(" ")[2]
                skille = "/" if hdd.current_dir != 0 else ""
                path = hdd.directorys[hdd.current_dir].path+skille+directory
                if hdd.get_dir_index_path(path) is None:
                    hdd.directorys.append(Directory(name=dir, path=path))
                hdd.current_dir = hdd.get_dir_index_path(path)
            case _ as command if command.startswith("dir"):
                directory = command = command.split(" ")[1]
                skille = "/" if hdd.current_dir != 0 else ""
                path = hdd.directorys[hdd.current_dir].path+skille+directory
                if hdd.get_dir_index_path(path) is None:
                    hdd.directorys.append(Directory(name=directory, path=path))
            case _ as command if command[0].isdigit():
                command = command.split(" ")
                hdd.directorys[hdd.current_dir].files.append(
                    File(size=int(command[0]), name=command[1]))
    return hdd


def part1(hdd: Harddrive):
    for directory in hdd.directorys:
        directory.size = directory.get_size()

    dir_totalt_size = 0
    for directory in hdd.directorys:
        dir_size = sum(
            (subdir.size for subdir in hdd.directorys if subdir.path.startswith(directory.path)))
        directory.total_size = dir_size
        if dir_size <= 100_000:
            dir_totalt_size += dir_size

    return dir_totalt_size


def part2(hdd: Harddrive):
    total_space = 70_000_000
    current_space = hdd.directorys[hdd.get_dir_index_path("/")].total_size
    free_space = total_space-current_space
    required_space = 30_000_000
    desired_space = required_space-free_space
    last = 0
    for directory in hdd.directorys:
        if last == 0:
            if directory.total_size >= desired_space:
                last = directory.total_size
        else:
            if directory.total_size < last and directory.total_size >= desired_space:
                last = directory.total_size
    return last


if __name__ == '__main__':
    load_dotenv()
    puzzle_input = get_puzzle(PUZZLE_FILE)
    harddrive = run_commands(puzzle_input)
    submit(part1(harddrive), part="a", day=DAY, year=YEAR)
    submit(part2(harddrive), part="b", day=DAY, year=YEAR)
