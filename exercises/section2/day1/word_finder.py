def read_file_lines(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    return file_content.split("\n")


def lines_with_word_occurrences(file_path: str, word: str):
    str_lines = read_file_lines(file_path)
    result = []
    for index, line in enumerate(str_lines, start=1):
        if word.casefold() in line.casefold():
            result.append(index)
        return result
