# pylint: skip-file
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=duplicate-code
from pathlib import Path
import os
import parse
from aocd import submit
from dotenv import load_dotenv

YEAR = os.environ.get("YEAR")
