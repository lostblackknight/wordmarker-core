import random


def random_list(seq: list):
    for i in seq:
        if i is None:
            seq.remove(i)
    if len(seq) != 0:
        return random.choice(seq)
    else:
        return None


def append_list(*args: list):
    _ = []
    for i in args:
        _.extend(i)
    return _
