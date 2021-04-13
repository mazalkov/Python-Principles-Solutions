# https://pythonprinciples.com/challenges/Randomness/


# only import the method as the whole library isn't required
from random import randint


def random_number():
    # no need for 'random.randint' as we only imported randint
    return randint(1, 100)
