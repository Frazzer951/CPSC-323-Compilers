from typing import List


def clean_input(lines: List[str]) -> List[List[str]]:
    """
    Cleans the input by removing comments and blank lines.
    Also removed redundant whitespace.
    """
    cleaned = []
    in_comment = False
    for line in lines:
        line_parts = line.strip().split(" ")  # Remove whitespace and split by spaces
        cleaned_line = []
        for part in line_parts:
            if not in_comment and "/*" in part:  # If we're not in a comment and we find a comment start
                in_comment = True  # We're now in a comment
                continue
            if in_comment and "*/" in part:  # If we're in a comment and we find a comment end
                in_comment = False  # We're no longer in a comment
                continue
            if in_comment:
                continue
            if len(part) == 0 or part.isspace():  # If the part is empty or whitespace continue
                continue
            cleaned_line.append(part)
        if len(cleaned_line) > 0:
            cleaned.append(cleaned_line)

    chars_to_seperate = ["(", ")", ";", ",", ":"]

    verified = False

    while not verified:
        verified = True
        for line in cleaned:
            spaced = []
            for token in line:
                modified = False
                if len(token) > 1:
                    for char in chars_to_seperate:
                        if not modified and char in token:
                            verified = False
                            modified = True
                            token = token.replace(char, " " + char + " ")  # Add whitespace around the char
                            seperated = token.split()  # Separate the token
                            seperated = [x.strip() for x in seperated]  # Remove whitespace
                            while "" in seperated:
                                seperated.remove("")
                            spaced += seperated
                if not modified:
                    spaced.append(token)
            line[:] = spaced  # Replace the old line with the new line

    return cleaned
