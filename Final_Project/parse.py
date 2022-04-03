from typing import List

reserved_words = ["program", "var", "begin", "end.", "integer", "write"]
terminals = [":", ";", "=", "+", "-", "*", "/", "(", ")", ","]


def parse_identifiers_and_nums(tokens: List[str]):
    print(tokens)
    for token in tokens:
        if token not in reserved_words and token not in terminals:
            print(f"Error: {token} is not a valid token")
