#!/usr/bin/env python3

from typing import List, Tuple


def parse_file(file_name):
    with open(file_name) as file:
        return [line.strip() for line in file]


def get_grid_size(lines: List[str]) -> Tuple[int, int]:
    return len(lines[0]), len(lines)


def is_in_bounds(pos, grid_size):
    return 0 <= pos < grid_size


def word_grid_search_x(
    lines: List[str],
    word: str,
    x: int,
    y: int,
) -> int:
    """
    Search for word that crosses in a X pattern.
    1. Check if the word is in bounds.
    2. Check all 4 possible directions for the word
       using the starting point and the middle of the word
       as index points to increment and decrement.
    """
    grid_size = get_grid_size(lines)
    distance_from_middle = (len(word) - 1) // 2
    found = 0
    directions = [
        ((-1, -1), (1, 1)),  # top left to bottom right
        ((-1, 1), (1, -1)),  # bottom left to top right
        ((1, -1), (-1, 1)),  # top right to bottom left
        ((1, 1), (-1, -1)),  # bottom right to top left
    ]
    for direction in directions:
        if found == 2:
            break

        (x1, y1), (x2, y2) = direction

        # start,stop edge to check against boundaries
        (x1, y1), (x2, y2) = (x1 * distance_from_middle, y1 * distance_from_middle), (
            x2 * distance_from_middle,
            y2 * distance_from_middle,
        )

        # bounds check
        if not (
            is_in_bounds(x + x1, grid_size[0])
            and is_in_bounds(x + x2, grid_size[0])
            and is_in_bounds(y + y1, grid_size[1])
            and is_in_bounds(y + y2, grid_size[1])
        ):
            continue

        for i in range(distance_from_middle, 0, -1):
            if (
                lines[y + y1 * i][x + x1 * i] != word[distance_from_middle - i]
                or lines[y + y2 * i][x + x2 * i] != word[i + distance_from_middle]
            ):
                break
            else:
                if i == 1:
                    found += 1
    return 1 if found == 2 else 0


def count_word_occurrences(lines: List[str], word: str) -> int:
    count = 0
    middle_of_word = word[(len(word) - 1) // 2 : (len(word) + 2) // 2]
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == middle_of_word:
                words_found = word_grid_search_x(lines, word, x, y)
                count += words_found
    return count


def main():
    lines = parse_file("./word_search")
    print(count_word_occurrences(lines, "MAS"))


if __name__ == "__main__":
    main()
