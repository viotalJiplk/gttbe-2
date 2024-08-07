from Crypto.Random import random
import string

alnum = list(string.ascii_letters)

def genState(length):
    return ''.join(random.choice(alnum) for _ in range(length))
