#!/usr/bin/env python3

from typing import List, Tuple


def _parse_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


def _split_into_separate_lists(data: List[str]) -> Tuple[List[str], List[str]]:
    left = []
    right = []
    for line in data:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))
    return left, right


def main():
    similarity_score = 0
    data = _parse_file("./locations_list")
    left, right = _split_into_separate_lists(data)
    for l_val in left:
        similarity_score += l_val * right.count(l_val)
    print(similarity_score)


if __name__ == "__main__":
    main()
