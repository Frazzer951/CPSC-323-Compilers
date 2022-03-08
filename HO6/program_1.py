"""
Input: (i+i)*i$
        MATCH! Stack: $, Q, R, ), E      Input: "i+i)*i$"
        MATCH! Stack: $, Q, R, ), Q, R   Input: "+i)*i$"
        MATCH! Stack: $, Q, R, ), Q, T   Input: "i)*i$"
        MATCH! Stack: $, Q, R, ), Q, R   Input: ")*i$"
        MATCH! Stack: $, Q, R            Input: "*i$"
        MATCH! Stack: $, Q, R, F         Input: "i$"
        MATCH! Stack: $, Q, R            Input: "$"
        MATCH! Stack:                    Input: ""
ACCEPTED


Input: i*(i-i)$
        MATCH! Stack: $, Q, R            Input: "*(i-i)$"
        MATCH! Stack: $, Q, R, F         Input: "(i-i)$"
        MATCH! Stack: $, Q, R, ), E      Input: "i-i)$"
        MATCH! Stack: $, Q, R, ), Q, R   Input: "-i)$"
        MATCH! Stack: $, Q, R, ), Q, T   Input: "i)$"
        MATCH! Stack: $, Q, R, ), Q, R   Input: ")$"
        MATCH! Stack: $, Q, R            Input: "$"
        MATCH! Stack:                    Input: ""
ACCEPTED


Input: i(i+i)$
        MATCH! Stack: $, Q, R            Input: "(i+i)$"
REJECTED
"""

from enum import Enum, auto


class State(Enum):
    E = 0
    Q = auto()
    T = auto()
    R = auto()
    F = auto()
    size = auto()


class Transition(Enum):
    BLANK = auto()
    TQ = auto()
    ADD_TQ = auto()
    SUB_TQ = auto()
    LAMBDA = auto()
    FR = auto()
    MULT_FR = auto()
    DIV_FR = auto()
    i = auto()
    PAREN_E = auto()


char_to_col = {
    "i": 0,
    "+": 1,
    "-": 2,
    "*": 3,
    "/": 4,
    "(": 5,
    ")": 6,
    "$": 7,
}

TT = [
    [
        Transition.TQ,
        Transition.BLANK,
        Transition.BLANK,
        Transition.BLANK,
        Transition.BLANK,
        Transition.TQ,
        Transition.BLANK,
        Transition.BLANK,
    ],
    [
        Transition.BLANK,
        Transition.ADD_TQ,
        Transition.SUB_TQ,
        Transition.BLANK,
        Transition.BLANK,
        Transition.BLANK,
        Transition.LAMBDA,
        Transition.LAMBDA,
    ],
    [
        Transition.FR,
        Transition.BLANK,
        Transition.BLANK,
        Transition.BLANK,
        Transition.BLANK,
        Transition.FR,
        Transition.BLANK,
        Transition.BLANK,
    ],
    [
        Transition.BLANK,
        Transition.LAMBDA,
        Transition.LAMBDA,
        Transition.MULT_FR,
        Transition.DIV_FR,
        Transition.BLANK,
        Transition.LAMBDA,
        Transition.LAMBDA,
    ],
    [
        Transition.i,
        Transition.BLANK,
        Transition.BLANK,
        Transition.BLANK,
        Transition.BLANK,
        Transition.PAREN_E,
        Transition.BLANK,
        Transition.BLANK,
    ],
]

strings = ["(i+i)*i$", "i*(i-i)$", "i(i+i)$"]

for string in strings:
    stack = ["$", State.E]
    input = list(string)
    cur_char = None
    print("Input:", string)
    while len(stack) > 0 or len(input) > 0:
        state = stack.pop()
        if not cur_char:
            cur_char = input.pop(0)

        if isinstance(state, str):
            if state == cur_char:
                cur_char = None
            else:
                break
        else:
            result = TT[state.value][char_to_col[cur_char]]

            if result == Transition.BLANK:
                break
            elif result == Transition.LAMBDA:
                continue
            elif result == Transition.TQ:
                stack.append(State.Q)
                stack.append(State.T)
            elif result == Transition.ADD_TQ:
                stack.append(State.Q)
                stack.append(State.T)
                stack.append("+")
            elif result == Transition.SUB_TQ:
                stack.append(State.Q)
                stack.append(State.T)
                stack.append("-")
            elif result == Transition.FR:
                stack.append(State.R)
                stack.append(State.F)
            elif result == Transition.MULT_FR:
                stack.append(State.R)
                stack.append(State.F)
                stack.append("*")
            elif result == Transition.DIV_FR:
                stack.append(State.R)
                stack.append(State.F)
                stack.append("/")
            elif result == Transition.PAREN_E:
                stack.append(")")
                stack.append(State.E)
                stack.append("(")
            elif result == Transition.i:
                if cur_char != "i":
                    break
                cur_char = None
            else:
                print("UNKNOWN TRANSITION", result)
                break
        if cur_char is None:
            stack_str = "Stack: " + ", ".join(
                x.name if isinstance(x, State) else x for x in stack
            )
            input_str = 'Input: "' + "".join(input) + '"'
            print("\tMATCH! {:<25} {}".format(stack_str, input_str))
    print("ACCEPTED" if len(stack) == 0 and len(input) == 0 else "REJECTED")
    print("\n")
