from collections import defaultdict
from typing import List
from typing import Set

# Define all the terminal values
reserved_words = ["program", "var", "begin", "end.", "integer", "write"]
terminals = [":", ";", "=", "+", "-", "*", "/", "(", ")", ",", '"value="', "$"]
allowed_letters = "abcdwf"


def parse_identifiers_and_nums(tokens: List[str]):
    identifiers = set()  # set of identifiers
    numbers = set()  # set of numbers
    valid = True  # whether the tokens are valid
    for token in tokens:
        if token not in reserved_words and token not in terminals:
            first_char = token[0]
            if first_char in allowed_letters:
                # Do identifier checks
                valid_token = True
                for char in token[1:]:  # check if the rest of the chars are allowed
                    if not (char.isnumeric() or char in allowed_letters):
                        print(f"Char {char} is not allowed in identifier {token}")
                        valid_token = False
                if valid_token:
                    identifiers.add(token)
                else:
                    print(f"Invalid token: {token}")
                    valid = False
            elif first_char.isdigit() or first_char == "-" or first_char == "+":
                # Do number checks
                valid_token = True
                for char in token[1:]:  # check if the rest of the chars are allowed
                    if not char.isnumeric():
                        print(f"Char {char} is not allowed in number {token}")
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


def debug_print(stack: List[str], input: List[str], cur_token: str):
    print(f"Stack:            {stack}")
    print(f"Remaining Tokens: {input}")
    print(f"Current Token:    {cur_token}")
    print("")


# Define the transition table
TT = defaultdict(lambda: defaultdict(lambda: None))
TT["PR"]["program"] = ["program", "ID", ";", "var", "DL", "begin", "SL", "end."]
TT["DL"]["ID"] = ["DE", ":", "TY", ";"]
TT["DE"]["ID"] = ["ID", "Z"]
TT["Z"][","] = [",", "DE"]
TT["Z"][":"] = ["lambda"]
TT["TY"]["integer"] = ["integer"]
TT["SL"]["write"] = ["SA", "W"]
TT["SL"]["ID"] = ["SA", "W"]
TT["W"]["end."] = ["lambda"]
TT["W"]["write"] = ["SL"]
TT["W"]["ID"] = ["SL"]
TT["SA"]["write"] = ["WR"]
TT["SA"]["ID"] = ["AS"]
TT["WR"]["write"] = ["write", "(", "ST", "ID", ")", ";"]
TT["ST"]["ID"] = ["lambda"]
TT["ST"]['"value="'] = ['"value="', ","]
TT["AS"]["ID"] = ["ID", "=", "EX", ";"]
TT["EX"]["ID"] = ["TR", "Q"]
TT["EX"]["NUM"] = ["TR", "Q"]
TT["EX"]["("] = ["TR", "Q"]
TT["Q"][")"] = ["lambda"]
TT["Q"]["+"] = ["+", "TR", "Q"]
TT["Q"]["-"] = ["-", "TR", "Q"]
TT["Q"][";"] = ["lambda"]
TT["TR"]["ID"] = ["FA", "R"]
TT["TR"]["NUM"] = ["FA", "R"]
TT["TR"]["("] = ["FA", "R"]
TT["R"][")"] = ["lambda"]
TT["R"]["+"] = ["lambda"]
TT["R"]["-"] = ["lambda"]
TT["R"]["*"] = ["*", "FA", "R"]
TT["R"]["/"] = ["/", "FA", "R"]
TT["R"][";"] = ["lambda"]
TT["FA"]["ID"] = ["ID"]
TT["FA"]["NUM"] = ["NUM"]
TT["FA"]["("] = ["(", "EX", ")"]


def parse_tokens(tokens: List[str], identifiers: Set[str], numbers: Set[str], debug: bool = False):
    prog_name = ""
    declared_vars = []
    operations = []
    declaration_mode = False
    declared = False

    if "end." not in tokens:
        print("'end.' is missing")
        return False, declared_vars, operations, prog_name

    stack = ["$", "PR"]
    input = tokens.copy()
    input.append("$")
    cur_token = None
    current_op = []
    in_op = False
    if debug:
        debug_print(stack, input, cur_token)
    while len(stack) > 0 or len(input) > 0:
        state = stack.pop()
        if state == "WR" or state == "AS":  # if we are in a write or an assign statement
            in_op = True  # we are in an operation
            current_op = [cur_token]
        if not cur_token:
            cur_token = input.pop(0)
            if in_op and cur_token == ";":  # if we are in an operation and the current token is a semicolon
                in_op = False  # we are not in an operation
                operations.append(current_op)
            elif in_op:
                current_op.append(cur_token)

        if state == "ID":
            if cur_token in identifiers:
                if declaration_mode:
                    declared_vars.append(cur_token)
                elif declared:
                    if cur_token not in declared_vars:
                        print(f"Variable '{cur_token}' not declared")
                        break
                else:
                    prog_name = cur_token
                cur_token = None
            else:
                print(f"Expected identifier, got {cur_token}")
                break
        elif state == "NUM":
            if cur_token in numbers:
                cur_token = None
            else:
                print(f"Expected number, got {cur_token}")
                break
        elif state in terminals:
            if state == cur_token:
                cur_token = None
            else:
                print(f"Expected '{state}', got {cur_token}")
                break
        elif state in reserved_words:
            if state == cur_token:
                cur_token = None
            else:
                print(f"Expected '{state}', got {cur_token}")
                break
            if state == "var":
                declaration_mode = True
            elif state == "begin":
                declaration_mode = False
                declared = True
        elif state == "lambda":
            continue
        else:
            if cur_token in identifiers:
                parse_token = "ID"
            elif cur_token in numbers:
                parse_token = "NUM"
            else:
                parse_token = cur_token
            result = TT[state][parse_token]
            if result is None:
                expected = list(TT[state])
                expected.remove(parse_token)
                expected = " or ".join(expected)
                print(f"Expected {expected}, got {cur_token}")
                break
            elif isinstance(result, list):
                stack += reversed(result)
            else:
                print(f"Unknown Result from TT: {result}")
                break
        if debug:
            if cur_token is None:
                print("MATCH")
            debug_print(stack, input, cur_token)
    accepted = len(stack) == 0 and len(input) == 0 and not cur_token
    return accepted, declared_vars, operations, prog_name
