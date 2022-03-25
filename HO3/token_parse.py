def is_identifier(token):
    # Check if token is an identifier
    # And identifier must start with a letter or and underscore
    # And identifier must contain only letters, numbers, and underscores
    if not (token[0].isalpha() or token[0] == "_"):
        return False
    for c in token[1:]:
        if not (c.isalnum() or c == "_" or c.isdigit()):
            return False
    return True


if __name__ == "__main__":
    # Define reserved words
    reserved_words = ["while", "for", "switch", "do", "return"]

    # Get the file with the tokens
    filename = input("Enter the filename: ")
    with open(filename) as f:
        file = f.read()

    file = file.split("\n")  # Split file by new-lines
    longest = max(len(x) for x in file)  # Find the longest token for formatting
    print(f"{'Token':<{longest+2}} Number Identifier Reserved Word")
    for line in file:
        # Setup variables
        number = False
        identifier = False
        reserved = False

        # Check what type the token is
        if line in reserved_words:
            reserved = True
        elif line.isdigit():
            number = True
        elif is_identifier(line):
            identifier = True

        # Print the token and its type
        number = "yes" if number else "no"
        identifier = "yes" if identifier else "no"
        reserved = "yes" if reserved else "no"
        print(f"{line:<{longest+2}} {number: <6} {identifier: <10} {reserved}")

"""
Enter the filename: token_file.txt
Token      Number Identifier Reserved Word
K-mart     no     no         no
23andMe    no     no         no
456        yes    no         no
Tax 2018   no     no         no
While      no     yes        no
switch     no     no         yes
do_it      no     yes        no
_Fall_20   no     yes        no
_Jan 19    no     no         no
"""
