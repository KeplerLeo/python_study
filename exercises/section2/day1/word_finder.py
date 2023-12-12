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


def main():
    file_path = "exercises/section2/day1/word_finder.py"
    search_word = "python"
    occurrences = lines_with_word_occurrences(file_path, search_word)
    print(f'Word "{search_word}" occurs in lines:', occurrences)


if __name__ == "__main__":
    main()
