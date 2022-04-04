from typing import List


def generate_python_program(filename: str, variables: List[str], operations: List[List[str]], prog_name: str):
    """
    Generates a Python program from the given variables and operations.
    """
    with open(filename, "w") as file:
        file.write(f"# Program {prog_name}\n\n")
        vars = " = ".join(variables)
        file.write(f"{vars} = 0\n")

        for operation in operations:
            if "=" in operation:
                file.write(f"{' '.join(operation)}\n")
            elif "write" in operation:
                file.write(f"print{' '.join(operation[1:])}\n")
