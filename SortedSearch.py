import numpy as np

def index(a, x, reverse=False):
    'Locate the leftmost (or rightmost if reversed) value exactly equal to x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='left', sorter=sorter)

    if i != len(a) and a[sorter[i]] == x:
        return sorter[i]
    raise ValueError("Couldn't find x in a")

def find_lt(a, x, reverse=False):
    'Find largest (rightmost normally, leftmost when reversed) value less than x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='left', sorter=sorter)

    if i:
        return sorter[i-1], a[sorter[i-1]]
    raise ValueError("No value in a less than {}".format(x))

def find_le(a, x, reverse=False):
    'Find largest (rightmost normally, leftmost when reversed) value less than or equal to x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='right', sorter=sorter)

    if i:
        return sorter[i-1], a[sorter[i-1]]
    raise ValueError("No value in a less than or equal to {}".format(x))

def find_gt(a, x, reverse=False):
    'Find least (leftmost normally, rightmost when reversed) value greater than x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='right', sorter=sorter)

    if i != len(a):
        return sorter[i], a[sorter[i]]
    raise ValueError("No value in a greater than {}".format(x))

def find_ge(a, x, reverse=False):
    'Find least (leftmost normally, rightmost when reversed) item greater than or equal to x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='left', sorter=sorter)

    if i != len(a):
        return sorter[i], a[sorter[i]]
    raise ValueError("No value in a greater than or equal to {}".format(x))
