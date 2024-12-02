#!/usr/bin/env python3

import sys
from typing import List, Tuple

LOCATION_FILE = "./locations_list"


def parse_file(file: str) -> Tuple[List[int], List[int]]:
    left = []
    right = []
    try:
        with open(file, "r") as f:
            for line in f:
                l_id, r_id = line.strip().split()
                try:
                    left.append(int(l_id))
                    right.append(int(r_id))
                except ValueError:
                    print(f"error casting line: {line}")
                    sys.exit(1)
    except FileNotFoundError:
        print(f"file not found: {file}")
        sys.exit(1)

    return left, right


def main():
    diff = 0
    left, right = parse_file(LOCATION_FILE)
    zipped = zip(sorted(left), sorted(right))
    for l, r in zipped:
        if l != r:
            diff += abs(l - r)
    print(diff)


if __name__ == "__main__":
    main()
