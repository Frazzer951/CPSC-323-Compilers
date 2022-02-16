def main():
    # CFG:
    # S -> aS | bB | cC
    # B -> bB | aC | cD | λ
    # C -> aS | bD | cD | λ
    # D -> bD | aB | cC

    tt = [[0, 1, 2], [2, 1, 3], [0, 3, 3], [1, 3, 2]]  # Transition table for above CFG
    final_states = [1, 2]  # Final states for above CFG

    # Get input string from user
    string = input("Enter a string with a $ at the end: ")

    # Setup variables starting at state 0
    state = 0
    i = 0
    col = 0

    # Loop through string and check if it is accepted
    while i < len(string):
        if string[i] == "a":
            col = 0
        elif string[i] == "b":
            col = 1
        elif string[i] == "c":
            col = 2
        elif string[i] == "$":
            if state in final_states:
                print(f"{string} is accepted by the CFG")
            else:
                print(f"{string} is rejected by the CFG")
            return
        state = tt[state][col]
        i += 1


if __name__ == "__main__":
    main()

"""
w1=abbbcaaa$:
    Enter a string with a $ at the end: abbbcaaa$
    abbbcaaa$ is rejected by the CFG

w2=ccccbbb$:
    Enter a string with a $ at the end: ccccbbb$
    ccccbbb$ is rejected by the CFG

w3=aabbcbbb$:
    Enter a string with a $ at the end: aabbcbbb$
    aabbcbbb$ is rejected by the CFG

w4=aabbcccc$:
    Enter a string with a $ at the end: aabbcccc$
    aabbcccc$ is accepted by the CFG
"""
