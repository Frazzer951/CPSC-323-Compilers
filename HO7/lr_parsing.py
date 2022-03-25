"""
Input: (i+i)*i$
Accepted

Input: (i*)$
Rejected: Reached BLANK state
"""
from collections import defaultdict
from enum import auto
from enum import Enum


class Transition(Enum):
    BLANK = auto()
    ACC = auto()
    S4 = auto()
    S5 = auto()
    S6 = auto()
    S7 = auto()
    S8 = auto()
    S9 = auto()
    S15 = auto()
    R1 = auto()
    R2 = auto()
    R3 = auto()
    R4 = auto()
    R5 = auto()
    R6 = auto()
    R7 = auto()
    R8 = auto()
    NT1 = auto()
    NT2 = auto()
    NT3 = auto()
    NT10 = auto()
    NT11 = auto()
    NT12 = auto()
    NT13 = auto()
    NT14 = auto()


TT = [
    defaultdict(lambda: Transition.BLANK),  # 0
    defaultdict(lambda: Transition.BLANK),  # 1
    defaultdict(lambda: Transition.BLANK),  # 2
    defaultdict(lambda: Transition.BLANK),  # 3
    defaultdict(lambda: Transition.BLANK),  # 4
    defaultdict(lambda: Transition.BLANK),  # 5
    defaultdict(lambda: Transition.BLANK),  # 6
    defaultdict(lambda: Transition.BLANK),  # 7
    defaultdict(lambda: Transition.BLANK),  # 8
    defaultdict(lambda: Transition.BLANK),  # 9
    defaultdict(lambda: Transition.BLANK),  # 10
    defaultdict(lambda: Transition.BLANK),  # 11
    defaultdict(lambda: Transition.BLANK),  # 12
    defaultdict(lambda: Transition.BLANK),  # 13
    defaultdict(lambda: Transition.BLANK),  # 14
    defaultdict(lambda: Transition.BLANK),  # 15
]

TT[0]["i"] = Transition.S5
TT[0]["("] = Transition.S4
TT[0]["E"] = Transition.NT1
TT[0]["T"] = Transition.NT2
TT[0]["F"] = Transition.NT3

TT[1]["+"] = Transition.S6
TT[1]["-"] = Transition.S7
TT[1]["$"] = Transition.ACC

TT[2]["+"] = Transition.R3
TT[2]["-"] = Transition.R3
TT[2]["*"] = Transition.S8
TT[2]["/"] = Transition.S9
TT[2][")"] = Transition.R3
TT[2]["$"] = Transition.R3

TT[3]["+"] = Transition.R6
TT[3]["-"] = Transition.R6
TT[3]["*"] = Transition.R6
TT[3]["/"] = Transition.R6
TT[3][")"] = Transition.R6
TT[3]["$"] = Transition.R6

TT[4]["i"] = Transition.S5
TT[4]["("] = Transition.S4
TT[4]["E"] = Transition.NT10
TT[4]["T"] = Transition.NT2
TT[4]["F"] = Transition.NT3

TT[5]["+"] = Transition.R8
TT[5]["-"] = Transition.R8
TT[5]["*"] = Transition.R8
TT[5]["/"] = Transition.R8
TT[5][")"] = Transition.R8
TT[5]["$"] = Transition.R8

TT[6]["i"] = Transition.S5
TT[6]["("] = Transition.S4
TT[6]["T"] = Transition.NT11
TT[6]["F"] = Transition.NT3

TT[7]["i"] = Transition.S5
TT[7]["("] = Transition.S4
TT[7]["T"] = Transition.NT12
TT[7]["F"] = Transition.NT3

TT[8]["i"] = Transition.S5
TT[8]["("] = Transition.S4
TT[8]["F"] = Transition.NT13

TT[9]["i"] = Transition.S5
TT[9]["("] = Transition.S4
TT[9]["F"] = Transition.NT14

TT[10]["+"] = Transition.S6
TT[10]["-"] = Transition.S7
TT[10][")"] = Transition.S15

TT[11]["+"] = Transition.R1
TT[11]["-"] = Transition.R1
TT[11]["*"] = Transition.S8
TT[11]["/"] = Transition.S9
TT[11][")"] = Transition.R1
TT[11]["$"] = Transition.R1

TT[12]["+"] = Transition.R2
TT[12]["-"] = Transition.R2
TT[12]["*"] = Transition.S8
TT[12]["/"] = Transition.S9
TT[12][")"] = Transition.R2
TT[12]["$"] = Transition.R2

TT[13]["+"] = Transition.R4
TT[13]["-"] = Transition.R4
TT[13]["*"] = Transition.R4
TT[13]["/"] = Transition.R4
TT[13][")"] = Transition.R4
TT[13]["$"] = Transition.R4

TT[14]["+"] = Transition.R5
TT[14]["-"] = Transition.R5
TT[14]["*"] = Transition.R5
TT[14]["/"] = Transition.R5
TT[14][")"] = Transition.R5
TT[14]["$"] = Transition.R5

TT[15]["+"] = Transition.R7
TT[15]["-"] = Transition.R7
TT[15]["*"] = Transition.R7
TT[15]["/"] = Transition.R7
TT[15][")"] = Transition.R7
TT[15]["$"] = Transition.R7


strings = ["(i+i)*i$", "(i*)$"]

for string in strings:
    stack = [0]
    input = list(string)
    cur_char = None
    print("Input:", string)
    while len(stack) > 0 or len(input) > 0:
        state = stack.pop()
        cur_char = input.pop(0)
        result = TT[state][cur_char]

        if result == Transition.BLANK:
            print("Rejected: Reached BLANK state")
            break
        elif result == Transition.ACC:
            print("Accepted")
            break
        elif result == Transition.S4:
            stack.append(state)
            stack.append(cur_char)
            stack.append(4)
        elif result == Transition.S5:
            stack.append(state)
            stack.append(cur_char)
            stack.append(5)
        elif result == Transition.S6:
            stack.append(state)
            stack.append(cur_char)
            stack.append(6)
        elif result == Transition.S7:
            stack.append(state)
            stack.append(cur_char)
            stack.append(7)
        elif result == Transition.S8:
            stack.append(state)
            stack.append(cur_char)
            stack.append(8)
        elif result == Transition.S9:
            stack.append(state)
            stack.append(cur_char)
            stack.append(9)
        elif result == Transition.S15:
            stack.append(state)
            stack.append(cur_char)
            stack.append(15)
        elif result == Transition.R1:
            stack.append(state)
            for _ in range(6):
                stack.pop()
            input.insert(0, cur_char)
            input.insert(0, "E")
        elif result == Transition.R2:
            stack.append(state)
            for _ in range(6):
                stack.pop()
            input.insert(0, cur_char)
            input.insert(0, "E")
        elif result == Transition.R3:
            stack.append(state)
            for _ in range(2):
                stack.pop()
            input.insert(0, cur_char)
            input.insert(0, "E")
        elif result == Transition.R4:
            stack.append(state)
            for _ in range(6):
                stack.pop()
            input.insert(0, cur_char)
            input.insert(0, "T")
        elif result == Transition.R5:
            stack.append(state)
            for _ in range(6):
                stack.pop()
            input.insert(0, cur_char)
            input.insert(0, "T")
        elif result == Transition.R6:
            stack.append(state)
            for _ in range(2):
                stack.pop()
            input.insert(0, cur_char)
            input.insert(0, "T")
        elif result == Transition.R7:
            stack.append(state)
            for _ in range(6):
                stack.pop()
            input.insert(0, cur_char)
            input.insert(0, "F")
        elif result == Transition.R8:
            stack.append(state)
            for _ in range(2):
                stack.pop()
            input.insert(0, cur_char)
            input.insert(0, "F")
        elif result == Transition.NT1:
            stack.append(state)
            stack.append(cur_char)
            stack.append(1)
        elif result == Transition.NT2:
            stack.append(state)
            stack.append(cur_char)
            stack.append(2)
        elif result == Transition.NT3:
            stack.append(state)
            stack.append(cur_char)
            stack.append(3)
        elif result == Transition.NT10:
            stack.append(state)
            stack.append(cur_char)
            stack.append(10)
        elif result == Transition.NT11:
            stack.append(state)
            stack.append(cur_char)
            stack.append(11)
        elif result == Transition.NT12:
            stack.append(state)
            stack.append(cur_char)
            stack.append(12)
        elif result == Transition.NT13:
            stack.append(state)
            stack.append(cur_char)
            stack.append(13)
        elif result == Transition.NT14:
            stack.append(state)
            stack.append(cur_char)
            stack.append(14)
