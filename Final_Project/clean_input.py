from typing import List


def clean_input(lines: List[str]) -> List[List[str]]:
    """
    Cleans the input by removing comments and blank lines.
    Also removed redundant whitespace.
    """
    cleaned = []  # The cleaned input
    in_comment = False  # Whether we're in a comment
    for line in lines:  # Loop through each line
        line_parts = line.strip().split(" ")  # Remove whitespace and split by spaces
        cleaned_line = []  # The cleaned line
        for part in line_parts:
            if not in_comment and "/*" in part:  # If we're not in a comment and we find a comment start
                in_comment = True  # We're now in a comment
                continue
            if in_comment and "*/" in part:  # If we're in a comment and we find a comment end
                in_comment = False  # We're no longer in a comment
                continue
            if in_comment:  # If we're in a comment
                continue  # Skip this part
            if len(part) == 0 or part.isspace():  # If the part is empty or whitespace continue
                continue
            cleaned_line.append(part)  # Otherwise add the part to the cleaned line
        if len(cleaned_line) > 0:  # If the cleaned line is not empty
            cleaned.append(cleaned_line)  # Add the cleaned line to the cleaned input

    chars_to_seperate = ["(", ")", ";", ",", ":"]  # The characters that should be seperated

    verified = False  # Whether we've verified the cleaned input

    while not verified:  # While we haven't verified the cleaned input
        verified = True
        for line in cleaned:  # Loop through each line
            spaced = []  # New line with special characters seperated
            for token in line:  # Loop through each token
                modified = False  # Whether we've modified the token
                if len(token) > 1:  # If the token is more than one character long
                    for char in chars_to_seperate:  # Loop through each character that should be seperated
                        if not modified and char in token:
                            verified = False
                            modified = True
                            seperated = token.split(char)  # Seperate the token
                            seperated = [x.strip() for x in seperated]  # Remove whitespace
                            while "" in seperated:
                                seperated.remove("")
                            spaced += [seperated[0], char] + seperated[1:]  # Add the seperated tokens to the new line
                if not modified:  # If we haven't modified the token
                    spaced.append(token)  # Add the token to the new line
            line[:] = spaced  # Replace the old line with the new line

    return cleaned
