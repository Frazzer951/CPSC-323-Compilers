"""
Input: a=(a+a)*a$
        MATCH! Stack: $, W               Input: "=(a+a)*a$"
        MATCH! Stack: $, E               Input: "(a+a)*a$"
        MATCH! Stack: $, Q, R, ), E      Input: "a+a)*a$"
        MATCH! Stack: $, Q, R, ), Q, R   Input: "+a)*a$"
        MATCH! Stack: $, Q, R, ), Q, T   Input: "a)*a$"
        MATCH! Stack: $, Q, R, ), Q, R   Input: ")*a$"
        MATCH! Stack: $, Q, R            Input: "*a$"
        MATCH! Stack: $, Q, R, F         Input: "a$"
        MATCH! Stack: $, Q, R            Input: "$"
        MATCH! Stack:                    Input: ""
ACCEPTED


Input: a=a*(a-a)$
        MATCH! Stack: $, W               Input: "=a*(a-a)$"
        MATCH! Stack: $, E               Input: "a*(a-a)$"
        MATCH! Stack: $, Q, R            Input: "*(a-a)$"
        MATCH! Stack: $, Q, R, F         Input: "(a-a)$"
        MATCH! Stack: $, Q, R, ), E      Input: "a-a)$"
        MATCH! Stack: $, Q, R, ), Q, R   Input: "-a)$"
        MATCH! Stack: $, Q, R, ), Q, T   Input: "a)$"
        MATCH! Stack: $, Q, R, ), Q, R   Input: ")$"
        MATCH! Stack: $, Q, R            Input: "$"
        MATCH! Stack:                    Input: ""
ACCEPTED


Input: a=(a+a)a$
        MATCH! Stack: $, W               Input: "=(a+a)a$"
        MATCH! Stack: $, E               Input: "(a+a)a$"
        MATCH! Stack: $, Q, R, ), E      Input: "a+a)a$"
        MATCH! Stack: $, Q, R, ), Q, R   Input: "+a)a$"
        MATCH! Stack: $, Q, R, ), Q, T   Input: "a)a$"
        MATCH! Stack: $, Q, R, ), Q, R   Input: ")a$"
        MATCH! Stack: $, Q, R            Input: "a$"
REJECTED
"""
from enum import auto
from enum import Enum


class State(Enum):
    S = 0
    W = auto()
    E = auto()
    Q = auto()
    T = auto()
    R = auto()
    F = auto()


class Transition(Enum):
    BLANK = auto()
    aW = auto()
    eq_E = auto()
    TQ = auto()
    LAMBDA = auto()
    ADD_TQ = auto()
    SUB_TQ = auto()
    FR = auto()
    MULT_FR = auto()
    DIV_FR = auto()
    a = auto()
    PAREN_E = auto()


char_to_col = {
    "a": 0,
    "=": 1,
    "+": 2,
    "-": 3,
    "*": 4,
    "/": 5,
    "(": 6,
    ")": 7,
    "$": 8,
}

TT = [
    [  # S
        Transition.aW,  # a
        Transition.BLANK,  # =
        Transition.BLANK,  # +
        Transition.BLANK,  # -
        Transition.BLANK,  # *
        Transition.BLANK,  # /
        Transition.BLANK,  # (
        Transition.BLANK,  # )
        Transition.BLANK,  # $
    ],
    [  # W
        Transition.BLANK,  # a
        Transition.eq_E,  # =
        Transition.BLANK,  # +
        Transition.BLANK,  # -
        Transition.BLANK,  # *
        Transition.BLANK,  # /
        Transition.BLANK,  # (
        Transition.BLANK,  # )
        Transition.BLANK,  # $
    ],
    [  # E
        Transition.TQ,  # a
        Transition.BLANK,  # =
        Transition.BLANK,  # +
        Transition.BLANK,  # -
        Transition.BLANK,  # *
        Transition.BLANK,  # /
        Transition.TQ,  # (
        Transition.BLANK,  # )
        Transition.BLANK,  # $
    ],
    [  # Q
        Transition.BLANK,  # a
        Transition.BLANK,  # =
        Transition.ADD_TQ,  # +
        Transition.SUB_TQ,  # -
        Transition.BLANK,  # *
        Transition.BLANK,  # /
        Transition.BLANK,  # (
        Transition.LAMBDA,  # )
        Transition.LAMBDA,  # $
    ],
    [  # T
        Transition.FR,  # a
        Transition.BLANK,  # =
        Transition.BLANK,  # +
        Transition.BLANK,  # -
        Transition.BLANK,  # *
        Transition.BLANK,  # /
        Transition.FR,  # (
        Transition.BLANK,  # )
        Transition.BLANK,  # $
    ],
    [  # R
        Transition.BLANK,  # a
        Transition.BLANK,  # =
        Transition.LAMBDA,  # +
        Transition.LAMBDA,  # -
        Transition.MULT_FR,  # *
        Transition.DIV_FR,  # /
        Transition.BLANK,  # (
        Transition.LAMBDA,  # )
        Transition.LAMBDA,  # $
    ],
    [  # F
        Transition.a,  # a
        Transition.BLANK,  # =
        Transition.BLANK,  # +
        Transition.BLANK,  # -
        Transition.BLANK,  # *
        Transition.BLANK,  # /
        Transition.PAREN_E,  # (
        Transition.BLANK,  # )
        Transition.BLANK,  # $
    ],
]

strings = ["a=(a+a)*a$", "a=a*(a-a)$", "a=(a+a)a$"]

for string in strings:
    stack = ["$", State.S]
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
            elif result == Transition.aW:
                stack.append(State.W)
                stack.append("a")
            elif result == Transition.eq_E:
                stack.append(State.E)
                stack.append("=")
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
            elif result == Transition.a:
                if cur_char != "a":
                    break
                cur_char = None
            else:
                print("UNKNOWN TRANSITION", result)
                break
        if cur_char is None:
            stack_str = "Stack: " + ", ".join(x.name if isinstance(x, State) else x for x in stack)
            input_str = 'Input: "' + "".join(input) + '"'
            print(f"\tMATCH! {stack_str:<25} {input_str}")
    print("ACCEPTED" if len(stack) == 0 and len(input) == 0 else "REJECTED")
    print("\n")
