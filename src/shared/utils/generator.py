from Crypto.Random import random
import string

alnum = list(string.ascii_letters)

def genState(length: int):
    """Generates random alphanumeric string of specified length

    Args:
        length (int): length of string

    Returns:
        str: alphanumeric string
    """
    return ''.join(random.choice(alnum) for _ in range(length))
