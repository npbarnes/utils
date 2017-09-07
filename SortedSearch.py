from bisect import bisect_left, bisect_right
import numpy as np

def index(a, x, reverse=False):
    'Locate the leftmost (or rightmost if reversed) value exactly equal to x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='left', sorter=sorter)

    if i != len(a) and a[sorter[i]] == x:
        return sorter[i]
    raise ValueError

def find_lt(a, x, reverse=False):
    'Find largest (rightmost normally, leftmost when reversed) value less than x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='left', sorter=sorter)

    if i:
        return sorter[i-1], a[sorter[i-1]]
    raise ValueError

def find_le(a, x, reverse=False):
    'Find largest (rightmost normally, leftmost when reversed) value less than or equal to x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='right', sorter=sorter)

    if i:
        return sorter[i-1], a[sorter[i-1]]
    raise ValueError

def find_gt(a, x, reverse=False):
    'Find least (leftmost normally, rightmost when reversed) value greater than x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='right', sorter=sorter)

    if i != len(a):
        return sorter[i], a[sorter[i]]
    raise ValueError

def find_ge(a, x, reverse=False):
    'Find least (leftmost normally, rightmost when reversed) item greater than or equal to x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='left', sorter=sorter)

    if i != len(a):
        return sorter[i], a[sorter[i]]
    raise ValueError
