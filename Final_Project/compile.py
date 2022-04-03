import sys

from clean_input import clean_input
from parse import parse_identifiers_and_nums

DEBUG = True


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

    tokens = []
    for line in cleaned:
        tokens += line

    valid, identifiers, numbers = parse_identifiers_and_nums(tokens)

    if DEBUG:
        print("Tokens:", tokens)
        print("Identifiers:", identifiers)
        print("Numbers", numbers)

    if not valid:
        print("REJECTED: Invalid input")
        return


if __name__ == "__main__":
    main(sys.argv)
