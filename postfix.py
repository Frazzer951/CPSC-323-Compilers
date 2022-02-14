def add(a, b):
    # Add two numbers
    return a + b


def sub(a, b):
    # Subtract two numbers
    return a - b


def mul(a, b):
    # Multiply two numbers
    return a * b


def div(a, b):
    # Divide two numbers
    return a / b


if __name__ == "__main__":
    # Create map of operater to its function
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }

    # Keep looping until user chooses to exit
    loop = True
    while loop:
        stack = []
        print("Enter a postfix expression with spaces between each element. ")
        val = input("Enter your expression: ")
        val = val.strip()  # Remove whitespace
        val = val.split()  # Split input into list of elements

        # Loop through each element in the list
        for element in val:
            if element.isnumeric():
                # If element is a number, push it to the stack
                stack.append(int(element))
            elif element in ["+", "-", "/", "*"]:
                # If element is an operator, pop two numbers from the stack
                # And apply the operator to them
                val2 = stack.pop()
                val1 = stack.pop()
                op_func = ops[element]
                result = op_func(val1, val2)
                stack.append(result)
            elif element == "$":
                # If element is $, end of expression has been reached
                break
            else:
                # If element is not a number or operator, treat it as a variable
                # And take user's input for its value
                var_value = input("What is the value of " + element + ": ")
                stack.append(int(var_value))

        # Display the result
        print("The expression evaluates to:", stack[-1])

        # Ask user if they want to continue
        continueLoop = input("Continue? y/n: ")
        if continueLoop.lower()[0] == "n":
            break

"""
Example Run:
    Enter a postfix expression with spaces between each element.
    Enter your expression: 20  num1  45 + tom  -  * $
    What is the value of num1: 10
    What is the value of tom: 5
    The expression evaluates to: 1000
    Continue? y/n: y
    Enter a postfix expression with spaces between each element.
    Enter your expression: myscore  yourscore  45 +  100 +  * $
    What is the value of myscore: 3
    What is the value of yourscore: 5
    The expression evaluates to: 450
    Continue? y/n: y
    Enter a postfix expression with spaces between each element.
    Enter your expression: 10 15 20 + -
    The expression evaluates to: -25
    Continue? y/n: n

"""
