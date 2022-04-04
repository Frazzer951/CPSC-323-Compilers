from collections import defaultdict
from enum import auto
from enum import Enum
from typing import List
from typing import Set

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


TT = defaultdict(lambda: defaultdict(lambda: None))


TT["PR"]["program"] = ["program", "ID", ";", "var", "DL", "begin", "SL", "end."]
TT["DL"]["ID"] = ["DE", ":", "TY", ";"]
TT["DE"]["ID"] = ["ID", "Z"]
TT["Z"][","] = [",", "DE"]
TT["Z"][":"] = "lambda"
TT["TY"]["integer"] = "integer"
TT["SL"]["write"] = ["SA", "W"]
TT["SL"]["ID"] = ["SA", "W"]
TT["W"]["end."] = "lambda"
TT["W"]["write"] = ["SL"]
TT["W"]["ID"] = ["SL"]
TT["SA"]["write"] = ["WR"]
TT["SA"]["ID"] = ["AS"]
TT["WR"]["write"] = ["write", "(", "ST", "ID", ")", ";"]
TT["ST"]["ID"] = "lambda"
TT["ST"]['"value="'] = ["“value=”", ","]
TT["AS"]["ID"] = ["ID", "=", "EX", ";"]
TT["EX"]["ID"] = ["TR", "Q"]
TT["EX"]["NUM"] = ["TR", "Q"]
TT["EX"]["("] = ["TR", "Q"]
TT["Q"][")"] = "lambda"
TT["Q"]["+"] = ["+", "TR", "Q"]
TT["Q"]["-"] = ["-", "TR", "Q"]
TT["Q"][";"] = "lambda"
TT["TR"]["ID"] = ["FA", "R"]
TT["TR"]["NUM"] = ["FA", "R"]
TT["TR"]["("] = ["FA", "R"]
TT["R"][")"] = "lambda"
TT["R"]["+"] = "lambda"
TT["R"]["-"] = "lambda"
TT["R"]["*"] = ["*", "FA", "R"]
TT["R"]["/"] = ["/", "FA", "R"]
TT["R"][";"] = "lambda"
TT["FA"]["ID"] = "ID"
TT["FA"]["NUM"] = "NUM"
TT["FA"]["("] = ["(", "EX", ")"]


def parse_tokens(tokens: List[str], indentifiers: Set[str], numbers: Set[str]):
    stack = ["$", "PR"]
