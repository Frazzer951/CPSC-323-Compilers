import sys

from clean_input import clean_input
from generate import generate_python_program
from parse import parse_identifiers_and_nums
from parse import parse_tokens

DEBUG = False


def main(argv):
    # Make sure we have the correct number of arguments
    if len(argv) != 2:
        print("Usage: python compiler.py <filename>")
        return

    # Get the filename
    filename = argv[1]

    # Read the file
    try:
        file = open(filename)
        lines = file.read().splitlines()
        file.close()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return

    # Clean the input
    cleaned = clean_input(lines)

    # Save the cleaned input
    with open(filename.split(".")[0] + "_cleaned.txt", "w") as file:
        file.write("\n".join([" ".join(line) for line in cleaned]))

    # Turn the 2D list into a 1D list of tokens
    tokens = []
    for line in cleaned:
        tokens += line

    # Get the identifiers and numbers from the tokens
    valid, identifiers, numbers = parse_identifiers_and_nums(tokens)

    if DEBUG:
        print("Tokens:", tokens)
        print("Identifiers:", identifiers)
        print("Numbers", numbers)

    # If any of the identifiers or numbers are invalid, print an error message
    if not valid:
        print("REJECTED: Invalid input")
        return

    # Parse the whole program
    valid, variables, operations, prog_name = parse_tokens(tokens, identifiers, numbers, DEBUG)

    if DEBUG:
        print("Variables:", variables)
        print("Stats:", operations)

    # If the program is invalid, print an error message
    if not valid:
        print("REJECTED: Invalid input")
        return

    # Generate the python program
    generate_python_program(filename.split(".")[0] + ".py", variables, operations, prog_name)


if __name__ == "__main__":
    main(sys.argv)
