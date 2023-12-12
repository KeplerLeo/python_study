import csv
import sys
from typing import Dict, List
from rich import print

DATA_PATH = "exercises/section2/day1/spotify.csv"


def get_command_options() -> str:
    return """
    The following commands are available:
    1 - Show top 10 most popular instrumentals songs
    2 - Show top 10 most popular dance songs
    3 - Show top 10 most popular energetic songs"""


def read_csv(path: str) -> List[Dict[str, str]]:
    """read csv file and return list of dictionaries"""
    with open(path, "r") as file:
        return list(csv.DictReader(file))


def get_invalid_option_help(option):
    return f"""
    Opção {repr(option)} inválida.
    {get_command_options()}
    """
