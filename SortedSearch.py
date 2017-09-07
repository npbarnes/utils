from bisect import bisect_left, bisect_right
import numpy as np

def index(a, x, reverse=False):
    'Locate the leftmost value exactly equal to x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='left', sorter=sorter)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x, reverse=False):
    'Find rightmost value less than x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='left', sorter=sorter)
    if i:
        return i-1, a[i-1]
    raise ValueError

def find_le(a, x, reverse=False):
    'Find rightmost value less than or equal to x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='right', sorter=sorter)
    if i:
        return i-1, a[i-1]
    raise ValueError

def find_gt(a, x, reverse=False):
    'Find leftmost value greater than x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='right', sorter=sorter)
    if i != len(a):
        return i, a[i]
    raise ValueError

def find_ge(a, x, reverse=False):
    'Find leftmost item greater than or equal to x'
    sorter = range(len(a))
    if reverse:
        sorter = list(reversed(sorter))

    i = np.searchsorted(a, x, side='left', sorter=sorter)
    if i != len(a):
        return i, a[i]
    raise ValueError
