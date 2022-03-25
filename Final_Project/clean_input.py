from typing import List


def clean_input(lines: List[str]) -> List[List[str]]:
    """
    Cleans the input by removing comments and blank lines.
    Also removed redundant whitespace.
    """
    cleaned = []
    in_comment = False
    for line in lines:
        line_parts = line.strip().split(" ")
        cleaned_line = []
        for part in line_parts:
            if not in_comment and "/*" in part:
                in_comment = True
                continue
            if in_comment and "*/" in part:
                in_comment = False
                continue
            if in_comment:
                continue
            if len(part) == 0 or part.isspace():
                continue
            cleaned_line.append(part)
        if len(cleaned_line) > 0:
            cleaned.append(cleaned_line)
    return cleaned
