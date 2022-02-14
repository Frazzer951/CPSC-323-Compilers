def is_identifier(token):
    if not (token[0].isalpha() or token[0] == "_"):
        return False
    for c in token[1:]:
        if not (c.isalnum() or c == "_" or c.isdigit()):
            return False
    return True


if __name__ == "__main__":
    reserved_words = ["while", "for", "switch", "do", "return"]

    filename = input("Enter the filename: ")
    with open(filename, "r") as f:
        file = f.read()

    file = file.split("\n")
    longest = max(len(x) for x in file)
    print(f"{'Token':<{longest+2}} Number Identifier Reserved Word")
    for line in file:
        line = line.lower()
        number = False
        identifier = False
        reserved = False

        if line in reserved_words:
            reserved = True
        elif line.isdigit():
            number = True
        elif is_identifier(line):
            identifier = True

        number = "yes" if number else "no"
        identifier = "yes" if identifier else "no"
        reserved = "yes" if reserved else "no"
        print(f"{line:<{longest+2}} {number: <6} {identifier: <10} {reserved}")

'''
Enter the filename: token_file.txt
Token      Number Identifier Reserved Word
k-mart     no     no         no
23andme    no     no         no
456        yes    no         no
tax 2018   no     no         no
while      no     no         yes
switch     no     no         yes
do_it      no     yes        no
_fall_20   no     yes        no
_jan 19    no     no         no
'''