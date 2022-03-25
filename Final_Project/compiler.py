import sys

from clean_input import clean_input


def main(argv):
    if len(argv) != 2:
        print("Usage: python compiler.py <filename>")
        return 1

    filename = argv[1]

    try:
        file = open(filename)
        lines = file.read().splitlines()
        file.close()
    except FileNotFoundError:
        print(f"File {filename} not found")

    cleaned = clean_input(lines)
    print(cleaned)

    with open(filename.split(".")[0] + "_cleaned.txt", "w") as file:
        file.write("\n".join([" ".join(line) for line in cleaned]))


if __name__ == "__main__":
    main(sys.argv)
