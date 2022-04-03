from typing import List

reserved_words = ["program", "var", "begin", "end.", "integer", "write"]
terminals = [":", ";", "=", "+", "-", "*", "/", "(", ")", ",", '"value="']


def parse_identifiers_and_nums(tokens: List[str]):
    identifiers = set()
    numbers = set()
    valid = True
    for token in tokens:
        if token not in reserved_words and token not in terminals:
            first_char = token[0]
            if first_char.isalpha():
                # Do identifier checks
                valid_token = True
                for char in token[1:]:
                    if not char.isalnum():
                        valid_token = False
                if valid_token:
                    identifiers.add(token)
                else:
                    print(f"Invalid token: {token}")
                    valid = False
            elif first_char.isdigit() or first_char == "-" or first_char == "+":
                # Do number checks
                valid_token = True
                for char in token[1:]:
                    if not char.isnumeric():
                        valid_token = False
                if valid_token:
                    numbers.add(token)
                else:
                    print(f"Invalid token: {token}")
                    valid = False
            else:
                print(f"Invalid token: {token}")
                valid = False
    return valid, identifiers, numbers
