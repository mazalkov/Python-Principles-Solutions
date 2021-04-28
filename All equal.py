# https://pythonprinciples.com/challenges/All-equal/


def all_equal(l):

    return True if len(l) == 0 else (l.count(l[0]) == len(l))
