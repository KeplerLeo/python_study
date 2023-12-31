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
    {get_command_options()}"""


def get_command_help(data_path) -> str:
    return f"""
    Analise informações do Spotify baseado no arquivo '{data_path}'.
    Modo de uso:
    python3 src/spotify.py [ opção ]
    {get_command_options()}"""


def get_most_instrumental_songs(
        data: List[Dict[str, str]]
        ) -> List[Dict[str, str]]:
    return sorted(data, key=lambda x: float(x["Instrumentalness"]),
                  reverse=True)[:10]


def get_most_danceable_songs(
        data: List[Dict[str, str]]
        ) -> List[Dict[str, str]]:
    return sorted(data, key=lambda x: float(x["Danceability"]),
                  reverse=True)[:10]


def get_most_energetic_songs(
        data: List[Dict[str, str]]
        ) -> List[Dict[str, str]]:
    return sorted(data, key=lambda x: float(x["Energy"]),
                  reverse=True)[:10]


OPTIONS = {
    "1": ("instrumentais", get_most_instrumental_songs),
    "2": ("dançantes", get_most_danceable_songs),
    "3": ("enérgicas", get_most_energetic_songs),
}


def process_music_analysis(data, option) -> None:
    print(f"Top 10 músicas mais {OPTIONS[option][0]}:")
    for index, song in enumerate(OPTIONS[option][1](data), start=1):
        print(f"{index:>2} - '{song['Track']}' de {song['Artist']}")


def handle_user_input(data, option) -> None:
    if option not in OPTIONS:
        print(get_invalid_option_help(option))
        raise ValueError
    process_music_analysis(data, option)


def main(file_path) -> int:
    cli_args = sys.argv[1:]
    if not cli_args:
        print(get_command_help(file_path))
        return 1

    data = read_csv(file_path)

    try:
        handle_user_input(data, cli_args[0])
    except ValueError:
        return 1

    return 0


if __name__ == "__main__":
    exit(main(DATA_PATH))
