#!/usr/bin/env python3

from typing import List, Tuple


def parse_file(file_name):
    with open(file_name) as file:
        return [line.strip() for line in file]


def get_grid_size(lines: List[str]) -> Tuple[int, int]:
    return len(lines[0]), len(lines)


def word_grid_search(lines: List[str], word: str, x: int, y: int) -> int:
    word_len = len(word)
    grid_size = get_grid_size(lines)
    found = 0
    directions = [
        (0, -1),  # left
        (0, 1),  # right
        (-1, 0),  # up
        (-1, -1),  # up-left
        (-1, 1),  # up-right
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1),  # down-left
    ]
    for direction in directions:
        dir_x, dir_y = direction
        for i in range(1, word_len):
            new_x = x + dir_x * i
            new_y = y + dir_y * i
            if new_x < 0 or new_x >= grid_size[0] or new_y < 0 or new_y >= grid_size[1]:
                break
            if lines[new_y][new_x] != word[i]:
                break
        else:
            found += 1
    return found


def count_word_occurrences(lines: List[str], word: str) -> int:
    count = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == word[0]:
                words_found = word_grid_search(lines, word, x, y)
                count += words_found
    return count


def main():
    lines = parse_file("./word_search")
    print(count_word_occurrences(lines, "XMAS"))


if __name__ == "__main__":
    main()
