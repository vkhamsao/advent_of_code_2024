#!/usr/bin/env python3

from typing import DefaultDict, Tuple, List
from collections import defaultdict

test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def parse_input(input_string: str) -> Tuple[DefaultDict, List[List[int]]]:
    """
    Parse the input string into a dictionary of page rules and a list of updates
    using '|' as a delimiter for page rules and ',' for updates
    """
    page_rules = defaultdict(list)
    updates = []
    for line in input_string.split("\n"):
        if "|" in line:
            l_page, r_page = line.strip().split("|")
            page_rules[int(l_page)].append(int(r_page))
        if "," in line:
            updates.append([int(x) for x in line.strip().split(",")])

    return page_rules, updates


def reordered_middles(page_rules: DefaultDict, update: List[int]) -> int:
    """
    Recursive calls to swap elements until page ordering is happy
    """
    for idx in range(1, len(update)):
        if page_rules.get(update[idx], []):
            lists_intersect = any(
                set(page_rules[update[idx]]).intersection(set(update[:idx]))
            )
            if lists_intersect:
                update[idx - 1], update[idx] = update[idx], update[idx - 1]
                reordered_middles(page_rules, update)

    return update[len(update) // 2]


def check_lines(page_rules: DefaultDict, updates: List[List[int]]) -> List[int]:
    """
    Return a list of middle elements of each update that do not violate the page rules
    """
    middles = []
    for update in updates:
        reordered = False
        for idx in range(1, len(update)):
            if reordered:
                break
            if page_rules.get(update[idx], []):
                lists_intersect = any(
                    set(page_rules[update[idx]]).intersection(set(update[:idx]))
                )
                if lists_intersect:
                    middle = reordered_middles(page_rules, update)
                    middles.append(middle)
                    reordered = True

    return middles


# Test small sample
page_rules, updates = parse_input(test_input)
print(sum(check_lines(page_rules, updates)))

page_rules, updates = parse_input(read_file("input"))
print(sum(check_lines(page_rules, updates)))