import difflib
from typing import Union

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def colorDiff(original: str, modified: str, ignoreWhitespace: bool = False):
    if ignoreWhitespace:
        original = [line.rstrip() for line in original.splitlines()]
        modified = [line.rstrip() for line in modified.splitlines()]
    else:
        original = original.splitlines()
        modified = modified.splitlines()

    diff = difflib.ndiff(original, modified)
    result = []

    for line in diff:
        if line.startswith('-'):
            result.append(RED + line[2:] + RESET)  # removed line
        elif line.startswith('+'):
            result.append(GREEN + line[2:] + RESET)  # added line

    return '\n'.join(result)

def diff(original, new):
    if isinstance(original, dict) and isinstance(new, dict):
        return dictDiff(original, new)
    elif isinstance(original, list) and isinstance(new, list):
        return listDiff(original, new)
    elif original is int and (isinstance(new, int) or isinstance(new, str)):
            try:
                int(new)
                return {}
            except ValueError:
                return {"original": original, "new": new}
    elif original is str and isinstance(new, str):
        return {}
    elif original == new:
        return {}
    else:
        return {"original": original, "new": new}


def dictDiff(original: dict, new: dict):
    differences = {}
    for key in original.keys() | new.keys():
        if key not in new:
            differences[key] = {"original": original[key], "new": None}
        else:
            difference = diff(original[key], new[key])
            if difference != {} and difference != []:
                differences[key] = difference

    return differences

def listDiff(original: list, new: list):
    differences = []

    zipped = zip(original, new)

    for originalItem, newItem in zipped:
        difference = diff(originalItem, newItem)
        if difference != {} and difference != []:
            differences.append(difference)

    return differences
