import sys


def main(argv):
    print(argv)
    if len(argv) != 2:
        print("Usage: python compiler.py <filename>")
        return 1


if __name__ == "__main__":
    main(sys.argv)
