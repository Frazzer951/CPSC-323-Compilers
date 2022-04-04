from typing import List


def generate_python_program(filename: str, variables: List[str], operations: List[List[str]], prog_name: str):
    """
    Generates a Python program from the given variables and operations.
    """
    # Open/Create the file
    with open(filename, "w") as file:
        # Write the program name
        file.write(f"# Program {prog_name}\n\n")

        # Declare the variables
        vars = " = ".join(variables)
        file.write(f"{vars} = 0\n")

        # Write the operations
        for operation in operations:
            if "=" in operation:  # Assignment
                file.write(f"{' '.join(operation)}\n")
            elif "write" in operation:  # Write
                file.write(f"print{' '.join(operation[1:])}\n")
